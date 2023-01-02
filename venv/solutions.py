#Part1
file=open('file.txt','w')
file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
file.write("J.U.U.U Kmltin.\n")
file.write("mmps iks nmk eio; ---> hkmu\n")
file.close()
file=open('file.txt','r')
dic1={}
dicMost4={}
str1=""
for line in file:
    line=line.lower()
    str1+=line
for l in str1:
    if l.isalpha():
        dic1[l]=str1.count(l)
l=list(dic1.values())
l=sorted(l)
flag=len(l)-1
while(flag>=0):
    for k in dic1:
        if dic1[k]==l[flag]:
            dicMost4[k]=l[flag]
    flag-=1
#etor
originalList=['e','t','o','r']
finalDic={}
lk=list(dicMost4.keys())
for i in range(4):
    finalDic[lk[i]]=originalList[i]
finalDicVal=list(finalDic.values())
finalDicKey=list(finalDic.keys())
for i in range(4):
    finalDic[finalDicVal[i]]=finalDicKey[i]
# print(l)
# print(lk)
# print(dic1)
# print(dicMost4)

# print(f"final dictionary is :{finalDic}")
