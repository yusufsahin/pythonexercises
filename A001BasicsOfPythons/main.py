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
#define method
def greet(name):
    return (f"Hello world!,{name}")

print(greet("Yusuf"))
print(greet("Ece"))

def topla(x,y):
    return x+y

k=int(input("k değerin giriniz : "))
l=int(input("l değerini giriniz : "))

print(topla(k,l))

#dictionary
studen_scores={"Alice":95,"Bob":90,"Charlie":75}
print(studen_scores["Alice"])
print(studen_scores["Charlie"])


#try block
try:
    num=int(input("Enter a number: "))
    result=10/num
    print("Result : ",result)
except ValueError:
    print("Invalied input! Please enter a valid number")
except ZeroDivisionError:
    print("Cannot devide by zero")

##file write

with open("example.txt","w") as file:
    file.write("Hello World!,File Write")

#file read
with open("example.txt","r") as file:
    content=file.read()
    print(content)

#File write with exception

try:
    with open("output.txt","w") as file:
        file.write("Hello world,this is a sample file")
except IOError:
    print("Error while writing to the file")
except Exception as e:
    print("An unexcepted error occured:" ,str(e))
else:
    print("File writing process completed successfully")

try:
    #open the file in read mode
    with open("output.txt","r") as file:
        content=file.read()

    print("File content:")
    print(content)

except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error while reading file.")
except Exception as e:
    print("An unexcepted erro occured: "+ str(e))
finally:
    print("File reading process completed")


    # Class

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name} says 'Wolf!'")


    # initiate
    dog1 = Dog("Buddy", 2)
    dog2 = Dog("Max", 4)

    # call class method
    dog1.bark()
    dog2.bark()
