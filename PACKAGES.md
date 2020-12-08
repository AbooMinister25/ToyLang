# Lite Libraries

Hey, in this document, I'm going to be explaining on how to interact with modules in Lite, and how to build your own. Lite has two types of modules, `Libraries` and `Evaluators`. Both of these can either be built in, or a third party module that you can install. Libraries are basically normal modules you can access using the `import` function, like below.
```
import (
    modulename
);
```
These libraries are basically files you are importing, and accessing the functions of. You can call the functions and attributes of the modules like below.
```
import (
    filetools
);
filetools.open_file("test.txt");
```
Its pretty straightforward. Lite also has another type of module you can import, that I mentioned above, called `Evaluators`. Evaluators are basically a normal module, but with only one class, the `Evaluator` class. Evaluators have their own grammar and syntax, and evaluate anything passed to the class, they can be accessed using the `include` keyword, like below.
```
include (
    EvaluatorName
);
```
They can be used like the following.
```
include (
    PythonEvaluator
);
PythonEvaluator.Evaluator(
"""
print("Hi")
"""
);

>>> Hi
```
As you can see above, Evaluators can be used to run python code, or any other languages you make an Evaluator for, as well as custom grammar. As of now, you can't actually make Evaluators yourself, as I'm trying to figure out a way to allow you to do that easily and efficiently. Lites collection of third party libraries is pretty limited, so any help and contribution is both welcome and appreciated, just contact me in some way or form, and let me know.

## Creating Libraries
As of the moment, you can only create normal libraries, not Evaluators, but that will be coming soon, right now, I'm going to show you how to create a simple beginner library. As of the moment, Lite libraries can only be made in python, so some basic knowledge of python is required before you can make a library. First of all, your going to have to install the pip package `lite-module` in order to create lite libraries. You can install it with pip using the following command.
```
# Windows
pip install lite-module

# Linux and Mac
pip3 install lite-module
```
Once you have this set, your going to need a project structure. The project stucture is going to be pretty straightforward. First, create a directory, you can name it whatever you like, it won't affect anything. After that, inside the directory, create a python file, name this whatever you like. again, it will not affect anything. After this, create a *second* python file, and make it have the same name as your library below is the format.
```
Directory Name
├── main.py
├── modulename.py
```
In my example, the library will be called `test`, so I would have the following directory tree.
```
Test
├── main.py
├── test.py
```
Now open your first `.py` file, the one whose name doesn't matter, for me, its `main.py`, and add the following lines.
```py
from lite import lite
```
The above is importing the `lite` module. Next, your going to have to call the `Setup` class for the `lite` module, which includes the setup information for your project. Now, add the following into your code, and fill it in with your relevant information.
```py
setup = lite.Setup(
    modulename,
    author,
    description, 
    version,
    filename
)
```
In the spot where it says `filename`, put the path of the other `.py` file you created, the one with the same name as your module. For me it looks like this.
```py
from lite import lite

setup = lite.Setup(
    "test",
    "AbooMinister",
    "A test module",
    "0.0.1",
    "Test/test.py"
)
```
Now, the above will create a `Setup` object which is used to register your module. Now, open up your other `.py` file, the one with the same name as your module, it should be blank. Once you have it open, write whatever functions, classes, and attributes you want your module to contain, just like a normal python module. I have the following in my file.
```py
def test():
    print("Test!")
```
Now, once your done, head back over to your other `.py` file with your setup script in it and add the following line of code.
```py
setup.register()
```
This line of code will register your module, and allow it to be imported. Now, you should have something like the following in your setup file.
```py
from lite import lite

setup = lite.Setup(
    "test",
    "AbooMinister",
    "A test module",
    "0.0.1",
    "Test/test.py"
)

setup.register()
```
Once you have this, double check to see you have everything you want in your module, and run the setup file. If everything goes correctly, you should get something like the following message in your terminal.
```
Module test successfully registered!
```
Great! You've registered your first Lite module, and it is ready to be installed. You can install it using the `ice` package manager for lite, which is used to handle third party libraries. Its still in development statges, so it may have bugs and errors you may experience, feel free to open an issue on the github. Now, to install your module, run the following command in your terminal, make sure you have Lite installed.
```
C:\Users\{user}\{Where the folder is located}\Lite-Master\Lite-Master\lite\ice.py install <modulename>
```
Make sure to pass the name of your module to it, for me, its something like this
```
C:\Users\{rayya}\{Downloads}\Lite-Master\Lite-Master\lite\ice.py install test
```
If everything went right, you should get the following message.
```
Module <modulename> installed successfully
```
Congratulations! You have registered and installed your first Lite module, you can now import it into your project and start using it.