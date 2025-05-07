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
    