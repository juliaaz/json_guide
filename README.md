# |Json Guide|

This program organises a navigation(guide) in a json file.
# |Functions|
Module includes 3 different functions:
1. check_format.
    |Checks whether user's file is a json file.|
2. read_file.
    |Reads a json file and converts it into a dictionary.|
3. guide.
    |Navigates(guides) a user throught the json file (dictionary format).|

# |Example of usage|
When user runs the program, he/she has ability to input a path to a json file in which he/she wants to be navigated.
Note: firstly, the program checks whether it actually is a son file with the help of check_format function.
After that on every step user will have choices:
1.  Choose a key or number of an element
2.  Type exit if the user wants to end the program.
3.  Move to parent (type parent)
4.  print current element (type print)

Note: if user prints 'parent' and he has already reached the document root,then proram will ask user to choose something else.
If user inputs wrongly, then program notifies him/her.