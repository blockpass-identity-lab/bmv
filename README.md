# bmv

Block Mean Value Based Hashing, Method 1, is a robust hash function which:
 1) Grey scale and normalises image size; 
 2) Divides the image into non-overlapped blocks i; 
 3) Encrypts the indices of block sequences i (skipped in this implementation);
 4) Calculates the mean (Mi) of each block, based on pixel value, and obtain Median (Md) of calculated means.
 5) Normalize mean values into binary hash form: h(i) = 0 if Mi < Md or 1 if Mi >= Md. 
 
 The implementation is based on Method 1 (note that the encryption step has been skipped) orginally described by:
 
B. Yang, F. Gu and X. Niu, "Block Mean Value Based Image Perceptual Hashing," 2006 International Conference on Intelligent Information Hiding and Multimedia, 2006, pp. 167-172, doi: 10.1109/IIH-MSP.2006.265125.

# Usage
Run the following commands in your Python (3.x) environment:

```
git clone https://github.com/blockpass-identity-lab/bmv
pip install -r requirements.txt
python bmv.py
```

Example output:
```
=============================================================================================================================
malicious.png binary hash: [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0];
=============================================================================================================================
modified1.png binary hash: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]; hd: 2;  match: True
modified2.png binary hash: [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]; hd: 0;  match: True
modified3.png binary hash: [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]; hd: 0;  match: True
benign.png binary hash:    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]; hd: 18; match: False
benign2.jpg binary hash:   [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]; hd: 16; match: False
```

Table of images and results:

| Name          | Image (resized to 128x128)                                                | Hamming Distance | Match |
|---------------|---------------------------------------------------------------------------|------------------|-------|
| malicious.png | <img src="img/malicious.png" alt="malicious.png" title="malicious.png" width="128" height="128" /> |  |  |
|               |                                                                           |                  |       |
| modified1.png | <img src="img/modified1.png" alt="modified1.png" title="modified1.png" width="128" height="128" /> | 2 | True |
| modified2.png | <img src="img/modified2.png" alt="modified2.png" title="modified2.png" width="128" height="128" /> | 0 | True |
| modified3.png | <img src="img/modified3.png" alt="modified3.png" title="modified3.png" width="128" height="128" /> | 0 | True |
| benign.png | <img src="img/benign.png" alt="benign.png" title="benign.png" width="128" height="128" /> | 18 | False |
| benign2.jpg | <img src="img/benign2.jpg" alt="benign2.jpg" title="benign2.jpg" width="128" height="128" /> | 16 | False |
