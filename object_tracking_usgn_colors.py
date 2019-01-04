import cv2
import numpy as np

def main():
    cam = cv2.VideoCapture(0)
    window = 'Original'
    filename = 'Original.avi'
    filename_b = 'Blue.avi'
    filename_g = 'Green.avi'
    filename_r = 'Red.avi'
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 24
    resolution = (640,480)
    video_orginal = cv2.VideoWriter(filename, codec, framerate, resolution)
    video_blue = cv2.VideoWriter(filename_b, codec, framerate, resolution)
    video_green = cv2.VideoWriter(filename_g, codec, framerate, resolution)
    video_red = cv2.VideoWriter(filename_r, codec, framerate, resolution)
    if cam.isOpened():
        ret, frame = cam.read()
        print(ret)
    else:
        ret = False
        print(ret)
        #break
    while ret:
        ret, frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #tracking of blue color
        low = np.array([100, 50, 50])
        high = np.array([140, 255, 255])

        #tracking of green color
        low_green = np.array([40, 50, 50])
        high_green = np.array([80, 255, 255]) 

        #tracking of red color
        low_red = np.array([140, 150, 0])
        high_red = np.array([180, 255, 255]) 

        #binary matrix
        image_mask = cv2.inRange(hsv, low, high)
        image_mask_green = cv2.inRange(hsv, low_green, high_green)
        image_mask_red = cv2.inRange(hsv, low_red, high_red)

        #display image_mask
        #cv2.imshow('image mask', image_mask)

        #output after and operation
        output_blue = cv2.bitwise_and(frame, frame, mask = image_mask)
        output_green = cv2.bitwise_and(frame, frame, mask = image_mask_green)
        output_red = cv2.bitwise_and(frame, frame, mask = image_mask_red)

        #display the output
        cv2.imshow('Output_blue', output_blue)
        cv2.imshow('Output_green', output_green)
        cv2.imshow('Output_red', output_red)
        cv2.imshow(window, frame)

        #save videos
        video_orginal.write(frame)
        video_blue.write(output_blue)
        video_green.write(output_green)
        video_red.write(output_red)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cam.release()

if __name__ == '__main__':
    main()