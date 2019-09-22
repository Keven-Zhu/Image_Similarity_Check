# Image_Similarity_Check
A program that calculates the similarity of two images using perceptual image hashing and hamming distance. Written in Python 3.7

## Getting Started
Install imagehash, distance, and PIL python packages

```python
pip install imagehash
pip install distance
pip install Pillow
```

## Running the program
To run this program, first add the paths to the images into the input.csv file. Then simply run 

```python
python main.py
```
in the project folder.

## Design Details
Perceptual image hashing, or just image hashing, is a a process that takes in the contents of an image and generates a unique id for the picture. More specifically, the hashing algorithm used here is the "difference hash" algorithm which looks at the difference between adjacent pixel values. What makes this hashing algorithm different than more standard ones like sha-1 or md5 is that a small change in the input file will result in extremely different hashes using sha-1 or md5. So, using the difference hash algorithm, similar images will then have very similar hashes. 

Once we hav obtained the hash, we can then calculate the hamming distance. The hamming distance calculates the minimum number of substitutions required to change one string to the other. 

ab**cd**e and ab**fg**e would have a hamming distance of **2**.

With the hamming distance, the similarity between two images can be calculated.
