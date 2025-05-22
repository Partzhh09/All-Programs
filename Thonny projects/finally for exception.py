try:
    fh=open("testfile.doc","w")
    fh.write("This is my test fille for exception handling!!")
    
finally:
    print("Error: can/'t find file or read data")