#Assigning elements given by user to two different lists
n=int(input("Enter desired length for the first list: "))
list1_data=[]
for i in range(n):
    list1_data.append(input("Enter data to first list: "))
print(list1_data)

n=int(input("Enter desired length for the second list: "))
list2_data=[]
for i in range(n):
    list2_data.append(input("Enter data to second list: "))
print(list2_data)

#Accessing elements from a tuple

t=tuple(list1_data)
print("\n\nElements in the tuple: ")
for i in t:
    print(i)

#Creating a dictionary and deleting specific elements

diction={ "1" : "Orange", "2" : "Red", "5" : "Blue"}
print("\n\nDictionary: ",diction)
del diction["2"]
print("Dictionary after deleting an element: ",diction)

