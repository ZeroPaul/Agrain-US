#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt

def viewImage(name, image, y):
    if y == 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(name)
    plt.axis('off')
    plt.imshow(image)
    # plt.show()

def viewShow():
    plt.show()
