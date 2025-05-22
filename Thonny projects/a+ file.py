file=open("mydetails.cpp","w+")
msg=["My name is Parth\n"]

file.write("I learn game devloping in khodiyar cad center\n")
file.write("I amstudy in 11th comm\n")
file.write("I am Video editor")
file.writelines(msg)
file.close()

file=open("mydetails.cpp","r+")
print("Reading information......")
print("*************************")

print(file.read())
print()
file.close()