list=[10,20,30,40,50,140,200]
result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
