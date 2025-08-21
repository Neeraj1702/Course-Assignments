#if statement

# a=int(input("Enter the number: "))
# if a>5:
#    print("The number is greater than 5")

#----------------------------------------------------

#if-else Statement
"""
A=int(input("Enter First Number : "))
if (A>=10):
    print("Pass")
else:
    print("Fail")
print("Thank You")
"""
#------------------------------------------------------------------

#else-if Statement
'''
x=int(input("Enter First Number : "))
y=int(input("Enter Second Number : "))
Operator=input("Enter Operator(+,-,*,/) : ")
add=x+y
sub=x-y
mul=x*y
div=x/y
if Operator=="+":
    print(add)
elif Operator=="-":
    print(sub)
elif Operator=="*":
    print(mul)
elif Operator=="/":
    print(div)
else:
    print("Invalid Operator")
'''

#----------------------------------------------------------------------------

#range Function
""""
n=list(range(10,20,4))
print (n)
"""
#range func has three parameters
#1. Start value
#2. End value
#3. Steps: means gap

#-------------------------------------------------------------------

# For Loop
'''
l=['Neeraj', 2.5, 52, "AA"]
l.append(1) # add values in the end
for i in l: #print every value one by one
 print (i)
 '''

#Output:
#Neeraj
#2.5
#52
#AA
#1

#Code:
'''
x='apple'
for i in x:
 print(i)
 '''
#output:
#a
#p
#p
#l
#e

'''for i in range(1,11):
    print(i)

    #or

for i in range(1,11):
    print('Neeraj')
'''

#-----------------------------------------------------------------------------

#while Loop is like a never ending loop
#print a----> 5 times

#syntax
#counter Variable
# while(test expr):
  #statement
  #increment/decrement

  #increment working
"""
counter=1
while counter<=5:
    print('a')
    counter+=1


# decrement working 

counter=5
while counter>=1:
    print('b')
    counter-=1
"""

#----------------------------------------------------------------------------

#code reusability using functions
'''
def str():
    str1='a'
    str2='b'
    str3='c'
    print(str1+str2+str3)

str()
str() 
'''

#------------------------------------------------------------------------------------

#return statement in a function
#return func is used to end the function and return the result
'''
def str1():
    str1='a'
    str2='b'
    return str1+str2
#when we are using a return never forget to assign a variable to the function called
ans=str1()
print(ans)
'''

#--------------------------------------------------------------------------------------------

#passing arg to a func
'''
def add(a,b):
    c=a+b
    return c
    
res=add(1,2)
print(res)
'''

#passing func as an arg
'''
def add(a,b):
    return a+b
def sqr(z):
    return z*z

res=sqr(add(1,2))
print (res)
'''

#-----------------------------------------------------------------------------------------

# Modules : are python files with a .py extension like practice.py = module  i.e. it is a module and can save it and  can be import to other
# python file

#ways to import a module
'''
#1:
import math
print(math.pi)
print(math.sqrt(100))

#2:
from math import pi
print(pi)

#3:
from math import * # import all that is present in math
print(sqrt(100))
'''

#----------------------------------------------------------------------------------------

# Recursion
'''
import sys
# sys.getrecursionlimit()
# print (sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
n=0
def func():
    global n
    n+=1
    print(n)
    func()

func()
'''

#-----------------------------------------------------------------------------------------

#factorial

#0!=1
#1!=1*0!=1*1=1
#2!=2*1!=2*1=2
#3!=3*2!=3*2=6
#4!=4*3!=4*6=24
'''
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
res=factorial(4)
print(res)
'''

#-------------------------------------------------------------------

#Local V/S Global Variables
#local variable preferred higher over global

'''
n=2 #global var

def func():
    #if i want that func also print global value then i do
    global n
    n=5  #local Variable and  if we remove this local variable ,then func will also print global var value
    print(n)
func()
print(n)
'''

#---------------------------------------------------------------------------------------

#exception Handling
'''
try:
    a=2
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:      #if i know the error then do the expect 'error i know' 
    print("Zero Division Error")
finally:
    print("Continue with the code")
'''

#----------------------------------------------------------------------------------------

