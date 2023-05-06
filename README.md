# Octoprint Webcam Redirect

A Python Flask application that redirects Octoprint webcams to a local URL for easier integration with other applications.

## Features

- Multiple webcams can be redirected simultaneously
- Simple authentication mechanism to restrict access to the webcams
- Uses multipart streaming to efficiently stream video from the webcams
- Customizable via environment variables

## Usage

1. Clone this repository to your machine.
2. Set the `INTERNAL_URLS` environment variable to a comma-separated list of internal webcam URLs. For example: `export INTERNAL_URLS="http://192.168.10.95/webcam/?action=stream,http://192.168.10.95:8081/?action=stream"`
3. Set the `USERNAME` and `PASSWORD` environment variables to the desired username and password for authentication.
4. Run the application with `python main.py`.
5. Access the redirected webcams via the URLs `http://localhost:8000/api/cam1` and `http://localhost:8000/api/cam2` (replace `cam1` and `cam2` with the appropriate camera number).

## Customization

The application can be customized via the following environment variables:

- `INTERNAL_URLS`: A comma-separated list of internal webcam URLs.
- `USERNAME`: The username for basic authentication.
- `PASSWORD`: The password for basic authentication.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
