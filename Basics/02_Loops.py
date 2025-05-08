#For Loop
#Q1 print 1 to 10 using while loop
for i in range (1,11):
    print(i)

#Q2 print even number from 1 to 100
for i in range (1,101):
    if i%2==0:
        print(i)
#Q3 print Odd numbers from 1 to 100
for i in range(1,101):
    if i%2 != 0:
        print(i)
        
#Q4 print sum of odd numbers from 1 to 100
total=0
for i in range(1,101):
    if i % 2 !=0:
        total += i
print(total)

#Q5 print all elements of list
List=['apple','orange','banana','watermelon']
for fruit in List:
    print(fruit)
    
#Q6 print multiplication table of given number
num=int(input("enter the number:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    
#Q7 Print Square of numbers from 1 to 10
for i in range(1,11):
    print(i*i) 
    
#Q8 calculate the sum of numbers from 1 to n
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    sum += i
print(f"{sum}")
        
#Q9 print reverse number from 10 to 1
for i in range (10,0,-1):
    print(i)
    
#Q10 print number that divisable by 5 from 1 to 100
for i in range(1,101):
    if i%5==0:
        print(i)