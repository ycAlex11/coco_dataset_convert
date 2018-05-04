import cv2
import json
def reading():
    file2 = 'val_new.json'
    with open(file2) as f:
    	cates = json.load(f)
    return cates

dataset = reading()
#images_path = '/home/cat/result/'
images = {}
path = '/home/cat/result/'

#for sth in dataset['images']:
#	images[sth['id']] = sth['file_name']

for sth in dataset['annotations']:
	#file =path+str(images[sth['image_id']])+'.jpg'
	if sth['image_id']>=18 and sth['image_id']<=26: 
		img = cv2.imread(path+'0000488/'+str(sth['image_id'])+'.jpg')
		cv2.rectangle(img,(int(sth['bbox'][0]),int(sth['bbox'][1])),(int(sth['bbox'][0])+int(sth['bbox'][2]),int(sth['bbox'][1])+int(sth['bbox'][3])),(55,255,155),5)
		cv2.imwrite(path+'0000488/'+str(sth['image_id'])+'.jpg',img)
	
