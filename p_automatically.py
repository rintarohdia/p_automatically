# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:35:17 2023

@author: rinta
"""
from tkinter import filedialog
import tkinter as tk
root=tk.Tk()
root.withdraw()
root.filename=filedialog.askopenfilename(
    title="ファイルを開く",
    filetypes=[("Text file",".txt")],
    initialdir="./")
f = open(root.filename, 'r',encoding="utf-8")
data = f.readlines()
f.close()
a=""
for i in data:
    a+=i+"</p>"
root.filesave=filedialog.asksaveasfilename(
    title="名前をつけて保存",
    filetypes=[("html",".html")],
    defaultextension ="html")
if root.filesave!="":
    with open(root.filesave,"w") as f:
        f.write(a)

