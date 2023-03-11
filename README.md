# octoprint-webcam-redirect

This is a Python Flask web application that streams video from a webcam to a web page. The web page updates the video in real-time, so it gives the appearance of a live stream.

## Setup

1. Clone this repository to your local machine.
2. Install Docker on your machine if not already installed.
3. Build the Docker image with the command: `docker build -t octoprint-webcam-redirect .`
4. Set the environment variables `USERNAME` and `PASSWORD` to your desired basic authentication credentials.
5. Edit the `urls` list in `main.py` to contain the URLs for your desired webcam streams.
6. Run the Docker container with the command: `docker run -p 8000:8000 -e USERNAME=$USERNAME -e PASSWORD=$PASSWORD octoprint-webcam-redirect`

## Usage

Navigate to `http://localhost:8000` in a web browser to view the video stream. You will be prompted to enter the basic authentication credentials you set up in step 4. Once authenticated, you should see the live video stream from your webcam.

## API

This application exposes an API for each webcam stream in the `urls` list. The API endpoints are as follows:

- `/api/video-feed`: Returns the video feed for the first webcam stream in the `urls` list.
- `/api/video-feed-2`: Returns the video feed for the second webcam stream in the `urls` list. (Add more routes as needed for additional streams.)

You can access the API endpoints by appending them to the base URL of the application.
