string_1="Goodbye my friend "
string_2=" It's hard to die"
msg=string_1+string_2
msg=string_1.rstrip()+string_2.lower()
print(msg)
string_1=string_1.rstrip()
string_2=string_2.lstrip()
msg='\n\t'+string_1+'\n\t'+string_2+'\n'
msg=msg.title()
print(msg)

