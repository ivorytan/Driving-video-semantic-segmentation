import numpy as np
import os
import cv2

# 获取图片的尺寸
img_dir = r'DeepLabV3Plus-Pytorch/test_results'

file_names = os.listdir(img_dir)
file_names.sort(key=lambda x:int(x[:-4]))

img_size = (1920, 1080)

videowrite = cv2.VideoWriter(r'test_result.mp4',-1,30,img_size)

for i in file_names:
    path = os.path.join(img_dir, i)
    if os.path.isfile(path):
        if os.path.splitext(path)[1] == '.png':
            # 进行图片读取及视频写入
            # img_paths.append(path)
            img = cv2.imread(path)
            if img is None:
                print(path + " is error!")
                continue
            videowrite.write(img)

videowrite.release()
print("The video is ready!")
