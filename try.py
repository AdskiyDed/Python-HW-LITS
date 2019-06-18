one = 1
string = 'hiworld'
tuple_new = (one,string)
list_new = [one,string,tuple_new]
dic_new = {tuple_new:list_new}
set_new = set(dic_new)
set_new1 = {one,two,three}
print (type(one), one,string,tuple_new,list_new,dic_new,set_new,set_new1, sep='\n')
print (type(one),type(string),type(tuple_new),type(list_new),type(dic_new),type(set_new),sep='\n')
input()
