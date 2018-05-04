#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import codecs
filec = 'cates2.json'

#add the category to annotations in the train/val file
with open(filec) as f:
	cates = json.load(f)
text2cate = {c['name']: c['id'] for c in cates}
#dic = {}
#for key, value in text2cate.items():
#	dic[value] = key


#file = '/Users/yidouco.ltd.grey/Desktop/downloads/nima/downloads/val.jsonl'

#file2 = '/Users/yidouco.ltd.grey/Desktop/downloads/nima/downloads/val2.json'

#jsonl is a json file saved all data in lines
file = 'val.jsonl'
file2 = 'val_temp.json'
l = []
j =0

#add the category id and annotation id to each annotations
#add a new keys 'yao' which means its a chinese and needs work on those annotations 
with open(file1) as f:
    #anno = json.loads(f.readline())
    for line in f.read().splitlines():
        anno = json.loads(line.strip())
        length = len(anno['annotations'])
        for i in range(length):
                for sth in anno['annotations'][i]:
                 if(sth['is_chinese']==True):
                        temp = sth['text']
                        if(text2cate.has_key(temp)):
                                sth['category_id'] = text2cate[temp]
                                sth['id'] = j
                                j = j+1
                                sth['yao'] = True
                 else:
                        sth['id'] =j
                        j = j+1
                        sth['category_id'] = -1
                        sth['yao'] = False
                        #sth['category_id'] = 1
                        #sth.pop('text')

        l.append(anno)
    	#print(i)


#write to a temp file
#the data structure will keep the CTW's structure, you may skip this step and convert to coco directly! 
with codecs.open(file2, 'w', 'utf-8') as f:
    json.dump(l, f, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True)		

