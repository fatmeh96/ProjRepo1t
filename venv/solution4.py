res=open('result.txt','r')
#lines num
count=0
str1=""
for line in res:
    count+=1
    line=line.lower()
    for letter in line:
        if letter.isalpha() or letter==" " or letter=='\n':
            str1+=letter
str1=str1.split()
max_length=0
max_word=""
for i in range(len(str1)):
    if len(str1[i])>max_length:
        max_length=len(str1[i])
        max_word=str1[i]
print(f"The number of lines in result file is: {count}\n")
print(f"The longest word in the file is: {max_word}")
#longest word
