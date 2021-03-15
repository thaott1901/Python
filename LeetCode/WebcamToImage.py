import cv2
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np


def predict(image):
    test_predictions = np.argmax(model.predict(np.array([image]), verbose=1), axis=1)
    print(test_predictions)
    # print(dict[test_predictions[0]])


def webcam_to_images(name, skip_frame):
    # using webcam
    cap = cv2.VideoCapture(0)
    # width, id = 3
    # cap.set(3, 640)
    # height, id = 4
    # cap.set(4, 640)
    # brightness, id = 10
    cap.set(10, 100)

    folder_path = 'data' + "/" + name
    name_path = folder_path + "/" + name
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except OSError:
        print('Error: Creating directory of data')

    curr_frame = 0
    # Capture frame-by-frame
    ret, frame = cap.read()
    count = 0
    while ret:
        ret, frame = cap.read()
        if ret and curr_frame % skip_frame == 0:
            name = './' + name_path + str(count) + '.jpg'
            print('Creating...' + name)
            width = 54
            height = 54
            dim = (width, height)
            cropped = frame[80:560, 0:480]
            resized = cv2.resize(cropped, dim, interpolation=cv2.INTER_AREA)
            predict(resized)
            cv2.imshow("Video", cropped)
            # cv2.imwrite(name, resized)
            count += 1
        # To stop duplicate images
        curr_frame += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


model = load_model("models/cnn5426_87.h5")
dict = ["A", "B", "C", "D", "Del", "E", "F", "G" , "H", "I", "J", "K", "L", "M", "N", "Nothing" "O",
        "P", "Q", "R", "S", "Space", "T" , "U", "V", "W", "X", "Y", "Z"]

name = "Test"
skip = 5
webcam_to_images(name, skip)
