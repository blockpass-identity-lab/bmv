"""
Block Mean Value Based Hashing, Method 1, is a robust hash function which:

 1) Grey scale and normalises image size; 
 2) Divides the image into non-overlapped blocks i; 
 3) Encrypts the indices of block sequences i (skipped in this implementation);
 4) Calculates the mean (Mi) of each block, based on pixel value, and obtain Median (Md) of calculated means.
 5) Normalize mean values into binary hash form: h(i) = 0 if Mi < Md or 1 if Mi >= Md. 

 The below implementation is based on Method 1 (note that the encryption step has been skipped) orginally described by:
 B. Yang, F. Gu and X. Niu, "Block Mean Value Based Image Perceptual Hashing," 2006 International Conference on Intelligent Information Hiding and Multimedia, 2006, pp. 167-172, doi: 10.1109/IIH-MSP.2006.265125.
"""

from image_slicer import slice
from PIL import Image
import statistics
from io import BytesIO
from scipy.spatial.distance import hamming

def bmv(image):
    """Computes hash of a image using Block Mean Value Based Hashing, Method 1. 
    Keyword arguments:
    image -- path and name of image
    """
    #1) Open image, normalise image size to 256 x 256 and convert to grey scale.
    original = Image.open(image).convert('L') #grey scale
    resized = original.resize((256, 256)) #normalise size to 256*256

    grey_scale_image = BytesIO()
    resized.save(grey_scale_image, format='png')

    #2) Divide the image into non-overlapped blocks. The value of 24 is arbitrarily chosen for now...
    sliced = slice(grey_scale_image, 24, save=False)

    #4) Calculate the mean (pixel value) of each block and obtain median of means; 
    means = []
    for i in sliced:
        pixel_values = list(i.image.getdata())
        means.append(statistics.mean(pixel_values))

    median = statistics.median(means)

    #5) Normalize mean value into binary hash form
    hash = []
    for m in means:
        if m < median:
            hash.append(0)
        else:
            hash.append(1)
    return(hash)

def isMatch(distance):
    """Determine if a match exists between two images based on computed hamming distance.
    Keyword arguments:
    distance -- computed hamming distance between two images
    """
    if distance <= 8: #If HD is less than or equal to 8, we consider it a match. 
        return True
    return False

if __name__ == "__main__":
    malicious = bmv('img/malicious.png') # "United States Next Generation Passport, design since 2021", Keesing Platform, Public Domain, https://platform.keesingtechnologies.com/introducing-the-u-s-next-generation-passport/
    modified1 = bmv('img/modified1.png') 
    modified2 = bmv('img/modified2.png')
    modified3 = bmv('img/modified3.png')
    benign = bmv('img/benign.png') # "Dutch passport specimen issued 9 March 2014", Rijksdienst voor Identiteitsgegevens (RvIG), licensed under CC0 1.0 Universal Public Domain Dedication, https://commons.wikimedia.org/wiki/File:Dutch_passport_specimen_issued_9_March_2014.jpg
    benign2 = bmv('img/benign2.jpg') # “Mr Bean passport”, Ben Deck, licensed under CC BY-NC-ND 2.0, https://www.flickr.com/photos/bendeck/2639210778

    hd1 = int(hamming(malicious, modified1) * len(malicious))
    hd2 = int(hamming(malicious, modified2) * len(malicious))
    hd3 = int(hamming(malicious, modified3) * len(malicious))
    hd4 = int(hamming(malicious, benign) * len(malicious))
    hd5 = int(hamming(malicious, benign2) * len(malicious))

    print("=============================================================================================================================")
    print("malicious.png binary hash: {0};".format(malicious))
    print("=============================================================================================================================")
    print("modified1.png binary hash: {0}; hd: {1};  match: {2}".format(modified1, hd1, isMatch(hd1)))
    print("modified2.png binary hash: {0}; hd: {1};  match: {2}".format(modified2, hd2, isMatch(hd2)))
    print("modified3.png binary hash: {0}; hd: {1};  match: {2}".format(modified3, hd3, isMatch(hd3)))
    print("benign.png binary hash:    {0}; hd: {1}; match: {2}".format(benign, hd4, isMatch(hd4)))
    print("benign2.jpg binary hash:   {0}; hd: {1}; match: {2}".format(benign2, hd5, isMatch(hd5)))
