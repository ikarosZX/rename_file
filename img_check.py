import os
import cv2

imgdir = './train_img/'
gtdir = './train_gt/'
imglist = os.listdir(imgdir)

def gt_check(imglist,gtdir):
    wrong_img = []
    for im in imglist:
        a = im.split('.')[0]
        gtname = gtdir + a + '.txt'
        if not os.path.exists(gtname):
            wrong_img.append(im)
  
    print(wrong_img)
    return wrong_img

def data_check1(imglist,imgdir):
    wrong_img = []
    for im in imglist:
        name = imgdir + im
        img = cv2.imread(name)
        if img is None:
            wrong_img.append(im)
    print(wrong_img)
    return wrong_img

def data_check2(imglist,imgdir):
    wrong_img = []
    num = 0
    for im in imglist:
        num += 1
        if num % 1000 == 0:
            print('rest:',len(imglist)-num)
        name = imgdir + im
        img = cv2.imread(name)
        if len(img.shape) != 3:
            wrong_img.append(im)
    print(wrong_img)
    return wrong_img


gt_check(imglist,gtdir)
data_check1(imglist,imgdir)
data_check2(imglist,imgdir)



