import os
import math
from examOOP import Student
Student_list={}

Manager_pass='1234'
def manager():
    while True:
        check_pass=input("enter password: ")
        if check_pass==Manager_pass:
            while True:
                    manager_list=["1-add_stu","2-remove_stu","3-show_stu","4-exit"]
                    print("-----------------------------------------------------------------------------------")
                    for x in manager_list:
                        print(x)
                    print("-----------------------------------------------------------------------------------")    
                    ch=int(input("enter choice: "))
                    if ch==1:
                            id_stu=input("enter student id: ")
                            name=input("enter student name: ")
                            Student_list[id_stu]={"name":name,"marks":{}}
                            print(f"{name} added!")
                            stu=Student(id_stu,name)     
                    elif ch==2:
                            remove_stud=input("enter the ID of the expelled student: ")  
                            if remove_stud in Student_list:
                                stu=Student(remove_stud,Student_list[remove_stud]["name"]) 
                                print(f"{Student_list[remove_stud]["name"]}:",end="")
                                Student_list.pop(remove_stud)
                                print("removed") 
                                if os.path.exists(stu.math_file):{ os.remove(stu.math_file) }
                                if os.path.exists(stu.science_file):{ os.remove(stu.science_file) }
                                if os.path.exists(stu.english_file):{ os.remove(stu.english_file) }
                                os.rmdir(stu.folder)
                            else:
                                 print("not found in the system!")     
                    elif ch==3:
                            for id in Student_list:
                                print(f"{Student_list[id]["name"]}------{id}")
                    elif ch==4:
                        print("thanks!")
                        return stu
        else:
            print("enter correct password!")                   
def student_fun():
    stud_list=["1-Math","2-Science","3-English","4-Marks","5-Exit"]
    print("-----------------------------------------------------------------------------------")
    for x in stud_list:
        print(x)
    print("-----------------------------------------------------------------------------------") 
    ch_stu=int(input("enter your choice: "))
    if ch_stu==1:
        _math()
    elif ch_stu==2:
        science()
    elif ch_stu==3:
        english()
    elif ch_stu==4:
        mark_student()
    elif ch_stu==5:
         print("Good luck!")        
def _math():
    id_stu=input("enter your id: ")
    if id_stu in Student_list:
        print(f"Hello,{Student_list[id_stu]["name"]}")
        print("---------------------------------------Math Exam---------------------------------------")
        stu=Student(id_stu,Student_list[id_stu]["name"])
        stu._exam("math")
        mark=stu.result_exam("math")
        Student_list[id_stu]["marks"]["math"]=int(mark)
    else:
        print("you are not in the system!")
def science():
    id_stu=input("enter your id: ")
    if id_stu in Student_list:
        print(f"Hello,{Student_list[id_stu]["name"]}")
        print("---------------------------------------Science Exam---------------------------------------")
        stu=Student(id_stu,Student_list[id_stu]["name"])
        stu._exam("science")
        mark=stu.result_exam("science")
        mark=stu.result_exam("science")
        Student_list[id_stu]["marks"]["science"]=int(mark)
    else:
        print("you are not in the system!")
def english():
    id_stu=input("enter your id: ")
    if id_stu in Student_list:
        print(f"Hello,{Student_list[id_stu]["name"]}")
        print("---------------------------------------English Exam---------------------------------------")
        stu=Student(id_stu,Student_list[id_stu]["name"])
        stu._exam("english")
        mark=stu.result_exam("english")
        mark=stu.result_exam("english")
        Student_list[id_stu]["marks"]["english"]=int(mark)
    else:
        print("you are not in the system!")
def mark_student():
    id_stu=input("enter your id: ")
    if id_stu in Student_list:
        total=0
        for x in Student_list[id_stu]["marks"]:
            print(f"{x}:  {Student_list[id_stu]["marks"][x]}") 
            total=total+Student_list[id_stu]["marks"][x]
        print(f"total: {total}")
        persent=math.ceil((total/300)*100)
        print(f"percent: {persent}%")       
    else:
            print("not found!")                         

while True:
    main_list=["1-Manager","2-Student","3-Exit"]
    print("-----------------------------------------------------------------------------------")
    for x in main_list:
        print(x)
    print("-----------------------------------------------------------------------------------") 
    choice=int(input("enter your choice: "))
    if choice==1:
       stud= manager()
    elif choice==2:  
        student_fun()  
    elif choice==3:
        print("you out of the system")  
        break

