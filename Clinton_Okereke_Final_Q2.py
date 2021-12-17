import datetime
import re
def replace(search_text, replace_text):
    with open("c:\PROG1783 Final Exam\PROG1783File2.txt", "r+") as f:
        
        file=f.read()
        file= re.sub(search_text, replace_text, file)


        f.write(file)
    return "the text has been replaced."

search_text= 'Clinton'
replace_text= '********'
#x=datetime.datetime.now()
print (replace(search_text,replace_text))
file1=open("c:\PROG1783 Final Exam\PROG1783File2.txt", "r")
#files= open("c:\PROG1783 Final Exam\PROG1783File2.txt", "w")
#print(files.write(datetime.datetime.now()))
#files= open("c:\PROG1783 Final Exam\PROG1783File2.txt", "r")
print(file1.read())

