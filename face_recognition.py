from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os #for getting images
import cv2 #more than 2500+ algorithms
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")