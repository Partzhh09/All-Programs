import re
line = 'Cats are smarter than dogs';
searchobj = re.search(r'(.*)than(.*?).*',line,re.M|re.I)
if searchobj:
    print("search.group():",searchobj.group())
    print("search.group(1):",searchobj.group(1))
    print("search.group(2):",searchobj.group(2))
else:
    print("Nothing found")