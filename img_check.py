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
    '''check that whether the img is broken or not'''
    wrong_img = []
    for im in imglist:
        name = imgdir + im
        img = cv2.imread(name)
        if img is None:
            wrong_img.append(im)
    print(wrong_img)
    return wrong_img

def data_check2(imglist,imgdir):
    '''check that whether the shape is H*W*n'''
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

def data_check3(imglist,imgdir):
    '''check the channel is 3 or not, if the channel is 4, then rewrite the img.'''
    wrong_img = []
    num = 0
    for im in imglist:
        num += 1
        if num % 1000 == 0:
            print('rest:',len(imglist)-num)
            
        name = imgdir + im
        img = cv2.imread(name)
        
        if img.shape[2] != 3:
            print('img.shape:',img.shape)
            if img.shape[2] == 4:
                img2 = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
                cv2.imwrite(name,img2)
            print(im)
            wrong_img.append(im)
    print(wrong_img)
    return wrong_img

def img_rewrite(imglist,imgdir):
    num = 0
    for im in imglist:
        num += 1
        if num % 1000 == 0:
            print('rest:',len(imglist)-num)
        if im.split('.')[1] != 'jpg':
            print(im)
            name = imgdir + im
            savename = imgdir + im.split('.')[0] + '.jpg'
            img = cv2.imread(name)
            cv2.imwrite(savename,img)
    return

    

gt_check(imglist,gtdir)
data_check1(imglist,imgdir)
data_check2(imglist,imgdir)



