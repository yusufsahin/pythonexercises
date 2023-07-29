x = 5
y = 10
name = "Alice"
is_true = True

print(x+y)
print("Hello World!,"+name)
print(is_true)

x=10
print(x)
print("New value of x:"+str(x))

z= x+y
print(z)

a,b,c=3,7,9
print(a)
print(b)
print(c)
a,b=b,a

print(a)
print(b)
#List
fruits=["apple","banana","cherry"]
print(fruits)

print(fruits[0])
print(fruits[1])

fruits.append("drogonfruit")

print(fruits)
#Tuples
fruits_tuple=("apple","banana","cherry")

print(fruits_tuple)
print(fruits_tuple[0])

#Set

fruits_set={"apple","banana","cherry"}
print(fruits_set)

fruits_set.add("drogonfruits")
print(fruits_set)
fruits_set.remove("apple")
print(fruits_set)


x=10
#if
if x>5:
    print("x is greater than 5")

x=int(input("Please enter x : "))
#if - else
if x>5:
    print("x is greater than x : "+str(x))
else:
    print("x is not greater then x : "+str(x))

y=int(input("Please enter y : "))


#if -elif  - else
if y>20:
    print("y is greater than 20")
elif x>5:
    print("x is greater than 5 but not greater than 20")
else:
    print("x is not greater than 5")

#for
for i in range(5):
    print(i)


#while
i=0
while i<5:
    print(i)
    i+=1

# for-if - break
for i in range(5):
    if i==3:
        break
    print(i)

#for-if-continue
for i in range(5):
    if i==3:
        continue
    print(i)

for i in range(5):
    pass