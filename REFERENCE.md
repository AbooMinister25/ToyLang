## Lite v.1.0.3 API Reference

Below is the full API reference for the latest stable version of Lite.

## Builtins

> `print`
* Prints data out to the console.
* Can be passed strings, expressions, functions, arrays, and integers.
* Example:
```
print("Hello, World");
>>> Hello, World
```
> `input`
* Collects user input through the console
* Can be passed strings, expressions, functions, arrays, and integers.
* Example:
```
input("Enter a number: ");
>>> Enter a number: 42
```
> `exit`
* Used for exiting the program.
* Can be passed an optional exit message.
* Example:
```
exit("Bye!");
>>> Bye!
```
> `wait`
* Used for pausing the code for a given amout of time in seconds.
* Can be passed only integers.
* Example:
```
print("Before 5 Seconds");
wait(5);
print("After 5 Seconds");
>>> Before 5 Seconds
...
>>> After 5 Seconds
```
> `sum`
* Used for getting the sum of a given array.
* Can only be passed arrays.
* Example:
```
arr = [1,2,3];
print(sum(arr));
>>> 6
```
> `random_integer`
* Used for getting a random integer from a given range.
* Can be passed two integer.
* Example:
```
print(random_integer(1, 10));
>>> 5
```
> `read_file`
* Used for reading the lines of a file.
* Can be passed a filename as a string.
* Outputs an array.
* Use the `filetools` library for more efficient file handling
* Example:
```
print(read_file("test.txt"));
>>> ['Test File']
```
> `doc`
* Gives the docstring for every builtin
* Can only be passed a string
> `mean`
* Gives the mean of a given array.
* Can only be pased an array
* Example:
```
arr = [1,2,3];
print(mean(arr));
>>> 2
```
> `square_root`
* Used for returning the square root of a given integer
* Can only be passed a single integer
> `path_exists`
* Used to see if a given path exists. Use the `filetools` lib for more efficient file handling
* Can only be passed a string
> `range`
* Used for returning a range of a given integer.
* Can only be passed an integer.
* Example:
```
for i in range(5) {
    print("HI");
}
>>> HI
>>> HI
>>> HI
>>> Hi
>>> Hi
```
> `hash`
* Used for getting the hash of a given data type
* Can only be passed integers or strings.
* Example:
```
print(hash("Hello"));
>>> -3365352440980255850
```
> `keys`
* Used for getting all of the keys in a dict
* Keys are stored in an array
* Example:
```
dict = {"HI": 1, "Bye": 1};
print(keys(dict));
>>> ["HI", "Bye"]
```
> `type`
* Used for getting the data type of an object
* Can be used on variables or plain data types as well.
* Example:
```
x = "Hi"
y = 5
print(type(x));
print(type(y));
>>> String
>>> Integer
```

## Control Flow

> `if`
* Used for creating conditional statements
* Can be passed several types of conditions
* Example:
```
if 5 == 5 {
    print("True");
}
>>> True
if 5 == 6 {
    print("True");
}
>>> None
```
> `else`
* Used to define a statement that is executed if the if statements before it are all false.
* Isn't passed any condition
```
if 5 == 6 {
    print("True");
}
else {
    print("False");
}
>>> False
```
> `function`
* Used for defining functions
* Arguments are optional but can be passed
* All arguments and variables declared inside a function are local, and cannot be accessed from the rest of the program.
* Example:
```
// With arguments
function add(val1, val2) {
    print(val1 + val2);
}
add(5, 5);
>>> 10
// Without arguments
function hello() {
    print("Hello!");
}
hello();
>>> Hello!
```
> `return`
* Used for returning values from functions
* Can be used to assign the return value of a function to a variable.
* Example:
```
function my_function() {
    return("Function!");
}
x = my_function();
print(x);
>>> Function!

> `while`
* Used to declare a while loop.
* Loops over a block of code as long as the given condition is true.
* Example:
```
// With bools
while true {
    print("HI");
}
>>> Hi
>>> Hi
>>> ...
// With condition
while 5 == 5 {
    print("HI");
}
>>> Hi
>>> ...
```
> `for`
* Used to declare a for loop.
* Can be used to loop over an array.
* Still very limited, and iterables do not work.
* Example:
```
// with range
for i in range(5) {
    print("HI");
}
>>> Hi
>>> Hi
>>> Hi
>>> Hi
>>> Hi
// With array
arr = [1,2,3];
for i in arr {
    print("HI");
}
>>> Hi
>>> Hi
>>> Hi
// With iteration
arr = [1,2,3];
for i in arr {
    print(i);
}
>>> 1
>>> 2
>>> 3
```

## Data Types

> `String`
* A string of characters that can be iterated over or printed out to the console.
* Can be added to other strings
> `Integer`
* Any type of real number
* Can be added, subtracted, multiplied, or divided with another integer.
> `Array`
* A list of data types
* Can be iterated or looped over
* Example:
```
arr = [1,2,3];
print(arr);
>>> [1,2,3]
```
> `Dict`
* A JSON like key/value object
* Values can be accessed by keys
* Example:
```
dict = {"Hi": 1, "Bye": 2}
print(dict["Hi"])
>>> 1
```

> `true`
* A boolean data type, returns True
> `false`
* A boolean data type, returns False


## Imports and Includes

> `import`
* Used to import an external library
* Example:
```
import (
    filetools
)
// Module filetools imported
```
> `include`
* Used to include an Evaluator to the program.
* Example:
```
include (
    PythonEvaluator
)
```

## Libraries and Evaluators

Lite has two kinds of modules you can import into your code, `Libraries` and `Evaluators`. A library can be imported using the `import` statement.
```
import (
    filetools
)
```
When you import a library, all of the libraries functions can be used by you, like the following.
```
import (
    filetools
)
x = filetools.open_file("test.txt");
// The value of test.txt is now stored in the variable x.
```
An Evaluator is another kind of module that you can import into your script, but it only has one class, the `Evaluator()` class, which is used to evaluate code. an Evaluator can parse and evaluate its own Grammar and AST, or evaluate another languages grammar. There is only one Evaluator included in Lite at the moment, the `PythonEvaluator` Evaluator. This can be used to evaluate python code within your script. Evaluators can be imported with the `include` function, and are used like the following.
```
include (
    PythonEvaluator
)
PythonEvaluator.Evaluator(
"""
print("Hello From Python!")
"""
)
>>> Hello From Python!
```
