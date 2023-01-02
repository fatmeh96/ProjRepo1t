file=open('file.txt','r')
def replaceChar(str1):
    from solutions import finalDic
    str1=str1.lower()
    str2=""
    l=list(finalDic.keys())
    for i in str1:
        if l.__contains__(i):
            str2+=finalDic[i]
        else:
            str2+=i
    print(str2)

def fileToStr (filePath):
    str1=""
    for line in filePath:
        for l in line:
            if l.isalpha() or l==" " or l=="\n":
                str1+=l

    replaceChar(str1)
    
fileToStr(file)

