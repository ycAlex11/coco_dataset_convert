# coco_dataset_convert
this is a simple expamle for covert CTW dataset to coco dataset. For CTW dataset please check this link:https://ctwdataset.github.io/tutorial/1-basics.html
Coco dataset is a dict contains a few keys : information, images,annotations , categories, license and so on

To make your own dataset, all you need is images, annotations and categories.

Step one: create a dict contains 3 keys: images, annotations and categories, each key's value is a list

Step two: images, as i mentationed the values is a list, each element in the list is a dict which needs a few keys:
          height, width,file_name,id
Step three: annotations, anntotaions' value is also list contains dict, each dict needs such keys: area:float, iscrowd: 0 or 1, image_id:int(Corresponding to images' id),bbox: list(minx,miny,w,h) , category_id: int, id: int(unique） , segmentation：list contains list.  After I have viewed coco api's code,the segmentations must contains at least 6 value in the list of list.otherwise Mask_RCNN would not count this annotations

Step four: categories, this one is pretty easy, list contains dict, each one contains two keys, id:int ; name:w/e

add_cate.py: change jsonl to json and add categories to json file

convert_to_coco.py: convert CTW to coco 

crop_image_coco.py: separate a group of 2048*2048 images to 800*800 images

So if you just want understand coco's json file, just need view the crop_image_coco.py


          
