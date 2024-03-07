# ShareHub

ShareHub is a Flask web application designed to facilitate easy file sharing across different devices. Users can upload files to the app, which are then locally saved on the server. This allows users to access and download their files from anywhere on the internet, making it a convenient solution for scenarios such as sharing files between different devices or accessing files needed for printing.

- Programmer: [Indrajit Ghosh](https://github.com/indrajit912)
- Repo: https://github.com/indrajit912/ShareHub

## Features

- Upload files from any device with internet access.
- Access and download uploaded files from anywhere.
- Simple and user-friendly interface.

## Getting Started

### Prerequisites

- Python 3
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/indrajit912/ShareHub.git
   cd ShareHub
   ```
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python3 run.py
    ```
4. Open your web browser and navigate to http://localhost:8080 to access ShareHub.

## Usage
- Upload files by clicking on the "Upload" button.
- Access your files from any device with an internet connection.
- Download files as needed.

## Running as a Systemd Service (Ubuntu)
1. Create a systemd service file:
    ```bash
    [Unit]
    Description=ShareHub Flask Application
    After=network.target

    [Service]
    User=<your-ubuntu-username>
    Group=<your-ubuntu-group>
    WorkingDirectory=/home/<path-to>/ShareHub
    Environment="PATH=/home/<path-to>/ShareHub/env/bin"
    ExecStart=/home/<path-to>/ShareHub/env/bin/python run.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

    ```
    Make sure to replace <your-ubuntu-username> and <your-ubuntu-group> with your actual Ubuntu username and group. Also, adjust the path to the virtual environment and the run.py script accordingly.

2. Move the file to the systemd directory:
    ```bash
    sudo cp sharehub.service /etc/systemd/system/
    ```
3. Reload systemd and start the service:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start sharehub
    ```
4. Enable the service to start on boot (Optional):
    ```bash
    sudo systemctl enable sharehub
    ```
5. Check the status of the service:
    ```bash
    sudo systemctl status sharehub
    ```

## Contributing
If you'd like to contribute to ShareHub, please fork the repository and create a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License
ShareHub is licensed under the [MIT License](LICENSE).
