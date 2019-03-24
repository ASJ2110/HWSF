'''
Hey Guys! I did some research on facial recognition and was playing around with skimage when I found out about another library which not
only carries out the same functions, but more. It's called opencv (open computer vision) and I thought it would be a good idea to share it
with you all.

Below are some codes that I wrote after playing around with it for a bit. The codes aren't related to each other and are separated with a
noticeably large space.
I will include comments documenting what each part means as I go along:
'''


import cv2
import numpy as np
# opencv relies on numpy as it deals with the manipulation of arrays of pixels etc



# This code simply reads an image file and displays it on a window

img = cv2.imread('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Wallpapers\\green-Linux-circle-Kali-Linux-NetHunter-Kali-Linux-leaf-134515-wallhere.com.jpg', 0)
# imread reads a file. Parameters include the file name or a path to the file name; and an option to grayscale it, denoted with 0

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# namedWindow resizes the image to the window

cv2.imshow('image', img)
cv2.waitKey(0)
# waitKey is required in order for the image to actually display on the window

cv2.imwrite('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Wallpapers\\Kali.jpg', img)
# You can also save your edited image using imwrite. This is me saving a grayscaled edit of my original photo





# This code allows you stream a video live using a webcam

cap = cv2.VideoCapture(0)
# VideoCapture tells the webcam to start capturing whatever it sees

width = cap.get(3)
height = cap.get(4)
# variable.get(3) and (4) gives you the default resolution of your webcam

cap.set(3, 320)
cap.set(4, 240)
# You can then change the resolution (Note: you can only downgrade. If you want a better resolution, get a better camera)

print(width, height)
while True:
    ret, frame = cap.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) and 255 == ord('q'):
        break
# This while loop grayscaled the livestream

cap.release()
# release tells the webcam to stop capturing once the stream is over




# This code records and saves a video using a webcam or any other camera you connect to your pc

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# fourcc establishes the codec that will be used (a decoder used by media players). For windows, DIVX is the recommended one.

out = cv2.VideoWriter('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Coding\\Open CV\\test.avi', fourcc, 20.0, (640, 480))
# We need to establish the details of the recording process (name of file, the codec variable, frames per second, and finally resolution)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:     
        out.write(frame)       
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) and 255 == ord('q'):
            break
    else:
        break
# I don't fully understand what's going on here but I'm guessing it records each frame and compiles it into a video

cap.release()
out.release()
# Always remember to end any processes you've started, including the webcam and the recording




# This code opens a video file. I will be opening the .avi file that I saved in the code directly above

cap = cv2.VideoCapture('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Coding\\Open CV\\test.avi')
# Locates the file that the video will be capturing

while cap.isOpened():
    ret, frame = cap.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    cv2.imshow('frame', gray)
    if cv2.waitKey(50) and 255 == ord('q'):
        break
cap.release()
# Grayscales it (I love grayscaling)
# Note: Here, the waitKey is 50, as opposed to 1, or 0. This is because waitKey represents frames per second. This is currently a slow-mo




# You can crop parts of photos and paste them onto other parts of the image. I have yet to experiment with cross pasting between images
# I also suspect this to be one of the foundations of facial recognition (or just feature recognition in general)

img = cv2.imread('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Wallpapers\\minimalism-wood-tan-Fight-Club-Tyler-Durden-Project-Mayhem-37180-wallhere.com.jpg', 0)

durden = img[0:975, 65:640]
tyler = img[0:975, 65:640]
# As long as you know the location of your desired detail, you can specify it here

img[0:975, 650:1225] = durden
img[0:975, 1235:1810] = tyler
# This sets the location of where you want to paste it. If the ratios aren't maintained, it will raise an error.

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('C:\\Users\\bsoma\\OneDrive\\My Documents\\Aymane\\Wallpapers\\editedMayhem.jpg', img)


'''
I hope this contributes to our scope of learning. As far as I know, Open CV is used by the top firms and industries to make all sorts
of products from image/video editing software, CCTV, robotics, security, and any other industry that requires visual input.
It could be the next step after we master skimage!
I think you can make GUIs on here as well
'''


