# Lite  v.1.0.0
### An interpreted programming language made in python3


Lite is a programming language made in `python3`, by Rayyan Cyclegar, or AKA AbooMinister25. Lite was made using the `lark` parsing library, and is still in development stages. The following is an example of a calculator made using Lite.
```
print("Welcome To My Calculator!");

x = input("Enter an operation: ");

if x == "plus" {
    num1 = input("Num1: ");
    num2 = input("Num2: ");
    print(num1 + num2);
}
if x == "minus" {
    num1 = input("Num1: ");
    num2 = input("Num2: ");
    print(num1 - num2);
}
if x == "mul" {
    num1 = input("Num1: ");
    num2 = input("Num2: ");
    print(num1 * num2);
}
if x == "div" {
    num1 = input("Num1: ");
    num2 = input("Num2: ");
    print(num1 / num2);
}
```

#### Lite currently has support for the following
* print statements
* input statements
* if statements
* else statements
* functions (limited)
* variables
* addition
* subtraction
* multiplication
* division
* loops
* booleans
* other small built in functions, full reference can be found at the documentation

Functions are very limited at the moment, Lite does not support arguments and doesn't have return statements yet, all of this is planning to be added in a later release.
You can find more examples and a complete and more detailed reference at the documentation. (Coming Soon)

# Installation
The installation for Lite is pretty straightforward, just follow the steps below.
* The following is the current stable release of lite, download it. [Lite 1.0.0](lite.exe)
* Once lite has been installed, you can run it by calling its full path, like the following