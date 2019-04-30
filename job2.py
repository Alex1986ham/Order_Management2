#!/usr/bin/env python3.3

import os
import shutil

try:
    fh = open('C:/Users/D&D/Downloads/Downloads2/?.txt')
    print("File exists")
except FileNotFoundError:
    print("File not exists...will create it")
    #shutil.copyfile('C:/Users/D&D/Desktop/flask-tutorial/flaskr/db.py', 'C:/Users/D&D/Desktop/flask-tutorial/flaskr/db6.py')


#exists = 'C:/Users/D&D/Desktop/flask-tutorial/flaskr/db4.py'
#os.path.isfile('C:/Users/D&D/Desktop/flask-tutorial/flaskr/db4.py')
#if exists:
    # store config file
#    print ('ok')
#else:
    # keep
    #shutil.copyfile('C:/Users/D&D/Desktop/flask-tutorial/flaskr/db.py', 'C:/Users/D&D/Desktop/flask-tutorial/flaskr/db4.py')
