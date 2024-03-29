import imagehash
import distance
import time
from PIL import Image
import csv

img1 = []
img1_path = []
img2 = []
img2_path = []
similarity = []
time_elapsed = []

print("Loading images...")

#reads in the image paths from the csv
with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            img1_path.append(row[0])
            img2_path.append(row[1])

            #loads in and stores the images
            img1.append(Image.open(row[0]))
            img2.append(Image.open(row[1]))
        line_count += 1

print("Images loaded")

print("Calculating similarities...")
for x in range(len(img1)):

    #starts the timer for the calculation
    time_start = int(round(time.time() * 1000))

    #calculates the hash for the pair of images
    hash1 = str(imagehash.dhash(img1[x]))
    hash2 = str(imagehash.dhash(img2[x]))

    #calculates the hamming distance of the two hashes
    similarity.append((distance.hamming(hash1, hash2)) / len(hash1))

    #ends the timer and records the time taken for the hashing function to run
    time_end = int(round(time.time() * 1000))
    time_elapsed.append(time_end - time_start)

print("Done calculations")

print("Writing to CSV file")

#Writes to the csv file
with open("output.csv", mode="w") as output_file:
    writer = csv.writer(output_file, delimiter=",")

    writer.writerow(["image1", "image2", "similarity", "time elapsed(in milliseconds)"])
    
    for x in range(len(img1)):
        writer.writerow([img1_path[x], img2_path[x], similarity[x], time_elapsed[x]])

print("Done writing")