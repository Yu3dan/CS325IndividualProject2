# Author: Jordan Brisley
# Date: 10/16/2023
# CS325-02 Project 3 Module 2
# Purpose: The purpose of this module in Project 3 is to use BeautifulSoup (scraping library) in order to parse through the HTML provided by Module 1's URL.
# Once the program has opened the textfile (from MOD 1), it reads through the HTML using BS4 and then finds the HTML section (by it's class) containing all of the Reddit posts comments.
# Once it finds the section, it seperates the comments by finding all instances of "<p>" in which each comment is initiated by.
# Then as it finds each instance of a comment, it opens a new file named "unfilteredcomments.txt", stores the file under the same folder and subfolder Module 1's output was stored and writes each comment using a for loop seperated by an empty space. ("\n")

from bs4 import BeautifulSoup

textfile = "../CS325_p3/Data/raw/html.txt"      #output from Module 1 (HTML from users URL) 

with open(textfile, 'rb') as bs:                                 #Opening the text file given by user and reading it, parsing it using Beautiful Soup and html5lib
    soup = BeautifulSoup(bs, 'html5lib')

commentree = soup.find("div", attrs={'class':'sitetable nestedlisting'})                #finding the block that contained comments
comments = commentree.find_all('p')                                                     #finding each comment by looking for <p>

with open("../CS325_p3/Data/raw/unfilteredcomments.txt", "w", encoding="utf-8") as output:                              #finally writing out the comments in "unfilteredcomments.txt" with a line seperated
    for comment in comments:
        output.write((comment.prettify()))
        output.write("\n")
     