#Retrieving resources from the web using Http requests 

import urllib.request #This module provides the classes and code needed to make Http requests

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode())) #This will print out the result code of the url using the get method
    
if __name__ == "__main__":
    main()