fileptr = open("himanshu.txt","w");
content = fileptr.write('alphabet');
print(type(content))
print(content)
fileptr.close()
