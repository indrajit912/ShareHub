# app/api/routes.py
# Author: Indrajit Ghosh
# Created On: Mar 05, 2024
# 

import logging
import os
from flask import request, make_response, current_app
from werkzeug.utils import secure_filename
from . import api_bp

logger = logging.getLogger(__name__)

@api_bp.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']

    save_path = current_app.config['UPLOAD_DIR'] / secure_filename(file.filename)
    current_chunk = int(request.form['dzchunkindex'])

    # If the file already exists it's ok if we are appending to it,
    # but not if it's new file that would overwrite the existing one
    if os.path.exists(save_path) and current_chunk == 0:
        # 400 and 500s will tell dropzone that an error occurred and show an error
        return make_response(('File already exists', 400))

    try:
        with open(save_path, 'ab') as f:
            f.seek(int(request.form['dzchunkbyteoffset']))
            f.write(file.stream.read())
    except OSError:
        # log.exception will include the traceback so we can see what's wrong 
        logger.exception('Could not write to file')
        return make_response(("Not sure why,"
                              " but we couldn't write the file to disk", 500))

    total_chunks = int(request.form['dztotalchunkcount'])

    if current_chunk + 1 == total_chunks:
        # This was the last chunk, the file should be complete and the size we expect
        if os.path.getsize(save_path) != int(request.form['dztotalfilesize']):
            logger.error(f"File {file.filename} was completed, "
                      f"but has a size mismatch."
                      f"Was {os.path.getsize(save_path)} but we"
                      f" expected {request.form['dztotalfilesize']} ")
            return make_response(('Size mismatch', 500))
        else:
            logger.info(f'File {file.filename} has been uploaded successfully')
    else:
        logger.debug(f'Chunk {current_chunk + 1} of {total_chunks} '
                  f'for file {file.filename} complete')
        
    return make_response(("Chunk upload successful", 200))