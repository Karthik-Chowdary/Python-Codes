import urllib.request
import urllib.parse

def read_text():
    quotes = open("/Users/KarthikChowdary/Desktop/profanity.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    address = "http://www.wdylike.appspot.com/?q="+encoded_text
    connection = urllib.request.urlopen(address)
    output = connection.read().decode('utf-8')
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
    
