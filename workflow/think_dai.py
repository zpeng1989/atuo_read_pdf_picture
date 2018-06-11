# encoding: utf-8
"""
Created on Mon Apr  9 17:31:52 2018

@author: zhangp
"""

import dai
import time
import sys
time1 = time.time()
import urllib, urllib2, base64
import json
import re
import os
import Tkinter 
import Tkinter as tk
import tkFileDialog as filedialog

root = Tkinter.Tk()
root.title('my window')
root.geometry('1200x1200')


var = tk.StringVar()
lp = tk.Label(root, bg='yellow', width=50, text='input')
lp.place(x=3,y=40)

def openfile():
    r = filedialog.askopenfilename(title='打开文件')
    var.set(r)

btn1 = Tkinter.Button(root, text='File Open', command=openfile)
btn1.place(x=3,y=3)

var1 = tk.IntVar()
l = tk.Label(root, bg='yellow', width=20, text='output')
l.place(x=400,y=10)


def hit_me():
    path_var = var.get()
    filepath = os.path.split(path_var)[0] + '/'
    print(filepath)
    filename = os.path.split(path_var)[1]
    print(filename)
    shotname = os.path.splitext(filename)[0]
    output_data = filepath + shotname + '.txt'
    lp = tk.Label(root, bg='yellow', width=50, text=path_var)
    lp.place(x=3,y=40)
    API_Key = ""
    Secret_Key = ""
    access_token=dai.get_token(API_Key,Secret_Key)
    recognition_word_high=dai.recognition_word_high(filepath,filename,access_token)
    if not os.path.exists(path_var):
        lpp = tk.Label(root, bg='yellow', width=50, text='something error')
        lpp.place(x=3,y=500)
    if not os.path.exists('output_file_one.txt'):
        lpp = tk.Label(root, bg='yellow', width=50, text='one file is not exist')
        lpp.place(x=3,y=500)
    if os.path.exists('output_file_one.txt') and os.path.exists('output_file_one.txt'):
        file_one = open('output_file_one.txt', 'rb')
        with open (output_data, 'w')as output_txt:
            lines1 = file_one.readlines()
            list1 = ''
            for line in lines1:
                elements = line.rstrip().split()
                elements = str(elements[0]) + '\n'
                list1 = list1 + elements
                output_txt.write(elements)
        lpp = tk.Label(root, text = lines1)
        lpp.place(x=400,y=40)
		



b = tk.Button(root, 
    text='hit me',     
    width=15, height=2, 
    command=hit_me)   
b.place(x=3,y=80)
root.mainloop()


