def most_frequent(string):
    for i in range(len(string)):
        temp=0
        for j in range(len(string)):
            if string[i] in string[j]:
                temp=temp+1
        mydict[string[i]]=temp
    print(mydict)

mydict={}
string=input("Enter a string: ")
most_frequent(string)

#I couldn't figure how to print the sorted list(by values) along with their keys.
#Secondly, is there an alternate more efficient logic to this program?
