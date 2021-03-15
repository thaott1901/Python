import cv2
import os


def length_of_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


def capture_frames(video_path, save_path, skip_frame):
    print("********** Entering extracting phase **********")
    _, file_name = os.path.split(video_path)
    file_name_wo_ext = os.path.splitext(file_name[0])
    length = length_of_video(video_path)
    if length == 0:
        print("Video length is 0, exiting extracting phase")
        return 0
    cap = cv2.VideoCapture(video_path)
    count = 0

    ret, frame = cap.read()
    name = './data/frame' + str(count) + '.jpg'
    test_file_path = os.path.join(save_path, name)

    cv2.imwrite(test_file_path, frame)
    if os.path.isfile(test_file_path):
        print("Saving test frame " + test_file_path + " successful!")
        count = 1
        while ret:
            ret, frame = cap.read()
            if ret and count % skip_frame == 0:
                cv2.imwrite(os.path.join(save_path, file_name_wo_ext[:6] + str(count) + ".jpg"), frame)
            count += 1
            print(count)
        else:
            count += 1
    else:
        print("Problem with saving test frame")
        return 0
    cap.release()
    print("********** Finished **********")

video_path = "E:/Tech/Projects/LeetCode/a.mp4"
save_path = "E:/Tech/Projects/LeetCode/Data"
capture_frames(video_path, save_path, 30)
