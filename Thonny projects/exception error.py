try:
    fh=open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Erorr:can\'t find or read data")
else:
    print("Written contect in the file successfully")
    fh.close()