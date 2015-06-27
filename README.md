# xbox360kinectLiveStreaming using Python

This code grabs the frames from the kinect RGB camera using the openkinect library, creates a jpeg picture and then streams the video with mjpeg codec.

## Prequisites
1. Have ffmpeg installed on the server.
2. Have freenect, opencv installed.

##Limitations
1. No audio, since using only mjpeg codec.
