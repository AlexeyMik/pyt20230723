# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
s = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
#
listW=[]
k1 =0
while k1 < len(listW) :
    while s[k1]==" " and k1<len(s) : 
        k1 +=1  
    k2 = k1
    while s[k2+1]!=" " and k2+1<len(s) :
        k2 +=1
    listW.append(s[k1,k2])
    k1=k2+1
print(len(listW))
print(listW)

