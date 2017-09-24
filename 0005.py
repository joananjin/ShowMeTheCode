import os
import cv2

isExists = os.path.exists('./res_animals')
if not isExists:
    os.mkdir('./res_animals')

for filename in os.listdir(r"./animals"):
    if not filename.startswith('.'):
        img1 = cv2.imread(r"./animals/" + filename, 1)
        img1 = cv2.resize(img1, (640, 1136), interpolation=cv2.INTER_CUBIC)
        os.chdir("./res_animals")
        cv2.imwrite("resized"+filename, img1)
        os.chdir(os.path.pardir)
