
# Getting Started
<ul>
<li>Typing python3 on terminal opens up python.</li>
<li>For running a python script, save the script with a '.py' extension and type in 'python3 filename.py' to run the python script.</li>
<li>In python, the comments are given using '#' character. unlike other languages, python does not support multiline comments.
    so we have to use '#' on each line for adding next lines of the comment.</li>

##  Variable

<li>One of the building blocks of programming is associating a name to a value. This is called assignment. The associated name is usually called a variable.</li>
<li>Python supports the following operators on numbers.<br>
<ul><li>+ addition</li><li>- subtraction</li><li>* multiplication</li><li>/ division</li><li>** exponent</li><li>% remainder</li></ul></li>

<li>Operator precedence from low to high<br>
<ul><li>'+' addition and '-' subtraction</li><li> '%' remainder, '*' multiplication and '/' division</li><li>'**' exponent</li></ul></li>
<li>All operators except '**' exponent are left assosiative ie. they are evaluated from left.</li>

## Strings

<li>Strings are used to represent texts and are enclosed in single quotes or double quotes.</li>
<li>Multiline strings are used to represent multiline texts, usually enclosed by three single or double quotes.</li>

## Functions

<li>Just like a value can be associated with a name, a piece of logic can also be associated with a name by defining a function.</li>
<li>Functions when assigned to variables, the variable can be used to call the function by adding '()' at its end.</li>
<li>Existing Functions can be passed as arguements to new functions where the name of the function is passed to the corresponding function arguement.</li>

#### Scope of variables:

<li>Global variables can be accessed locally inside any code block, but the value of the global variable cannot be altered from inside local scope.Inorder to change/alter the global variable, 'global' keyword must be used inside the code block.</li>
<li>When an undeclared variable is used inside a code block, then Python would check for a global variable with that name, if present then the value of global variable is used inside the code block.</li>

#### Creating a Function

<li>Functions can be called with keyword parameters.</li>

```
def difference(x,y):
   return x-y
print(difference(x=5,y=2))
print(difference(5,y=2))
print(difference(x=5,2))
print(difference(y=2,x=5))
```


<li>Function arguements can have default values, the value assigned to the variable at the time of function definition will be used if the variable is not passed any value on function call.</li>

```
def val(x,y=1):
   x=x+y
print(val(5))
print(val(5,5))
```

<li>Creating functions using the 'lambda' operator, such functions are called 'lambda functions'.They are also called anonymous functions since functions created using lambda operator are not stored in a variable and are single line functions.Also lambda functions does not need 'return' statement.</li>

```
print((lambda x: x+1)(5))
# result is 6

sqr=(lambda x: x ** 2)
print(sqr(2))
# result is 4
```

## Built-in Functions

<li>Python provides various useful built-in functions like len(),min(),max(),int(),str() etc.</li>

```
print(len("helloworld"))
# result is: 10

print(str(12))
# result is: '12'
```


## Methods

<li>Methods are functions that operate on objects. ie. the functions that are defined in an object in python can be called as a method of that object.</li>

```
x="hello"
print(x.upper())
#result is: "HELLO"

# Assigning the function to a variable and then calling the variable with '()'
f = x.upper
print(f())
#result is: "HELLO"
```

## Conditional Expressions

<li>Python provides various operators for comparing values.The result of the comparison is always 'True' or 'False'.</li>

#### Some of the Conditional operators in python are:

<li>'==' equal to</li>
<li>'!=' not equal to</li>
<li>'<' less than</li>
<li>'>' greater than</li>
<li>'<=' less than or equal to</li>
<li>'>=' greater than or equal to</li>

<li>These operators can be used in combinations without 'and', 'or' operators. They can even work on strings according to lexical order.</li>

```
x>y>n

"strings">"xenial"
```
#### Logical Operators

<li>and</li>
<li>or</li>
<li>not</li>

<li>Logical operator 'and' returns true if both conditions are true.</li>
<li>The 'or' operator returns True if any one of the conditions are true even if the false condition is logically incorrect (It skips the next condition if the first condition is True and returns True).
</li>
<li>The not operator returns true when condition is false. </li>

## The if Statement

<li>The if statement checks for the condition given and if it is True, the following statements in the 'if' block will be executed.</li>
<li>There is an optional 'else' statement which is executed when the 'if' condition turns out to be 'False'.The 'elif' statement is actually 'else if' and it checks for additional conditions and executes the statements in its block if the condition is True. </li>

```
x=42
if x<10:
   print("one digit number")
elif x<100:
   print("2 digit number")
else:
   print("big number")
```
<li>Note: when the if condition is satisfied, python still checks the else condition and its block for syntax errors, if the syntax is wrong, it will be an error. </li>

```
x = 2
if x == 2:
    print x
else:
    print y

# result is :2

x = 2
if x == 2:
    print x
else:
    x +

# result is : Syntax error
```

## Lists

<li>Lists are one of the important data structures in Python. </li>
<li>Lists are heterogenous. ie. they can store all types of variables and also lists.</li>

```
x = [1, 2, "hello", "world", ["another", "list"]]
```

<li>They are indexed from '0' and the elements of the lists can be accessed using '[]' operator.</li> 

```
x=[1,2,3]
print(x[0])
# result is : 1
```

## Modules 

<li>Modules are pieces of codes which can be imported and used in our program.</li>

#### There are 3 types of modules

<li>Those we write</li>
<li>Preinstalled modules in python</li>
<li>Third-party modules</li><br>
<li>A module is imported using 'import' keyword</li>
<li>An example is importing the time module, which has methods to manipuate time and also 'sys' module which has 'argv' property which stores the command line input.The first element in 0th index of 'sys.argv' will be the program name .</li>

```
import time
print(time.asctime())
#result: prints the current time

import sys
print(sys.argv[0])
print(sys.argv[1])
# input: python3 filename.py hello
# result: 
filename.py
hello
```

</ul>

