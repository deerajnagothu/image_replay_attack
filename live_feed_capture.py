import cv2
import numpy as np
import time
import base64
import urllib3


from foscam import FoscamCamera

cam = FoscamCamera("192.168.2.10", "88", "admin", "cns2202")

cam.ptz_move_down()
#cam.ptz_move_up()

#cam.flip_video(0)
cam.get_video_stream_param()

cam.get

