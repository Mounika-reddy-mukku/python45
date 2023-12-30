str="i.like.this.programming.very.much" 
list=str.split(".") #splitting the string ['i', 'like', 'this', 'programming', 'very', 'much']
list.reverse() #reversing the list['much', 'very', 'programming', 'this', 'like', 'i']
str_out='.'.join(list) # joining the elements in list with .
print(str_out)