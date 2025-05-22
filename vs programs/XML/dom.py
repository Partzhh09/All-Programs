from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies2.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root Element :%s" % collection.getAttribute("shelf"))
    
movies = collection.getElementsByTagName("movie")
    
for movie in movies:
    print('--------------------')
    print("<<<<<< MOVIES >>>>>>")
    if movie.hasAttribute("title"):
        print("title :%s" % movie.getAttribute("title"))
        type = movie.getElementsByTagName('type')[0]
        print("type :%s" % type.childNodes[0].data)
        format = movie.getElementsByTagName('format')[0]
        print("format :%s" % format.childNodes[0].data)
        rating = movie.getElementsByTagName('rating')[0]
        print("rating :%s" % rating.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print("description :%s" % description.childNodes[0].data)