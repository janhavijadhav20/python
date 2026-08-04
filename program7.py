print ("********************* student addmision eligiblity *********************")

name = input("enter student name:")
age = int(input("enter student age:"))
marks = float(input("enter student marks:"))



if(age>=17 and age<=30):
    print("student is eligible for addmission")
   
    if(marks>=60):
        print("student is eligible for addmission")

        if(marks>=85):
           print("student is selected for the AIML department")

        elif(marks>=80):
            print("student is selected for the CSE department")

        elif(marks>=70):
            print("student is selected for the ENTC department")     

        else:
            print("you can apply for MACHANICAL or CIVIL department")

    else :
        print("student is not eligible for addmission, because of less marks")

else :
    print("student is not eligible for addmission, because of age limit")


