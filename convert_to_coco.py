#this file is convert CTW dataset into coco
#the data strcutre is val_temp is list contains dict,which each elements in the list describe a image file
#each element in the list is a dict,which has a few keys:width,height, file_name id , annotations

import json
import codecs

file1 = 'val_temp.json'

file2 = 'cates2.json'

file3 = 'valsth.json'


dataset = {}

with open(file1) as f:
	data = json.load(f)

with open(file2) as f:
	cates = json.load(f)

#make the images for coco
images = []
for sth in data:
	temp = {}
	temp['width'] = sth['width']
	temp['height'] = sth['height']
	temp['file_name'] =sth['file_name']
	temp['id'] = sth['image_id']
	images.append(temp)

dataset['images'] = images


#make the categories for coco
cates_new = []
for sth in cates:
	temp ={}
	temp['id'] = sth['id']
	temp['name'] = sth ['name']
	cates_new.append(temp)
dataset['categories'] = cates_new


#make the anotations for coco
l3 = []
for sth in data:
	#print(type(sth))
	for sth2 in sth['annotations']:
		for sth3 in sth2:
			#print(sth3.keys())
			#print(type(sth3))
			if sth3['yao'] ==True:
				temp = {}
				temp['image_id'] = sth['image_id']
				temp['bbox'] = sth3['adjusted_bbox']
				temp['id'] = sth3['id']
				temp['category_id'] = sth3['category_id']
				l4 = []
				for nima in sth3['polygon']:
					for nima2 in nima:
						l4.append(nima2)
				temp['iscrowd'] = 0
				temp['ingore'] = 0
				temp['area'] = temp['bbox'][2]*temp['bbox'][3]  
				#l4.append(1)
				#l4.append(2)
				temp['segmentation'] =[]
                		temp['segmentation'].append(l4)
				l3.append(temp)

with codecs.open(file3, 'w', 'utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True)		



