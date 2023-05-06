import requests


def gen_frames(cam_url_list):
    for cam_url in cam_url_list:
        stream = requests.get(cam_url, stream=True)
        stream_bytes = b''
        for stream_chunk in stream.iter_content(chunk_size=1024):
            stream_bytes += stream_chunk
            frame_start = stream_bytes.find(b'\xff\xd8')  # search start for frame
            frame_end = stream_bytes.find(b'\xff\xd9')  # search end of frame
            if frame_start != -1 and frame_end != -1:
                full_frame = stream_bytes[frame_start:frame_end + 2]
                stream_bytes = stream_bytes[frame_end + 2:]
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + full_frame + b'\r\n')