#File Handling
#1:
'''
file=open("File.txt","w")
#directory= specify the location
#mode= r,w,a,r+
file.write("Hello World")
file.write("\nHow are you")
file.close()
'''

#2;
# with open('File.txt','w') as f:
#     print(f.write("My"))


#reading data from file

#using #1 method
'''
file=open("File.txt","r")
#reading=file.read(10) #specifying how many characters i want to read as parameters like 10
#reading1=file.readline() # read line of a file
reading2=file.readlines()# it combines the lines into a list
#print(reading)
#print(reading1)
print(reading2)
file.close()
'''

#using #2 method

# with open('File.txt','r+') as f:
#     reading2 = f.readline()
#     print(reading2)

#-------------------------------------------------------------------------------------

#Adding data to a file

'''
#1: first writing the new content
newfile=open("File.txt", 'w')
#while writing in exiting file ,it takes place of the existing characters and add the new characters and keep the other continuous characters along with newly added ones 
writing_in_file=newfile.write("Hello World!")  
print(writing_in_file)
newfile.close()

#2 then again reading the updated file or new file
newfile=open("File.txt", 'r')
r_file=newfile.read()
print(r_file)
newfile.close()
'''

#--------------------------------------------------------------------------------------------

#appending data to a file
'''
# first lets read the contents of file if exists

newfile=open("File.txt", 'r')
reading_new_file=newfile.read()
print(reading_new_file)
newfile.close()

#then lets do the appending part

newfile=open("File.txt", 'a')
appending_new_file=newfile.write("welcome to this file")
print(appending_new_file) #show how many characters are added in this file
newfile.close()

# now again read the file

newfile=open("File.txt", 'r')
reading_new_file=newfile.read()
print(reading_new_file)
newfile.close()
'''

#---------------------------------------------------------------------------------------------------------
#Here we use r+ means read + write
'''
#just using r+ because it works for both read and write ....instead of using specific r,w 
newfile=open("File.txt", 'r+')
writing_in_file=newfile.write("Hey bro")
print(writing_in_file)
newfile.close()

newfile=open("File.txt", 'r+')
reading_new_file=newfile.read()
print(reading_new_file)
'''

#-----------------------------------------------------------------------------------------------------------
#Dictionary

'''
Dictionary is similar to list. whenever we specify a list we give elements of list inside [], elements in list have index value like array 0 1 2 3
list syntax;
List[1,2,3,4], index values 

whereas for Dictionary,  we give elements inside {}
syntax:
Dictionary{key:value,...}
'''
"""
dict={'Key1':1,'Key2':'12','Key3':[453]}
print(dict)
print(dict['Key1'])

dictionary={1:'K',2:'V'}
print(dictionary[1])
"""

#----------------------------------------------------------------------------------
#Dictionary Functions
'''
Dict={'a':"apple", 'b':'banana','c':'cat','d':'dog',}
print(Dict)
Dict['e']='elephant'  #adding an element
print(Dict)
del(Dict['c']) #deleting an element
print(Dict)

#to check whether key and value is present or not
check='a' in Dict
print(check) #if present return True else False

#other way to check whether key and value is present in dic or not
print(Dict.get('g'))  #prints NONE if not present  and this is useful when u have a blank list or takes input form user to check
print(Dict.get('g',"'g' not found")) # here it prints my given output 

#to get all keys from dictionary
all_keys=Dict.keys()
print(all_keys)

#to get all values form dictionary
all_values=Dict.values()
print(all_values)
'''

#--------------------------------------------------------------------------------------
#List
'''
list=[1,2,3,' ','Neeraj']  #example of list
print(list[4])

#list operations

list1=['heyy',45.5, 85]
list2=['bob', 74]
print(list1+list2) #it combines them in a simgle list

#now i want to change the name or value of a specific index means LIst are Mutable means changeable
list2[1]=('Sandhu')
print(list2)
print(list1*2) #gives result like [1 2 3 1 2 3]
'''

#-------------------------------------------------------------------------------------------------------------------
#List functions

