# -*- coding: utf-8 -*-。
import os
import sys

# Get the writing date of the passage
def getPassageDate(name):
    fp = open(name, 'r')
    lines = fp.readlines()
    for line in lines:
        a = line.split(' ')
        if a[0] == "date:":
            return a[1]
            break
    fp.close()



# Rename the file (adding the date before the original file name)
def changeFileName(name, date):
    newName = date + '-' + name
    os.rename(name, newName)



# Handle the file content
def contentHandling(name):
    # Get the contents of the file
    fp = open(name, 'r')
    contents = fp.readlines()
    fp.close()
    
    # Insert '---' line before the passage contents
    contents.insert(0, '---\n')
    
    i = 0
    length = len(contents)
    print length
    while i < length:
        # Delete some lines
        if contents[i][0:4] == 'date' or contents[i] == '<!-- more -->\n' \
            or contents[i] == "categories:\n" or contents[i] == "categories:\n" \
            or contents[i] == "{% blockquote %}\n" or contents[i] == "{% endblockquote %}\n" \
            or contents[i] == "***\n" or contents[i] == "{% endblockquote %}":
            del contents[i]
            length -= 1
            continue
        
        # Add two blank space before each tag
        if contents[i][0:2] == '- ':
            contents[i] = "  " + contents[i]
        

        if contents[i] == "{% codeblock lang:cpp %}\n":
            contents[i] = "{% highlight cpp %}\n"

        if contents[i] == "{% endcodeblock %}\n":
            contents[i] = "{% endhighlight %}\n"

        i += 1

    # Write the contents back to the file
    fp = open(name, 'w')
    contents = "".join(contents)
    fp.write(contents)
    fp.close()


# Main program

# Open the file list
files = os.listdir('/Users/vitasuper/Desktop/testtest')

for name in files:
    if name[0] != '.' and name != 'a.py':
        date = getPassageDate(name)
        print date
        contentHandling(name)
        changeFileName(name, date)

