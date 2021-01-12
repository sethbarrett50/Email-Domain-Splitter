'''
Created by Seth Barrett
AIST 2120-Scripting and Automation with Professor York
Final Programming Project
11/15/2020
Final Project Scripting-Seth Barrett.py


My project is an email domain sorter.
It takes a text file full of email addresses followed by a colon and a password, and searches through it to seperate emails by domain.
It does this by using regular expressions to identify email addresses, their domains, and the password.
It then sorts the emails and their associated passwords into separate text files named after the email’s domain, with all the emails of the same domain being sent to the same text file.
It then sends the output text files into a new zip file.

-----------------------------------------------------------------------
Import Statements to Import Used Modules
-----------------------------------------------------------------------
'''
import re, os, zipfile
'''
-----------------------------------------------------------------------
Opening Message
-----------------------------------------------------------------------
'''
print(f'\n{"":-^60}\n{"Final Programming Project":-^60}\n{"Email Domain Sorter":-^60}\n{"Created by Seth Barrett":-^60}\n{"AIST 2120":-^60}\n{"":-^60}\n')
'''
-----------------------------------------------------------------------
Show Current Working Directory, Ask for Input and Open Input file
-----------------------------------------------------------------------
'''
print(f'Current Working Directory:{os.getcwd()}')
files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ]
for file in files:
    print(f'{"-"*5}{file}')
lgfile = open(str(input('''Please choose the text file you wish to open:''')+'.txt'), 'r')
'''
-----------------------------------------------------------------------
Read text from file, save it, and close file
-----------------------------------------------------------------------
'''
text = lgfile.read()
lgfile.close()
print(f'\n{"Text Copied":-^60}')
'''
-----------------------------------------------------------------------
Regular Expressions
-----------------------------------------------------------------------
'''
print(f'{"Checking For Email Domains":-^60}')
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    ([a-zA-Z0-9-]+)  #Group 1 used for domains
    \.[a-zA-Z]{2,4}
    )''',re.VERBOSE | re.IGNORECASE)
fullogRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    ([a-zA-Z0-9-]+)
    \.[a-zA-Z]{2,4}
    \:\w+           #For capturing password
    )''',re.VERBOSE | re.IGNORECASE)
'''
-----------------------------------------------------------------------
Group 1 is the domain of email
Create tuple for each domain
-----------------------------------------------------------------------
'''
domains = []
for groups in emailRegex.findall(text):
    potdomain = groups[1]
    if(potdomain not in domains):
        domains.append(potdomain)
'''
-----------------------------------------------------------------------
Create text file for each domain and put in zipfile
-----------------------------------------------------------------------
'''
bigzip = zipfile.ZipFile('BigZip.zip', 'w')
if len(domains) > 0:
    print(f'{"Domains Found & Adding To Text Files":-^60}')
    for string in domains:
        domfilename = str(string + '.txt')
        domfile = open(domfilename, 'w')
        for groups in fullogRegex.findall(text):
            if(groups[1].lower() == string):
                domfile.write(f'{groups[0]}\n')
        domfile.close()
        bigzip.write(domfilename, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(domfilename)
    print(f'{"Text Files Added To Zip File":-^60}\n{"Zip File Created, Filled & Named BigZip.zip":-^60}')
    bigzip.close()
else:
    print(f'{"No Email Domains Found":-^60}')
'''
-----------------------------------------------------------------------
Exit Message
-----------------------------------------------------------------------
'''
print(f'\n\n{"":-^60}\n{"End of Final Project":-^60}\n{"":-^60}')


