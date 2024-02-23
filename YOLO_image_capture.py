import os
import cv2
import uuid

IMAGES_PATH = os.path.join('data', 'test_images')  # /data/images
labels = ['awake', 'drowsy']
number_imgs = 20


cap = cv2.VideoCapture(0)

# Loop through labels
for label in labels:
    print('Collecting images for {}'.format(label))
    input("Press Enter to start capturing...")
    
    # Loop through image range
    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))

        # Webcam feed
        ret, frame = cap.read()

        # Naming our image path
        imgname = os.path.join(IMAGES_PATH, label + '.' + str(uuid.uuid1()) + '.jpg')

        # Writes out image to file
        cv2.imwrite(imgname, frame)

        # Render to the screen
        cv2.imshow('Image Collection', frame)

        # Wait for the 'c' key to be pressed
        if img_num > 0:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('c'):
                continue
            elif key == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
