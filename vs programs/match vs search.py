import re
line = "Cats are smarter than dogs,parth is best";
matchobj = re.match(r'cats',line,re.M|re.I)
if matchobj:
    print("matchobj.group():",matchobj.group())
else:
    print("No match")

searchobj = re.search(r'parth',line,re.M|re.I)
if searchobj:
    print("searchobj.group():",searchobj.group())
else:
    print("Nothing found")