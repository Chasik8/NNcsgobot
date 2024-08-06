import numpy as np
import torch
import cv2
def Train(name):
    res = cv2.imread(name)
    img = cv2.resize(res, dsize=(300, 300), interpolation=cv2.INTER_CUBIC)
    # img = np.expand_dims(img, 0)
    img = img.astype(np.float32)
    img = torch.from_numpy(img)
    img = img.to('cuda:0')
    return img