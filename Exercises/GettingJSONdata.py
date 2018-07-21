'''
@author: laptop
'''
import urllib.request
import json

"""
This printResults function takes an argument called data 
which is the JSON data that's read into the main function below

The loads function takes a string of JSON and parses it into a 
native Python object. So this allows us to use that object just 
like any other Python object
"""
def printResults(data):
    theJSONdata = json.loads(data)
    
    
"""
Access the contents of the JSON like any other Python object:
"""    

    
    
    
    
    
    
    
    
    
    

def main():
    """
    The data feed that the URL is pointing to is from the U.S. Geological Survey
    uses to deliver JSON data for all earthquakes within the last day with a magnitude 
    of 2.5 or greater 
    """
    dataFeed = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5"

    #Hit the URL and read the data
    webUrl = urllib.request.urlopen(dataFeed)
    print ("result code: " + str(webUrl.getcode()))
    
    #If we are able to hit that URL and got a success code of 200, 
    if (webUrl.getcode() == 200):
        data = webUrl.read()#read the contents of the url
        printResults(data)#Call the printResults function and print the data
    else:
        print("Received error, cannot parse results")
        
    if __name__ == "__main__":
        main()