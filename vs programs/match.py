import re
line = "Cats are smarter than dogs"
matchobj = re.match(r'(.*)smarter(.*?).*',line,re.M|re.I)
if matchobj:
    print("matchobj.group():",matchobj.group())
    print("matchobj.group(1):",matchobj.group(1))
    print("matchobj.group(2):",matchobj.group(2))
else:
    print("No match!!")