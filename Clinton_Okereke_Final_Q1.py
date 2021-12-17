

filename1= input('Please entre the name of the file: ')
wordstocpy= int(input('Please entre the number of words you wish to copy: '))

f= open(filename1, "r")
newfile= open ('c:\\TEXTFILE\\PROG1783file1After.txt', "a")

newfile.write(f.read(wordstocpy))

print(f.read())
f.close()
newfile.close()

#Clinton Okereke 8752065