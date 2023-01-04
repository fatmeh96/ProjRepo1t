import solution2
file=open('file.txt','r')
file2=open('file2.txt','r')
res=open('result.txt','w')
solution2.fileToStr(file)
res.write("The encrypt text is:\n")
for line in file:
    res.write(line)
res.write("The decrypt text is:\n")
for li in file2:
    res.write(li)
# for line2 in fileToStr(file):
#     file1.write(line2)

