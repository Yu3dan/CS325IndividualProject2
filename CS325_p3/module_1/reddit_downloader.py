# Author: Jordan Brisley
# Date: 10/16/2023
# CS325-02 Project 3 Module 1
# Purpose: The purpose of this module in Project 3 is to take a URL given by the user and download the HTML (source code) then write it into another file named "html.txt" and store it into folder Data and subfolder raw.
# Using the sys module it allows the program to take an argument given by a user. (In this case a Reddit URL). Then it uses urllib.request to access the URL's source code and download it into the directory in quotes.
# NOTE: In order for this to work, you must still use an OLD reddit URL similarly to project 1 and 2. Ex: " https://old.reddit.com/r/OnePiece/comments/174xxx0/i_get_its_an_purely_optical_thing_but/"

import sys
import urllib.request

URL = sys.argv[1]       #Saving the URL argument giving by user 

urllib.request.urlretrieve(URL, "../CS325_p3/Data/raw/html.txt")     #Retrieving and printing out the text contents of URL given by user to text file "html.txt"

