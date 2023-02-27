import sys
import os
from datetime import date

today = str(date.today())

photos = "1"
video = "2"

x = (input('Select a function: 1. photos 2. video'))

# Creates a new folder to sort photos
if x == "1":
    print('How do you want to name your folder?')
    nameFolder = input()
    
    os.chdir ('/Users/x******n/Desktop') #Enter the file path for your pwd.
    try:
        os.mkdir (nameFolder + "_" + today)
        print('File Created.')
    except FileExistsError:
        print('Folder name already exists.')
else:
    if x != "1" or "2":
        print("That's not a valid function.")