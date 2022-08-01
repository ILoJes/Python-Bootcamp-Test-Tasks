import os.path
from moviepy.editor import VideoFileClip

test_url = "https://v16-webapp.tiktok.com/a1f807e363d688ef3c4ce1a1a0f688dc/62e85cb2/video/tos/useast2a/tos-useast2a-ve-0068c004/68ba42ffc5674ce6803cd729c00a39e3/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3402&bt=1701&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZjSjKwe2ND7JLl7Gb&mime_type=video_mp4&qs=0&rc=NDw5MzpoaTg1NjNlODc6NkBpM2h0ZWY6ZndsZDMzNzczM0BjMTFgXzBfXzExLl4vX2EvYSNpazVgcjRfMG1gLS1kMTZzcw%3D%3D&l=2022080117064001021702822122472F13"


def convert_tiktok_to_gif(url):
    file_path = "TikTok-example-1.gif"
    try:
        videoClip = VideoFileClip(url)
        videoClip.write_gif(file_path)
        return os.path.abspath(file_path)
    except:
        return ""


print(convert_tiktok_to_gif(test_url))
