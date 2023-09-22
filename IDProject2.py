# Author: Jordan Brisley
# Date: 10/02/2023
# CS325-02 Project 2

import sys
from bs4 import BeautifulSoup
import html5lib
import requests


textfile = sys.argv[1]       #Saving the URL argument giving by user 

with open(textfile, 'rb') as bs:                                 #Opening the text file given by user and reading it, parsing it using Beautiful Soup and html5lib
    soup = BeautifulSoup(bs, 'html5lib')

def remove_tags(html):                                          #cutting the HTML and CSS styling from the filtered text
    bs = BeautifulSoup(html, 'html.parser')
    for data in bs(['style', 'script']):
        data.decompose()
    return ' '.join(bs.stripped_strings)

commentree = soup.find("div", attrs={'class':'sitetable nestedlisting'})                #finding the block that contained comments
comments = commentree.find_all('p')                                                     #filtering out the comments in previously found block

#for comment in comments:                                                               #testing for loop and results from parsing
    #print(remove_tags(comment.prettify()))

with open("comments.txt", "w", encoding="utf-8") as output:                              #finally writing out the comments in a neater format without the HTML style to comments.txt 
    for comment in comments:
        output.write(remove_tags(comment.prettify()))
        output.write("\n")
     
     
        




