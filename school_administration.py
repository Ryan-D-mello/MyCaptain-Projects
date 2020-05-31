import csv

def file_input(student_data):
    with open("Data.csv", "a", newline="") as data:
        write=csv.writer(data)
        if student_index==1:
            write.writerow(("Name", "Age", "Contact Number", "E-Mail ID"))
            write.writerow(student_data)
        else:
            write.writerow(student_data)

condition=True
student_index=1
while(condition==True):
    student_info=input("Enter information of student #{} in following pattern (Name Age Contact_Number E-Mail_ID): ".format(student_index))
    student_info_list=student_info.split(" ")
    print("Entered information: \nName : {}\nAge : {}\nContact Number : {}\nE-Mail ID : {}"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    quality_check=input("Is this correct?(yes/no): ")
    if quality_check=="yes":
        file_input(student_info_list)
        student_index+=1
    
    condition_checker=input("Do you want to continue to add student information?(yes/no): ")
    if condition_checker=="yes":
        condition=True
    elif condition_checker=="no":
        condition=False
