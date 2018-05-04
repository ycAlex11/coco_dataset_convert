#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import cv2

num_img = 0;

def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print path+'---creating folder'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+'--the folder is existed'
        return False

def reading():
    file2 = '/home/cat/ceshi/valsth.json'
    with open(file2) as f:
    	cates = json.load(f)
    return cates

def moving(l,chose,segmentation):
    l_new=[]
    seg = segmentation[0]
    seg_new =[]
    temp = []
    if chose == 1:
        l_new = l
        seg_new.append(seg)
    elif chose == 2:
        l_new.append(l[0]-624)
        l_new.append(l[1])
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-624) 
        temp.append(seg[1])
        temp.append(seg[2]-624) 
        temp.append(seg[3])
        temp.append(seg[4]-624) 
        temp.append(seg[5])
        temp.append(seg[6]-624) 
        temp.append(seg[7])
        seg_new.append(temp)
    elif chose==3:
        l_new.append(l[0]-1248)
        l_new.append(l[1])
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-1248) 
        temp.append(seg[1])
        temp.append(seg[2]-1248) 
        temp.append(seg[3])
        temp.append(seg[4]-1248) 
        temp.append(seg[5])
        temp.append(seg[6]-1248) 
        temp.append(seg[7])
        seg_new.append(temp)
    elif chose==4:
        l_new.append(l[0])
        l_new.append(l[1]-624)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]) 
        temp.append(seg[1]-624)
        temp.append(seg[2]) 
        temp.append(seg[3]-624)
        temp.append(seg[4]) 
        temp.append(seg[5]-624)
        temp.append(seg[6]) 
        temp.append(seg[7]-624)
        seg_new.append(temp)
    elif chose == 5:
        l_new.append(l[0]-624)
        l_new.append(l[1]-624)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-624) 
        temp.append(seg[1]-624)
        temp.append(seg[2]-624) 
        temp.append(seg[3]-624)
        temp.append(seg[4]-624) 
        temp.append(seg[5]-624)
        temp.append(seg[6]-624) 
        temp.append(seg[7]-624)
        seg_new.append(temp)
    elif chose ==6:
        l_new.append(l[0]-1248)
        l_new.append(l[1]-624)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-1248) 
        temp.append(seg[1]-624)
        temp.append(seg[2]-1248) 
        temp.append(seg[3]-624)
        temp.append(seg[4]-1248) 
        temp.append(seg[5]-624)
        temp.append(seg[6]-1248) 
        temp.append(seg[7]-624)
        seg_new.append(temp)
    elif chose ==7:
        l_new.append(l[0])
        l_new.append(l[1]-1248)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]) 
        temp.append(seg[1]-1248)
        temp.append(seg[2]) 
        temp.append(seg[3]-1248)
        temp.append(seg[4]) 
        temp.append(seg[5]-1248)
        temp.append(seg[6]) 
        temp.append(seg[7]-1248)
        seg_new.append(temp)
    elif chose ==8:
        l_new.append(l[0]-624)
        l_new.append(l[1]-1248)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-624) 
        temp.append(seg[1]-1248)
        temp.append(seg[2]-624) 
        temp.append(seg[3]-1248)
        temp.append(seg[4]-624) 
        temp.append(seg[5]-1248)
        temp.append(seg[6]-624) 
        temp.append(seg[7]-1248)
        seg_new.append(temp)
    else:
        l_new.append(l[0]-1248)
        l_new.append(l[1]-1248)
        l_new.append(l[2])
        l_new.append(l[3])
        temp.append(seg[0]-1248) 
        temp.append(seg[1]-1248)
        temp.append(seg[2]-1248) 
        temp.append(seg[3]-1248)
        temp.append(seg[4]-1248) 
        temp.append(seg[5]-1248)
        temp.append(seg[6]-1248) 
        temp.append(seg[7]-1248)
        seg_new.append(temp)
    return l_new,seg_new

def get_anno(i,sth,anno_id,annos,l):
    anno_temp = {}
    bbox_result,seg_result = moving(sth['bbox'],i,sth['segmentation'])
    anno_temp['bbox'] = bbox_result
    anno_temp['segmentation'] = seg_result
    anno_temp['iscrowd'] = sth['iscrowd']
    anno_temp['area'] =sth['area']
    anno_temp['image_id'] = l[i-1]
    anno_temp['id'] = anno_id
    anno_id = anno_id + 1
    anno_temp['category_id'] = sth['category_id']
    annos.append(anno_temp)
    return anno_id

dataset ={}
anno_id =0
new_imgs=[]
anno_new = []
write_path = '/mnt/cfs/data/CTW800/val/'
data = reading()
count =0
checking = {}
img_new = 0
#path = '/mnt/cfs/data/CTW800/val/'

