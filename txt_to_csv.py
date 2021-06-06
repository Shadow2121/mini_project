from importlib.abc import PathEntryFinder
from os import name
from sys import path_importer_cache
from PIL import Image


import numpy as np
import csv

f1 = open('wider_face_train.txt', 'r')

line_count = 0
for line in f1:
    if line != "\n":
        line_count += 1
print(line_count)

f1.close()

f1 = open('wider_face_train.txt', 'r')
f2 = open('wider_face_train.csv', 'w')
writer = csv.writer(f2)

for i in range(line_count):
    temp = f1.readline()

    s1 = temp.split()
    img_name = s1[0].split("/")[-1]
    ti = Image.open(img_name)
    w, h = ti.size
    print(img_name)
    num = s1[1]
    remaining = s1[2:]

    # dim = []
    # c = 0
    # tt = []
    # for ti in remaining:
    #     if (c+1)%5 != 0 or c == 0:
    #         tt.append(ti)
    #     else:
    #         dim.append(tt)
    #         tt = []
    #     c += 1
    # if len(dim) == num:
    #     print("wow")

    dim = []
    c = 0
    for ti in remaining:
        if (c+1)%5 != 0 or c == 0:
            dim.append(ti)
        c += 1
    d = " ".join(dim)
    print(num, len(dim))
    print(d)
    fnl = [img_name, num, w, h, d]
    writer.writerow(fnl)