#pip install list:
# pytube
# opencv-python
# pillow

from pytube import YouTube
import cv2
import os 
import shutil
from PIL import Image, ImageStat


video_url = "https://www.youtube.com/watch?v=hMILDJ_l5ik"

download_folder = "cache"
download_name = "test"
frame_folder = os.path.join(download_folder,"frames")

shutil.rmtree(download_folder)

#Make sure folders exist
os.makedirs(download_folder, exist_ok=True)
os.makedirs(frame_folder, exist_ok=True)

#Download video
video = YouTube(video_url)
stream = video.streams.filter(mime_type="video/mp4",res="360p").all()[0]
stream.download(download_folder, download_name)

#Get frames from video (once every second)
vidcap = cv2.VideoCapture(download_folder+"/"+download_name+".mp4")
fps = vidcap.get(cv2.CAP_PROP_FPS)
success,image = vidcap.read()
count = 0
frame_list = []
while success:
  if count % round(fps) == 0:
    frame_name = "frame%d.jpg" % count
    cv2.imwrite(frame_folder+"/"+frame_name, image)     # save frame as JPEG file
    frame_list.append(frame_name)
  success,image = vidcap.read()
  count += 1

print(frame_list)

#Get average colour of frames
for imagename in frame_list:
  image = Image.open(frame_folder+"/"+imagename)
  average = ImageStat.Stat(image).median
  print(imagename + ": " + str(average))