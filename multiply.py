#18/03/22
#Noela completed multiply.py
number=[12,10,32,3,66,17,42,99,20]
sum=0
product=1
for i in number:
    print(i)
# printing numbers and their corresponding squares
for i in number:
    print("the number", i,"has the square",i*i)
#printing the sum of all the numbers
for i in number:
    sum=sum+i
print("the sum is ",sum)
#printing the product of all the numbers of the list
for i in number:
    product=product*i
print("the product is ",product)
