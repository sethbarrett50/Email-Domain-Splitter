'''
Created by Seth Barrett
Email Domain Splitter
11/15/2020
Email Domain Splitter-Seth Barrett.py


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
fullogRegex = re.compile(r'''( #Group 0 for capturing email, colon and password
    [a-zA-Z0-9._%+-]+ 
    @
    ([a-zA-Z0-9-]+) #Group 1 Used for capturing the domain
    \.[a-zA-Z]{2,4}
    \:\w+           
    )''',re.VERBOSE | re.IGNORECASE)
'''
-----------------------------------------------------------------------
Group 1 is the domain of email
Create tuple for each domain
-----------------------------------------------------------------------
'''
bigzip = zipfile.ZipFile('BigZip.zip', 'w')
domains = []
for groups in fullogRegex.findall(text):
    potdomain = groups[1]
    domfilename = str(potdomain.lower() + '.txt')
    if(domfilename not in domains):
        domains.append(domfilename)
    domfile = open(domfilename, 'w')
    domfile.write(f'{groups[0]}\n')
    domfile.close()
for domain in domains:
      bigzip.write(domain, compress_type=zipfile.ZIP_DEFLATED)
      os.remove(domain)
bigzip.close()
'''
-----------------------------------------------------------------------
Exit Message
-----------------------------------------------------------------------
'''
print(f'\n\n{"":-^60}\n{"End of Final Project":-^60}\n{"":-^60}')