for sth in data['annotations']:
 #if count<10:
    if checking.has_key(sth['image_id'])==False:
       
       img = cv2.imread('/mnt/cfs/data/CTW/images-trainval/'+sth['image_id']+'.jpg')
       img1 = img[0:800,0:800]
       img2 = img[0:800,624:1424]
       img3 = img[0:800,1248:2048]
       img4 = img[624:1424,0:800]
       img5 = img[624:1424,624:1424]
       img6 = img[624:1424,1248:2048]
       img7 = img[1248:2048,0:800]
       img8 = img[1248:2048,624:1424]
       img9 = img[1248:2048,1248:2048]
       crop_images = []
       path = write_path+str(sth['image_id'])+'/'
       mkdir(path)
       path2 = str(sth['image_id'])+'/'
       #cv2.rectangle(img,(int(sth['bbox'][0]),int(sth['bbox'][1])),(int(sth['bbox'][0])+int(sth['bbox'][2]),int(sth['bbox'][1])+int(sth['bbox'][3])),(55,255,155),5)
       #cv2.imwrite(path+str(sth['image_id'])+'.jpg',img)

       cv2.imwrite(path+str(img_new)+'.jpg',img1)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img2)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img3)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img4)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1
       
       cv2.imwrite(path+str(img_new)+'.jpg',img5)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img6)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img7)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img8)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       cv2.imwrite(path+str(img_new)+'.jpg',img9)
       img_temp = {}
       crop_images.append(img_new)
       img_temp['width'] = 800
       img_temp['height'] = 800
       #img_temp['file_name'] = str(img_new)+'.jpg'
       img_temp['file_name'] = path2+str(img_new)+'.jpg'
       img_temp['id'] = img_new
       new_imgs.append(img_temp)
       img_new = img_new + 1

       checking[sth['image_id']] = crop_images
       if sth['bbox'][0]<800 and sth['bbox'][1]<800:
            #anno_temp,anno_id = get_anno(1,sth,anno_id)
            anno_id=get_anno(1,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]<800 and sth['bbox'][0]>=624:
            anno_id=get_anno(2,sth,anno_id,anno_new,crop_images)

       if  sth['bbox'][1]<800 and sth['bbox'][0]>=1248:
            anno_id=get_anno(3,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<800 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624:
            anno_id=get_anno(4,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624 and sth['bbox'][0]>=624:
            anno_id=get_anno(5,sth,anno_id,anno_new,crop_images)   
        
       if sth['bbox'][0]>=1248 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624:
            anno_id=get_anno(6,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<800 and sth['bbox'][1]>=1248:
            anno_id=get_anno(7,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]>=624 and sth['bbox'][1]>=1248:
            anno_id=get_anno(8,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]>=1248 and sth['bbox'][1]>=1248:
            anno_id=get_anno(9,sth,anno_id,anno_new,crop_images) 
                   
       count = count +1     

    else:
       #img = cv2.imread('/home/cat/result/'+str(sth['image_id'])+'/'+str(sth['image_id'])+'.jpg')
       #cv2.rectangle(img,(int(sth['bbox'][0]),int(sth['bbox'][1])),(int(sth['bbox'][0])+int(sth['bbox'][2]),int(sth['bbox'][1])+int(sth['bbox'][3])),(55,255,155),5)
       #cv2.imwrite('/home/cat/result/'+str(sth['image_id'])+'/'+str(sth['image_id'])+'.jpg',img)
       crop_images = checking[sth['image_id']]
       if sth['bbox'][0]<800 and sth['bbox'][1]<800:
            #anno_temp,anno_id = get_anno(1,sth,anno_id)
            anno_id=get_anno(1,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]<800 and sth['bbox'][0]>=624:
            anno_id=get_anno(2,sth,anno_id,anno_new,crop_images)

       if  sth['bbox'][1]<800 and sth['bbox'][0]>=1248:
            anno_id=get_anno(3,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<800 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624:
            anno_id=get_anno(4,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624 and sth['bbox'][0]>=624:
            anno_id=get_anno(5,sth,anno_id,anno_new,crop_images)   
        
       if sth['bbox'][0]>1248 and sth['bbox'][1]<1424 and sth['bbox'][1]>=624:
            anno_id=get_anno(6,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<800 and sth['bbox'][1]>=1248:
            anno_id=get_anno(7,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]<1424 and sth['bbox'][1]>=624 and sth['bbox'][1]>=1248:
            anno_id=get_anno(8,sth,anno_id,anno_new,crop_images)

       if sth['bbox'][0]>=1248 and sth['bbox'][1]>=1248:
            anno_id=get_anno(9,sth,anno_id,anno_new,crop_images) 

dataset['images'] = new_imgs
dataset['annotations'] = anno_new
dataset['categories'] =data['categories']

file3 ='/mnt/cfs/data/CTW800/val_new.json' 

with open(file3,"w") as f:
    json.dump(dataset,f)
