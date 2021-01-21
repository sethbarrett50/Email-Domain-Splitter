# Email-Domain-Splitter
This project takes a text file full of email addresses followed by a colon and a password, and searches through it to seperate emails by domain.
It does this by using regular expressions to identify email addresses, their domains, and the password.
It then sorts the emails and their associated passwords into separate text files named after the email’s domain, with all the emails of the same domain being sent to the same text file.
It then sends the output text files into a new zip file.

I'm want to better parse user input on the text file name as well as having a way for the user to name the zip file created.
I hope to come back and improve on my work, but this works very nice right now.
