import freenect
import cv2
import numpy as np
from PIL import Image
from subprocess import Popen, PIPE

#function to get video frames 
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

 
if __name__ == "__main__":
    
    im = Image.new( "RGB", (480,640))
    p = Popen(['ffmpeg', '-y', '-f', 'image2pipe','-vcodec', 'mjpeg', '-i', '-', '-qscale', '5','-vcodec', 'mpeg4','-b:v','5','-r','10',  'http://127.0.0.1:8090/feed1.ffm'], stdin=PIPE)
    while True:   
       frame = get_video()
       im = Image.fromarray(frame)
       im.save(p.stdin, 'JPEG')
    p.stdin.close()
    p.wait()
    

