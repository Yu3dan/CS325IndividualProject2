# Author: Jordan Brisley
# Date: 10/02/2023
# CS325-02 Project 1

import requests
import sys
import os
import urllib.request


URL = sys.argv[1]       #Saving the URL argument giving by user 

urllib.request.urlretrieve(URL, "file1.txt")     #Retrieving and printing out the text contents of URL given by user to text file "file1.txt"