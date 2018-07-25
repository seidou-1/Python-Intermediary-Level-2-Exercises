'''
@author: laptop
'''

"""
Operating on the DOM
"""
import xml.dom.minidom

def main():
    
    #Using the parse() function to load and parse the sample data XML file
    doc = xml.dom.minidom.parse("/Users/laptop/Development/GitHub/Python/Intermediary Level 2 Examples/samplexml.xml")
    
    #Print out the document node and the name of the first child tag
    #nodeName, firstChild, and tagName are all standard properties of DOM
    print(doc.nodeName) 
    print(doc.firstChild.tagName)
    
    #Get list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill") #The tag i'm looking for is the skill tag
    print("%d skills: " % skills.length)
    
    for skill in skills:
        print(skill.getAttribute("name")) #This prints out each individual skill







 
if __name__ == "__main__":
    main();
