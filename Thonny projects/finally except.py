try:
    Parth=open("A.doc","w")
    try:
        Parth.write("This is my test file for exception handling")
        
    finally:
        print("Going to cluse the file")
    Parth.close()
except IOError:
    print("Error: can/'t find or read data")