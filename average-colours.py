#pip install list:
# pytube
# opencv-python
# pillow

from pytube import YouTube
import cv2
import os 
import shutil
from PIL import Image, ImageStat, ImageDraw

#Get average colour of frames
def get_average_colour(image_name, colour_list, frame_folder):
  image = Image.open(frame_folder+"/"+image_name)
  average = ImageStat.Stat(image).mean
  colour_list.append(average)
  
def get_colour_list(download_folder, download_name, frame_folder):
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
      get_average_colour(frame_name, colour_list, frame_folder)
    success,image = vidcap.read()
    count += 1
  return colour_list

def image_scale(index, scale):
  return int(index * scale)

def average_colours(video_url):
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
  print("downloading video...")
  video = YouTube(video_url)
  stream = video.streams.filter(mime_type="video/mp4",res="360p").all()[0]
  stream.download(download_folder, download_name)

  print("averaging colours...")
  colour_list = get_colour_list(download_folder, download_name, frame_folder)

  image_size = image_scale(len(colour_list), 2)

  print("writing image...")
  output_image = Image.new('RGB', (image_size, image_size), color = 'white')
  d = ImageDraw.Draw(output_image)

  for index, value in enumerate(colour_list):
    d.line((index,image_size, index, 0), fill=(int(value[0]),int(value[1]),int(value[2])))
  
  output_image = output_image.resize((1920,1080),resample=Image.BILINEAR)
  output_image.show()


if __name__ == "__main__": average_colours("https://www.youtube.com/watch?v=HRV6tMR-SSs")
