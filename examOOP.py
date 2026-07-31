import os
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.folder=f"students/{name}"
        os.makedirs(self.folder,exist_ok=True)
        self.math_file=os.path.join(self.folder,"math.txt")
        self.science_file=os.path.join(self.folder,"science.txt")
        self.english_file=os.path.join(self.folder,"english.txt")
    
    def _exam(self,type_exam):
        type_=type_exam 
        ques=open(f"qu_{type_}.txt","r")
        ans=open(getattr(self,f'{type_}_file'),"w")
        for x in range(1,6):
            print("\n")
            print(ques.readline())
            stu_ans=input("enter answer:")
            ans.write(f"{stu_ans}\n")
    
    def result_exam(self,type_exam):
        type_=type_exam
        correct_answer=open(f"correctAnswer_{type_}.txt","r")
        student_answer=open(getattr(self,f"{type_}_file"),"r")
        count=0
        for i in range(1,6):
            if correct_answer.readline().strip()==student_answer.readline().strip():
                count=count+20  
        if count<50:
            print(f"mark: {count}\nyou Fail{self.name}!😕") 
            return count 
        else:
            print(f"mark: {count}\ncongratulation {self.name}! you pass🤩🥳")
            return count 

           
