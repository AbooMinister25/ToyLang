# Lite
### A simple interpreted language made in python.

Lite has the following syntax:

```
//This is a comment
print(5 + 2);
//prints out 7

//conditionals

x = 10

if x == 10 {
  return true;
} else {
  return false;
}

//functions

function myFunction(args){
  print(args);
  return args;
}

//user input

input("enter a number");
```

So far I have a basic lexer and parser with only the print function.
