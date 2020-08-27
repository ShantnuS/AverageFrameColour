# AverageFrameColour
Creates an image of average frame colours for a YouTube video. 

An example image is shown below, for the movie trailer for [Us 2019](https://www.youtube.com/watch?v=hNCmb-4oXJA): 
<img src="docs\assets\images\us_trailer.png" alt="Simply Easy Learning" width="50%">

## Install

You need Python 3 installed to run this.   

The first step is to clone the repository: 
```
git clone https://github.com/ShantnuS/AverageFrameColour.git   
```

Next a number of Python libraries need to be installed using pip:
```
pip install pytube3
pip install opencv-python
pip install pillow 
```
You are now ready to run. 

## Usage

To run the script, copy the URL of a YouTube video. Ideally this video should be short (5 mins max). 
```
python3 average-colours.py
```
The script will ask you to paste in the video URL, i.e.:
```
Enter a YouTube video URL: https://www.youtube.com/watch?v=hNCmb-4oXJA
```

Now just wait until the image is saved in the script folder (as a PNG) and an output image is displayed. 

## Contributing

Feel free to fork, mirror, etc. 

## License
MIT (basically just do whatever I'm not involved)

