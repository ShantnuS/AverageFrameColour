#pip install list:
# pytube
# opencv-python
# pillow

from pytube import YouTube
import cv2
import os 
import shutil
from PIL import Image, ImageStat

#Get average colour of frames
def get_average_colour(image_name, colour_list):
  image = Image.open(frame_folder+"/"+image_name)
  average = ImageStat.Stat(image).median
  colour_list.append(average)
  print(image_name + ": " + str(average))
  
video_url = "https://www.youtube.com/watch?v=hMILDJ_l5ik"

download_folder = "cache"
download_name = "test"
frame_folder = os.path.join(download_folder,"frames")

try:
  shutil.rmtree(download_folder)
except FileNotFoundError:
  print(download_folder + " folder does not exist. Creating one!")

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
colour_list = []
while success:
  if count % round(fps) == 0:
    frame_name = "frame%d.jpg" % count
    cv2.imwrite(frame_folder+"/"+frame_name, image)     # save frame as JPEG file
    get_average_colour(frame_name, colour_list)
  success,image = vidcap.read()
  count += 1
