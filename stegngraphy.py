from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def randPix():
    return (np.random.randint(255),np.random.randint(255),np.random.randint(255))

def steg(M,O):
    temp = []
    for i in range(3):
        temp.append((M[i]&252)|(O[i]>>6))
    return tuple(temp)

org = Image.open('org.jpg')
Org = org.load()
plt.title("Original image")
plt.imshow(org)
plt.show()

im = Image.new("RGB",(org.size[0]*2,org.size[1]*2),"white")
Map = im.load()

for i in range(org.size[0]):
    for j in range(org.size[1]):
        Map[i*2,j*2]=randPix()
        Map[i*2,j*2]=steg(Map[i,j],Org[i,j])
        
plt.title("Stegmentized image")
a = plt.imshow(im)
plt.show()

rec = Image.new("RGB",(int(im.size[0]/2),int(im.size[1]/2)),"white")
Rec = rec.load()

for i in range(rec.size[0]):
    for j in range(rec.size[1]):
        temp = []
        for k in range(3):
            temp.append((Map[i*2,j*2][k]&3)<<6)
        Rec[i,j]=tuple(temp)

plt.title("Recovered image")
a = plt.imshow(rec)
plt.show()