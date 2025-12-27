
# List is one of the datatype ,it performs store multiple datatypes
#insert ,updation and delete

list=[1,2,3.0,"apple",7]
print(list)
print(list[0]) #1
print(list[4])  #7
print(list[-1]) # 7
print(list[0:3])    #1,2,3.0
list.insert(5,"add")
print(list)
#insert is the command for adding inside the list
list.append("sub")
print(list)
#append is the keyword to insert any value added to inside the list as the last value
del list[0]
print(list)
list[1]="I updated"
print(list)

