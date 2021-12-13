strl=input("Enter a string:")
char=strl[0]
strl=strl.replace(char, '$')
strl=char+strl[1:]
print("Replaced string:",strl)
