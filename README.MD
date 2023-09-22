# HTML text file to Filtered Comments
### CS325 Individual Project 2

This project is focused on using Python to convert a Reddit page given by user to a text file containing it's text only media. Once that text file is created, then it will then parse through the HTML, filter out the comments, and print them into another text file.

If you are interested in using my code above, the first thing you must do is clone this repository by using this command in your terminal:

```
git clone https://github.com/Yu3dan/CS325IndividualProject2
```

Once you have done this, make sure you are in the correct directory the repository (and its content) was downloaded to using cd (file location) in your terminal.

The requirements.yaml file included is all the neccesary libraries in the environment I coded this project under while using miniconda.
In order to use the packages needed to run this program, you must create a new environment using the .yaml file given. Before you do this, you must remember to deactivate your current environment using

```
conda deactivate
```

The command to create the new environment is:

```
conda create --name my_yaml_env --file requirements.yaml
```

My_yaml_env would be the name of the new environment in that instance (You may use any name you would like to). Next, activate the new environment with the commmand:

```
conda activate my_yaml_env
```

(Note: In order to 100% see the comments in the HTML text file, replace www in the URL to old, Example: https://www.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/ VS https://old.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/ ) 

Now, the syntax to create the text file containing HTML from the Reddit page you provide is:

```
python IDProject1.py (URL)
```

The output of project 1 should be a text file where all the source code of the URL you provided is neatly written to a text file (file1.txt).
The output.txt file included here is my output using the Reddit URL https://old.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/ .

My command would look like this:

```
python IDProject1.py https://old.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/
```

If ran correctly, you should see your updated file1.txt file in the same folder with all the new data of the Reddit post you provided.

In order to verify whether this was done correctly, you may open file1.txt and press CTRL+F on your keyboard in order to search the first comment in the post. If it comes up, everything is set for project 2.

Once this is set, the next command would be:

```
python IDProject2.py file1.txt
```

This command takes file1.txt (output from project 1) and parses through it to find the comments, then prints them neatly into comments.txt.
After this you should see an updated comments.txt with all the comments of the post in a format like so:

[–] Lukeinafter 46 points 47 points 48 points 13 days ago (25 children)
Waiting for someone to say zoro is already close to yonko level

"Lukeinafter" is the author of the comment, and "Waiting for someone to say zoro is already close to yonko level" is the commment itself.