'''

l1=[1,45,'neeraj','bob', 45.52]
l1.append(74) # to add a value in list
print (l1)
l1.extend([52,'sandhu']) # to add multiple values in list
print(l1)
l1.remove(52) # to remove a value from list
print(l1)
del l1[0:2]  # to remove multiple values continuously
print(l1)
l1.pop(1) #another way to delete a value from list
print(l1)
# l1.clear() # if i want list to be blank
# print(l1)
l1.insert(1,'sandhu') #to add a value in between the list at a certain index
print(l1)

l2=[54,25.1,1.5,85.25,62,45.75]
# l2.sort() # to sort the values in increasing order
# print(l2)
# l2.reverse() # to reverse the values of list
# print(l2)
check_index=l2.index(1.5) #.index is used to check the index of value using with a variable
print(check_index)
length=len(l2)
print(length)

'''
#------------------------------------------------------------------------------------------------------

#list slicing
'''
num=[1,2,3,4,5]
#    0 1 2 3 4
#syntax: num[n:n+1:interval]
slice=num[1:4:2]
print(slice)

'''
#list Comprehension : it does convert multiple line of code in single line code
'''
x=[]
for i in range(11):
    #if i%2==0:  # if i want squares of even no. only
       z=i**2
       x.append(z)
print(x)

# using list comprehension
# syntax:                       {Optional}
# [expression for item in list {if (test expression)}]

x=[i**2 for i in range(11) if i%2==0]
print(x)
'''

#----------------------------------------------------------------------------------------------------
#Sets: type of collection in which we input python types like float integer string that we can define inside a set
#Sets are unordered
#have unique elements
#{}
'''
set={1,2,3,4,5,1}
print(set)
set.add(6) # to add value in set
print(set)
set.remove(1) # to remove value from set
print(set)
check=2 in set # to check whether value is present or not
print(check)

set2={1,4,2,5,6,2}
intersection=set&set2
print(intersection)  # return common elements
union=set.union(set2) #return all common elements
print(union)
subset=(set2.issubset(set)) # to check if it is a subset or not
print(subset)
'''

# ---------------------------------------------------------------------------------
# String Functions
'''
a='neeRaJ Sandhu'
print(a.capitalize()) # it makes the first alphabet in uppercase and rest are lowercase
print(a.lower()) # print all letters in lowercase
print(a.upper()) # print all letters in uppercase
print(a.swapcase())  # makers upper -> lower and lower-> upper
print(a.isalpha())  # check if string is alphabet
print(a.isnumeric()) # '7' if this is input then true
print(a.startswith('a'))
print(a.endswith('J'))
print(a.count('a'))
print(a.replace('neeRaJ','neeraj'))
print(a.find('a')) #or a.index('a')
print(a.lstrip()) # removes unnecessary space from start
print(a.rstrip()) # removes unnecessary space form end
print(a.split('a'))
print(a.rsplit('a',2))
print(a.splitlines()) # it simpley puts string int a list
print(a.split()) # simply puts the string in a list by separating each word

b='Mike','neeraj'
print(b)
# if i want to remote () and '' from output
c=','
print(c.join(b)) #then join c with b

'''

#------------------------------------------------------------------------------------------------
# String Formatting

'''
name="Neeraj"
number= len(name)*4
print("Hello {}, Your Roll Number is {}".format(name,number))

example="Newton's law"
string="This is the formula of {}".format(example)
print(string)

first='apple'
second='banana'
third='cat'
print("{0} {2} {1}".format(first,second,third))

price=150
after_tax=250
print("Price: Rs{:.2f}, After Tax: {:.2f}".format(price,after_tax))
'''

#--------------------------------------------------------------------------------------------
#list [ ] -------> are Mutable
#Dictionary { }

#Tuples ( )-----------> Immutable
'''
numbers=(1,2,3,4,5)
print(numbers)
print(numbers.count(3))
print(numbers.index(3)) # prints the index of specific no.
print(numbers[2]) # prints the number at specific index\

tup1=('Mike', 10, "Ronny", 45)
tup2=('Bob', 74)
print(tup1 + tup2)

print(len(tup1))
print(len(tup2))

# tup1[0]=99
# print(tup1)  gives error because tuples are immutable

tup3=(54,85,14,1,0,2,5,75,1,0)
print(sorted(tup3)) #sort the tuple
print(tup3.index(0))
'''