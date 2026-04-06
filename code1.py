print("Hello , World")

name= "Nithya"

height=5
is_student=True

print("Hello",name,height)

#input taking from user
age=input("Enter your age;")
print("age:",age)

#input() always gives string,not number
age1=int(input("enter your age"))
print("age1:",age1+1, "next year")

#Add two number
a,b=map(int,input("Enter two number to be added").split())
print("Sum of a+b:",a+b)
print("Multiplication of a and b:",a*b)