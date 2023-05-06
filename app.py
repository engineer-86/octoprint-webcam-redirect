import os
import json
from flask import Flask, Response
from flask_basicauth import BasicAuth

from stream import gen_frames

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ["USERNAME"]
app.config['BASIC_AUTH_PASSWORD'] = os.environ["PASSWORD"]
basic_auth = BasicAuth(app)

internal_urls = json.loads(os.environ["INTERNAL_URLS"])
api_urls = [f"http://localhost:8000/api/cam{i + 1}" for i in range(len(internal_urls))]


@app.route('/')
@basic_auth.required
def index():
    urls = api_urls
    video_tiles = ''
    for i, url_cam in enumerate(urls):
        video_tiles += f'<div class="video-tile"> \
                        <img src="{api_urls[i]}" width="320" height="240" /> \
                        <br /> \
                        <a href="{url_cam}" target="_blank">{url_cam}</a> \
                        </div>'
    page_content = f'<html><head><link rel="stylesheet" href="/static/style.css"></head>\
                     <body>\
                     <h1>Webcams</h1>\
                     {video_tiles}\
                     </body></html>'
    return page_content


for i, url in enumerate(internal_urls):
    route = f'/api/cam{i + 1}'


    def camera_func(internal_urls_index):
        def camera():
            return Response(gen_frames([internal_urls[internal_urls_index]]), mimetype='multipart/x-mixed-replace; boundary=frame')

        return camera


    app.add_url_rule(route, view_func=camera_func(i), endpoint=f"camera{i + 1}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
