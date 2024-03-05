from flask import render_template, current_app, request, send_file, redirect, url_for, flash
import logging, os
from pathlib import Path
import zipfile
from config import Config
from . import main_bp

logger = logging.getLogger(__name__)

UPLOAD_FOLDER = Config.UPLOAD_FOLDER

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload/', methods=['GET'])
def upload():
    return render_template('upload.html')

@main_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        # Redirect to the download route if the file does not exist
        flash(f'File not found: {filename}', 'error')
        return redirect(url_for('main.download'))
    

@main_bp.route('/download/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        selected_files = request.form.getlist('file_checkbox')

        if len(selected_files) == 1:
            # If only one file is selected, provide a direct download link
            return send_file(os.path.join(current_app.config['UPLOAD_FOLDER'], selected_files[0]), as_attachment=True)
        
        elif len(selected_files) > 1:
            zip_file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'selected_files.zip')

            # Create a ZIP archive containing selected files within a common folder
            common_folder_name = 'selected_files'
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for file_name in selected_files:
                    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
                    arcname = os.path.join(common_folder_name, os.path.basename(file_name))
                    zipf.write(file_path, arcname=arcname)

            # Send the ZIP archive to the user
            return send_file(Path(zip_file_path).absolute(), as_attachment=True)

    # If the request method is GET, render the download.html template
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('download.html', files=files)