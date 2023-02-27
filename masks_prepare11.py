import os
import sys
import numpy as np
from PIL import Image
from zipfile import ZipFile
from natsort import natsorted
#script_dir=os.path.abspath(os.path.dirname(sys.argv[0]))
#default_path=script_dir+'/data/Segmentation/teeth_mask'

def convert_one_channel(img):
    #some images have 3 channels , although they are grayscale image
    if len(img.shape)>2:
        img=img[:,:,0]
        return img
    else:
        return img
'''def pre_masks(resize_shape=(512,512),path=default_path):
    #ZipFile(path+"/Orig_Masks.zip").extractall(path+'/Masks/') 
    #path=path+'/Masks/'
    dirs=natsorted(os.listdir(path))
    masks=img=Image.open(path+dirs[0])
    masks=(masks.resize((resize_shape),Image.ANTIALIAS))
    masks=convert_one_channel(np.asarray(masks))
    for i in range (1,len(dirs)):
        img=Image.open(path+dirs[i])
        img=img.resize((resize_shape),Image.ANTIALIAS)
        img=convert_one_channel(np.asarray(img))
        masks=np.concatenate((masks,img))
    masks=np.reshape(masks,(len(dirs),resize_shape[0],resize_shape[1],1))
    return masks'''


#default_path=script_dir+'/data/'


#CustomMasks 512x512
#default_path="D:/VIII_sem_project/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net/data/Segmentation/teeth_mask"
def pre_splitted_masks(path1):
    #ZipFile(path+"/splitted_masks.zip").extractall(path+'/Masks/') 
    dirs=natsorted(os.listdir(path1))
    masks=img=Image.open(path1+dirs[0])
    masks=convert_one_channel(np.asarray(masks))
    for i in range (1,len(dirs)):
        img=Image.open(path1+dirs[i])
        img=convert_one_channel(np.asarray(img))
        masks=np.concatenate((masks,img))
    masks=np.reshape(masks,(len(dirs),512,512,1))
    return masks
    




    
