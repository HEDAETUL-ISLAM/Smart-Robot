# Smart-Robot

This project was done by

######  [Faisal Abdullah](https://www.facebook.com/faisalkhanfossil)
######  [Fokrul Islam Bhuiyan](https://www.facebook.com/fokrulbhuiyan01)
######  [Hedaetul Islam](https://hedaetul-islam.github.io/)

We all know the Raspberry Pi is a wonderful developing platform with its high computational power and development options it can work out wonders in hands of electronics hobbyists or students. So, we supposed to build an image-processing robot using Raspberry Pi. This robot is capable of travel one point to another point. What the robot do is that it clicks picture of a view from upper and detects all the obstacles in the picture and also calculate the distance of objects from one to another. Then the robot can travel given source to destination by following the shortest path. But we could not reach that  much. In the project, we build an image-processing line follower robot and try to add shortest path functionality. We used the Pi Camera to capture a video stream and applied computer vision algorithms to follow the line. Using camera has some big advantages over sensors like sensor follow the line using edge detection rather than grayscale thresholding which is virtually immune for shadows and grey zones in the image.  The robot will work in such a way that first it will capture the frame then it will define the ROI(region of interest) after that identify all of the black regions in this ROI(region of interest) and accordingly will follow the line. 
