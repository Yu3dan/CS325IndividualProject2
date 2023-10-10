# Author: Jordan Brisley
# Date: 10/16/2023
# CS325-02 Project 3 Module 3
# Purpose: The purpose of this last module is to remove the HTML tags from the comments. (The output from Module 2). This program opens the output from Module 2 and parses through it using Beautiful Soup as well. 
# It then opens and writes into a new file named "filteredcomments.txt" and stores this output under the folder "Data" and subfolder "processed". It writes the same comments from the output of Module 2 into this new file,
# however the difference is it removes the HTML tags by using a for loop and decomposing the style and script tags contained in the HTML. It then writes a new comment with neater format and removed HTML tags into the output of this module ("filteredcomments.txt")

from bs4 import BeautifulSoup

def remove_tags(html):                                          #cutting the HTML and CSS styling from the filtered text
    bs = BeautifulSoup(html, 'html.parser')
    for data in bs(['style', 'script']):
        data.decompose()
    return ' '.join(bs.stripped_strings)

with open("../CS325_p3/Data/raw/unfilteredcomments.txt", 'rb') as bs:                                 #Opening the text file given by user and reading it, parsing it using Beautiful Soup and html5lib
    soup = BeautifulSoup(bs, 'html5lib')

comments = soup.find_all('p')

with open("../CS325_p3/Data/processed/filteredcomments.txt", "w", encoding="utf-8") as output:                              #finally writing out the comments in a neater format without the HTML style to filteredcomments.txt 
        for comment in comments:       
            output.write(remove_tags(comment.prettify()))
            output.write("\n")
