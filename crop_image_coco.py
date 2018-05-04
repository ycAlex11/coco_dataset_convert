#!/usr/bin/python
# -*- coding: utf-8 -*-
#this is a simple code to separate a image(2048*2048) into 9 images in a group of images 
#And re-write the josn file as coco dataset for all cropping images

import json
import cv2


num_img = 0;

#a simple function to create folder 
def mkdir(path):
    import os

    path=path.strip()

    path=path.rstrip("\\")
 

    isExists=os.path.exists(path)

    if not isExists:
        os.makedirs(path) 
 
        print path+'---creating folder'
        return True
    else:
        print path+'--the folder is existed'
        return False

#reading the original coco dataset's json file
def reading():
    file2 = '/home/cat/ceshi/val1.json'
    with open(file2) as f:
    	cates = json.load(f)
    return cates

#move the bbox and segmentation to right position in cropping image
def moving(l,chose,segmentation):
    l_new=[]
    seg = segmentation[0]
    seg_new =[]
    temp = []
    if chose == 1:
        l_new = l
        seg_new.add(seg)
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

#write a new annotations for the cropping image
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
write_path = '/mnt/cfs/data/CTW800/train/'

#the data in original coco dataset's joson file
data = reading()
count =0

#the key is original image name, the value is a list which contains its all cropping images' name
checking = {}

img_new = 0

#go through all annotations
for sth in data['annotations']:
 #if count<10:
    #this if part is separate image when the image appears first time ,because one image may have a few of annotations
    #so for one image we only want crop it into 9 cropping image once  
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
       #make folder for each image's cropping images
       path = write_path+str(sth['image_id'])+'/'
       mkdir(path)
       path2 = str(sth['image_id'])+'/'
       #cv2.rectangle(img,(int(sth['bbox'][0]),int(sth['bbox'][1])),(int(sth['bbox'][0])+int(sth['bbox'][2]),int(sth['bbox'][1])+int(sth['bbox'][3])),(55,255,155),5)
       #cv2.imwrite(path+str(sth['image_id'])+'.jpg',img)

       #separate each image into 9 parts
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

       #check each case to move the bbox and segmentation
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
                   
       count = count +1     

    else:
       #img = cv2.imread('/home/cat/result/'+str(sth['image_id'])+'/'+str(sth['image_id'])+'.jpg')
       #cv2.rectangle(img,(int(sth['bbox'][0]),int(sth['bbox'][1])),(int(sth['bbox'][0])+int(sth['bbox'][2]),int(sth['bbox'][1])+int(sth['bbox'][3])),(55,255,155),5)
       #cv2.imwrite('/home/cat/result/'+str(sth['image_id'])+'/'+str(sth['image_id'])+'.jpg',img)

       #if the images has already separated , find the corresponding cropping image
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

#write the new json file
file3 ='/mnt/cfs/data/CTW800/val_new.json' 

with open(file3,"w") as f:
    json.dump(dataset,f)
