from app import create_app

app = create_app()

if __name__ == '__main__':
    if not app.config['UPLOAD_FOLDER'].exists():
        app.config['UPLOAD_FOLDER'].mkdir()

    app.run(host='0.0.0.0', port=8080)
    