file=open('file.txt','r')
file1=open('result.txt','w')
file1.write("The encrypt text is:\n")
for line in file:
    file1.write(line)
file1.write("The decrypt text is:\n")
from solution2 import fileToStr
decryptedText=solution2.fileToStr(file)
print(decryptedText)
# for line2 in fileToStr(file):
#     file1.write(line2)

