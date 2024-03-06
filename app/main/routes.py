# app/main/routes.py
# Author: Indrajit Ghosh
# Created On: Mar 05, 2024
# 

import logging
from pathlib import Path

from flask import render_template, current_app, request, send_file, redirect, url_for, flash, make_response
from . import main_bp

logger = logging.getLogger(__name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload/', methods=['GET'])
def upload():
    return render_template('upload.html')

@main_bp.route('/all_files/', methods=['GET'])
def all_files():
    upload_dir:Path = current_app.config['UPLOAD_DIR']
    files = [x for x in upload_dir.glob('**/*') if x.is_file()]

    return render_template('all_files.html', files=files)


@main_bp.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    file_path:Path = current_app.config['UPLOAD_DIR'] / filename

    if file_path.exists():
        return send_file(file_path, as_attachment=True)
    else:
        # Redirect to the download route if the file does not exist
        flash(f'File not found: {filename}', 'error')
        return make_response(('ERROR: File not found!', 404))


@main_bp.route('/delete/<filename>', methods=['GET', 'POST'])
def delete_file(filename):
    file_path:Path = current_app.config['UPLOAD_DIR'] / filename

    if file_path.exists():
        file_path.unlink()
        flash("File deleted successfully!", 'success')
        return redirect(url_for('main.all_files'))
    else:
        # Redirect to the download route if the file does not exist
        flash(f'File not found: {filename}', 'error')
        return make_response(('ERROR: File not found!', 404))