import torch
import numpy as np
import cv2
from time import time
import torch
from ultralytics import YOLO
from mss import mss
from PIL import Image, ImageOps, ImageGrab
import time
# import pyscreenshot as ImageGrab
# import pytesseract
import pyautogui
# import mouse
from pynput.mouse import Button, Controller


def run():
    # mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    # sct = mss()
    model = YOLO("D:\\Project\\Python\\Neroset_cs1\\runs\\detect\\yolov8n4\\weights\\best.pt")
    # model.val()
    model.to('cuda:0')
    # mouse = Controller()
    kef = 1920 // 640
    while 1:
        # last_time = time.time()
        # img = sct.grab(mon)
        img = ImageGrab.grab()
        # img = img.resize((640, int(640 / 1920 * 1080)))
        # img.show()
        # img=ImageOps.fit(img, (640, 640), method=Image.ANTIALIAS)
        results = model.predict(source=img)
        res = results[0].to("cpu")
        # results = model.predict(img, stream=True)
        # results = torch.tensor(results).to("cpu")
        for box in res.boxes:
            b = box.xyxy.numpy()
            # mouse.move(b[0][0]*1920 / 640-mouse.position[0], b[0][1]*1920 / 640-mouse.position[1])
            # time.sleep(1)
            # mouse.move(b[0][0], b[0][1], absolute=False, duration=0.2)
            x = b[0][0] - 1920 // 2
            y = b[0][1] - 1080 // 2
            # m1=pyautogui.position()
            # time.sleep(5)
            pyautogui.move(x, y, 0.5)
            time.sleep(2)
            # time.sleep(1)
            # pyautogui.click(b[0][0], b[0][1])
            # m2=pyautogui.position()
            # print("Yes")
            # img = cv2.rectangle(np.array(img), (b[0][0], b[0][1], b[0][1], b[0][1]), (255, 0, 0), 2)
            break
        # Boxes object for bbox outputs
        # masks = results[0].masks  # Masks object for segmenation masks outputs
        # probs = results[0].probs
        # print('fps: {0}'.format(1 / (time.time() - last_time)))
        # cv2.imshow('screen', np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    run()
