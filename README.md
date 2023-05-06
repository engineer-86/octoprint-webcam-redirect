# Octoprint Webcam Redirect

A Python Flask application that redirects Octoprint webcams to a local URL for easier integration with other applications.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Customization](#customization)
- [Environment Variables](#environment-variables)
  - [INTERNAL_URLS](#internal_urls)
  - [USERNAME and PASSWORD](#username-and-password)
- [License](#license)

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

The application can be customized via environment variables. See the [Environment Variables](#environment-variables) section for details.

## Environment Variables

### `INTERNAL_URLS`

`INTERNAL_URLS` is an environment variable that contains a list of URLs that point to internal webcams. These URLs are used by the application to receive and display video feeds from the webcams. The URLs should be comma-separated and enclosed in quotation marks. Here's an example:

```
INTERNAL_URLS="http://192.168.10.95/webcam/?action=stream,http://192.168.10.95:8081/?action=stream"
```


### `USERNAME` and `PASSWORD`

`USERNAME` and `PASSWORD` are environment variables used for authenticating users who want to access the webcam feeds. If you don't set these variables, no authentication is required. However, if you want to increase security, you can set a combination of a username and password that restricts access to the feeds.

You can set these variables like this:

```
USERNAME=myuser
PASSWORD=mypassword
```


Note that the username and password are stored as plaintext in the environment variable, which poses a security risk. To minimize this risk, you should ensure that the environment variables are securely stored on your system.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Docker Support

This project also includes support for Docker, making it easy to run the project in a container.

