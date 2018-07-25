'''
@author: laptop
'''

"""
Operating on the DOM
"""
import xml.dom.minidom
def main():
    
    #Using the parse() function to load and parse the sample data XML file
    doc = xml.dom.minidom.parse("samplexml.xml")
    
    #Print out the document node and the name of the first child tag
    #nodeName, firstChild, and tagName are all standard properties of DOM
    print(doc.nodeName) 
    print(doc.firstChild.tagName)
    
    







 
if __name__ == "__main__":
    main();
