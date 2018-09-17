#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/gary/Downloads/My Project API.json"
python3 twitter.py
python3 google.py
ffmpeg -r 1 -f image2 -s 1080*720 -i /home/gary/EC601/picture2/%04d.jpg -pix_fmt yuv420p /home/gary/EC601/test.mp4





