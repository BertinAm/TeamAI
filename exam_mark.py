#18/03/22
#Noela created exam_mark.py
def result(mark):
    if(mark>=75):
        print("you are awarded First")
    if(mark>=70 and mark<75):
        print("you are awarded Upper Second")
    if(mark>=60 and mark<70):
        print("you are awarded Second")
    if (mark >= 50 and mark < 60):
        print("you are awarded Third")
    if (mark >= 45 and mark < 50):
        print("you are awarded F1 Supp")
    if (mark >= 40 and mark < 45):
        print("you are awarded F2")
    if (mark  < 40):
        print("you are awarded F3")
result(int(input("enter mark")))
