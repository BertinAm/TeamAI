#18/03/22
#Noela completed 3_sides.py
#assuming the the side of the triangle is the longest
print("enter the lenght of the 3 sides")
def check(a,b,c):
    if( (c*c) == ( (a*a)+(b*b)) ):
        print("this is a right_angled triangle")
    else:
        print("this is a right_angled triangle")
check(int(input("enter side a")),int(input("enter side b")),int(input("enter side c")) )
