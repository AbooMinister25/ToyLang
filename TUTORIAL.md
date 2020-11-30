# Lite v.1.0.3 Official Tutorial

Welcome to the official Lite tutorial, this document will walk you through the basics of Lite, and give you an understanding of how to use it. First, check if you have Lite installed, if not, see the README.md on instructions on how to install it. Lite only has syntax highlighting in VSCode, so I suggest you use that for this tutorial.

## Your first program

This step will walk you through creating your first Lite program. First create a file called `main.lite` in whatever directory you desire. From there, you should have an emtpy file. Lite uses the `print` function to display data to the console, you can print out both Integeres and Strings. You'll learn more about data types later on. Right now, include the following in your file.
```
print("Hello World");
```
This line of code will print out `Hello World` into the console. Lite uses semicolons to seperate different functions. Lite allows multiple statements on one line, so technically, you could have your entire program on one line, seperated by semicolons. Now you need to run the program. There are two ways you can run a lite program, one of them is to run the following command, with your information formatted in.
```
C:\Users\{user}\{Where the folder is located}\Lite-Master\Lite-Master\lite run -f main.lite
```
If the above command doesn't work, check that your information is formatted in correctly, and that you have the requirements installed. If it still doesn't work, run the following, formatted again.
```
C:\Users\{user}\{Where the folder is located}\Lite-Master\Lite-Master\lite\lite.py run -f main.lite
```
The above two commands will run `main.lite`, and if everything goes correctly, the output in the console should be the following.
```
Hello World
```
Congratulations! You have written your first Lite program.

## User Input

The next thing we are going to cover is *user input*. Lite can collect user input from the console using the `input` function. Type the following into your `main.lite` file.
```
input("Enter a number: ");
```
The above will prompt the user to enter a number, try running the file again, your output should be the following.
```
Enter a number: 
```
The console is prompting you to enter a number, enter whatever, and press enter. Lite hasn't done anything with the number you entered because you haven't saved it anywhere. In order to save user input, you'll have to assign it to a variable, which we will cover in the next section.

## Variables

Lite uses variables to store user input and data types. Variables are defined like the following.
```
x = 10;
```
The above has set the variable `x` to the Integer `10`. Now, if you call x, the value will be `10`.
```
x = 10;
print(x);
>>> 10
```
You can store strings inside variables as well
```
x = "Hello";
print(x);
>>> Hello
```
Variables can also be used to store user input, type the following into your `main.lite` file.
```
num = input("Enter a number: ");
print(num);
```
The above code will promp you to enter a number, and save it to the variable `num`, which is then called and printed out. Now try running your file, if you did everything correctly, you should get something like the following.
```
Enter a number: 25
25
```
I entered the number `25`, which was then printed out into the console by `print`.

## Data Types

Lite makes use of 4 main data types, Strings, Integers, Arrays, and Booleans. A string is a string of characters that can be defined like below.
```
x = "Hello";
```
In the above, `Hello` is a string. Strings can be added together to produce a new string, such as the following.
```
x = "Hello " + "World";
print(x);
>>> Hello World
```
An Integer is basically any kind of whole number. Integers can be added, multiplied, subtracted, and divided by other integers, as in the calculator example in the README.md.
```
print(5 + 5);
>>> 10
print(5 * 5);
>>> 25
print(5 / 5);
>>> 1
print(5 - 5);
>>> 0
```
An array is basically a list of data types, and can be defined with square brackets `[]`.
```
x = [1,2,3];
```
Array values can be accessed through indexing, like the following.
```
x = [1,2,3];
print(x[0]);
>>> 1
```
Array indexing starts at `0`, and goes up from there, so `x[0]` would return `1`. Arrays can be looped over, which will be more focused on in the Loops section of this tutorial.

Booleans consist of two values, `true` or `false`. Booleans can be stored in variables, or used in while loops, which will be showcased in the Loops section of this tutorial.

## If/Else Statements

If/Else statements are used to define *conditional statements*, which can be used to only execute a block of code if a given condition is true. If statements can be used like the following.
```
if 5 == 5 {
    print("True!");
}
```
The above will print out `True`, because 5 is equal to 5. Make sure not to get mixed up between `=` and `==`. `=` is used to define variables, and `==` is a comparison operator, and is used to see if two values are true.

Else is used to execute a block of code if an if statement above it isn't true, like the following.
```
if 5 == 6 {
    print("True");
}
else {
    print("False");
}
>>> False
```
In the above, the if statement is not true, which leads to code to evaluate the block of code underneath `else`. You can also use if statemetns to compare variables.
```
x = 5;
y = 5;
if x == y {
    print("True");
}
>>> True 
```

## Functions

This section of the tutorial is on defining functions. Functions can be defined using the `function` keyword, and can take any number of arguments. A function is like `print` or `input`, and using the `function` keyword. you can define your own, such as.
```
funcion add(num1, num2) {
    print(num1 + num2);
}

add(1, 2);
>>> 3
```
The above defines a functino called `add` which takes two arguments and adds them together. Functions can have no arguments as well.
```
function hello() {
    print("Hello!");
}
hello();
>>> Hello!
```
Any variables or arguments that are defined inside of a function cannot be accessed outside of the function.
```
function myfunction() {
    print("Hello!");
    x = 5;
}

myfunction();
print(x);
// Raises an error saying that x isn't defined.
```

## Loops

There are two kinds of loops in Lite, `for` and `while` loops. While loops loop over a block of code as long as a condition is true, such as.
```
while true {
    print("Hi");
}
// Will print Hi forever.
```
Or with a condition
```
while 5 == 5 {
    print("Hi");
}
// Will print Hi forever
```
For loops can be used to loop over a range or over an array.
```
for i in range(5) {
    print("HI");
}
// Will print Hi 5 times
```
Or with an array
```
arr = [1,2,3];
for item in arr {
    print("HI");
}
// Will print Hi 3 times.
```

## Afterword

Congratulations! You have finished learning the basics of Lite! If you want to learn some more concepts, check out REFERENCE.md. Thanks for reading, and please report any bugs or errors to me, and feel free to raise an issue, thanks!