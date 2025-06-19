import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium", app_title="intro_to_python.marimo")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Introduction to Python""")
    return


@app.cell
def _(mo):
    mo.md(r"""This chapter provides a foundational overview for new programmers. Beginning with an introduction to Python, the material covers essential concepts such as data types, variables, input and output operations. Key points presented here aim to help learners understand how to store and manipulate data, interact with users, and annotate their code for readability. By the end of this chapter, you will be familiar with the basic building blocks required for writing effective Python scripts.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Data Types""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Variables""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Variables are containers for storing data values. In Python there is no special command for declaring them, you simply use the `=` symbol:""")
    return


@app.cell
def _():
    variable = 3
    return (variable,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now the variable with name `a` is associated with the piece of memory that holds the data `3`. We can simply print it or use it in calculations as we wish:""")
    return


@app.cell
def _(variable):
    print(variable)
    return


@app.cell
def _(variable):
    print(variable + 1)
    return


@app.cell
def _(variable):
    variable2 = variable * 2 + 1
    print(variable2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Variables can be named according to your preference, however it is important to follow a logical approach to variable naming, which allows the code to be readable to other users (or yourself in the future). Commen naming conventions and recommandations can be found in the [link](https://peps.python.org/pep-0008/#naming-conventions).""")
    return


@app.cell
def _():
    pi = 3.14
    radius = 1
    area_circle = pi * radius**2    # common naming style for variables is lowercase with underscore(s)
    print(area_circle)

    WindSpeed = 12                  # another common style is CamelCase, but this is not recommended for variables as it is used for class names (see below)
    print(WindSpeed)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can delete any variable by using the `del` command:""")
    return


@app.cell
def _(variable):
    del variable

    # The next line will raise an error because 'a' has been deleted
    print(variable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Two variables can point to the same object in memory:""")
    return


@app.cell
def _():
    c = 3.14
    d = c
    print("c =", c, ", d =", d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""But remember, changing one of them re-assigns the variable name to a completely new piece of memory. The other variables is still associated with the old object.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Data Types""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Python comes with built-in numeric types, built-in composed types, and built-in functions. Based on these building blocks, developers can create the data structures and functionality that they need in order to attack their problem.

    Build-in numeric types are "data atoms", and Python provides three different such types:

    - **int**: Integer numbers,
    - **float**: Double precision floating-point numbers,
    - **complex**: Complex numbers
    - **str**: String.

    As we have already seen, variables in Python can simply be created without specifying the type of data:
    """
    )
    return


@app.cell
def _():
    var = 3
    return (var,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Python automatically determines the data type, given the assigned data. We can check the choice by using the _type_ function:""")
    return


@app.cell
def _(var):
    type(var)
    return


@app.cell
def _():
    var1 = 3.14
    type(var1)
    return (var1,)


@app.cell
def _():
    text = "Hello"
    type(text)
    return


@app.cell
def _():
    compare = 3 < 4
    print("compare =",compare)
    type(compare)
    return


@app.cell
def _():
    z = complex(2,3)
    print("z =",z)
    type(z)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There are several things to note here:

    - The _type_ function returns the name of the basic data type, in fact the name of the underlying class.
    - There is no type called _double_ in python. In fact, the Python _float_ is the c _double_ (8 bytes or more, platform dependent).
    - The Python _int_ type is actually the c _long int_.

    For more details on built-in numeric types, see the [python documentation](https://docs.python.org/3/library/stdtypes.html).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It is possible to assign data values to multiple variables at once by simply using the assignment operator "=":""")
    return


@app.cell
def _():
    action, year = "Assign", 2024
    print("action =",action,", type =",type(action))
    print("year =",year,", type =",type(year))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Also, we can enforce a type of our choice by explicitly creating specific data objects as follows:""")
    return


@app.cell
def _():
    number1 = float("3")
    print("number1 =",number1,", type =",type(number1))
    print()

    number2 = int(3.6)
    print("number2 =",number2,", type =",type(number2))
    print()

    number3 = str(3.14)
    print("number3 =",number3,", type =",type(number3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""A string in Python can consist of letters or numbers or a combination of both. They should always be enclosed with either single *' '* or double *" "* quotation marks. It is important that strings started with one or double quotation mark must be closed with one or double quotation marks respectively.""")
    return


@app.cell
def _():
    single_quoted = 'This is a single-quoted string'
    print(single_quoted)
    type(single_quoted)
    return


@app.cell
def _():
    double_quoted = "This is a double-quoted string"
    print(double_quoted)
    type(double_quoted)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Mind that a numbers in a string are **not** representations of the numerical value but rather just the character representing the numerical value. As example: While 8 is an integer value and 8.7578 is a float value, \"8\" or '8.7578' is no longer an integer resp. float but a string.""")
    return


@app.cell
def _():
    number8 = 8
    string8 = '8'
    print("number8 =",number8,", type =",type(number8))
    print("string8 =",string8,", type =",type(string8))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Input, Output and Comments""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Input""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The `input()` function in Python is used to take user input as a string. When called, it pauses program execution, displays an optional prompt (if provided), and waits for the user to type something. The input is then returned as a **string**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Example:
    In this example, the user is prompted to enter their name. The input is saved to the variable `name` and then printed as part of a greeting.

    **Note:** You see an error message on the website because the `input` function only works in a Python environment.
    """
    )
    return


@app.cell
def _():
    name = input("Enter your name: ")
    print(f"Hello {name}!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Output""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It can be noticed how anytime we needed to output variables, the `print()` function was used. It prints strings, i.e., variables that store text, but also variables directly:""")
    return


@app.cell
def _():
    print("Hello this is text")
    print('Hello this is text')
    print("Hello 'this' is text")
    print('Hello "this" is text')

    string = "This is a str variable"
    print(string)

    pi_value = 3.14
    print(pi_value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can print many objects by just giving them as separate arguments to the print function:""")
    return


@app.cell
def _(var, var1):
    print("Hello:", var, ", and a great example for a number is", var1, ".")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Notice that an extra blank space is smuggled in for each comma.

    Another fancy way of printing variables is to use a so-called formatted string, indicated by the preceding letter _f_. Anything within curly brackets will then be translated into a string and replace the bracket.
    """
    )
    return


@app.cell
def _(var):
    print(f"Hello, var = {var}! Plus one: {var + 1}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It is possible to make it neater by setting the number of decimal points we want to output, by simpli adding `:.xf`, behind the variable, where _x_ is the amount of numbers behind the decimal point we want.""")
    return


@app.cell
def _(var):
    # Output with variables set to only 2 decimal points
    print(f"Hello, var = {var:.2f}! Plus one: {(var + 1):.2f}") 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can enforce a new line by the "\n" character. This is an example for an [escape sequence](https://www.python-ds.com/python-3-escape-sequences).""")
    return


@app.cell
def _():
    print("Hi!\nJumping to a new line.\n\nHi from down here!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 1.2.3 Comments""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Comments are pieces of text in your code that are simply ignored by the interpreter.

    Single-line comments are created by the hashtag symbol `#`:
    """
    )
    return


@app.cell
def _():
    # This is a comment
    return


@app.cell
def _():
    a = 3.14 # all text behind the hashtag is ignored
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    You can also include multiline comments in your code. The beginning and the end of such comments accross lines are indicated by three ` symbols in a row.

    **Note**: In a Jupyter notebook (or in a Python or iPython shell) such a comment would be interpreted as a multiline string.
    """
    )
    return


@app.cell
def _():
    """ 
    The medicine, education, wine, public order, 
    irrigation, roads, the fresh-water system, 
    and public health 
    - what have the Romans ever done for us?

    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In general, commenting code is very valuable - unless your code is really self-explaining. You should make it a habit from the very early stages of your coding career.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 1.3 Numerical Operations and Conditionals""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The built-in numeric types support basic math operations:""")
    return


@app.cell
def _():
    # addition:
    num1 = 1000
    num2 = 5
    addition = num1 + num2
    print("num1 =",num1,", num2 =",num2,": Result = num1 + num2 =",addition)
    return num1, num2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The numerical operation can be done in the print statement as well:""")
    return


@app.cell
def _(num1, num2):
    print("num1 =",num1,", num2 =",num2,": Result = num1 + num2 =",  num1 + num2)
    return


@app.cell
def _(num1, num2):
    # subtraction:
    subtraction = num1 - num2
    print("num1 =",num1,", num2 =",num2,": Result = num1 - num2 =",subtraction)
    return


@app.cell
def _(num1, num2):
    # multiplication:
    multiplication = num1 * num2
    print("num1 =",num1,", num2 =",num2,": Result = num1 * num2 =",multiplication)
    return


@app.cell
def _(num1, num2):
    # power
    power = num1 / num2
    print("num1 =",num1,", num2 =",num2,": Result = num1:num2 = ",power)
    return


@app.cell
def _():
    # Magnitude of a Complex Number
    complex_num = 3 + 4j
    magnitude = abs(complex_num)
    print(magnitude)
    return


@app.cell
def _():
    # Modulo Operator - returning the remainder of devision
    remainder = 7 % 2
    print()
    print("Remainder of 7/2 is:",remainder)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""For more advanced functionality, we need to import the other libraries like `math`, `numpy`, or hundreds of other specialized open-source libraries.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 1.3.2 Conditionals""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Conditions in Python are expressions that evaluate to the boolean values `True` or `False`. This is done through comparison operators:

    - `==` : is equal to
    - `!=` : is not equal to
    - `<` : smaller than
    - `<=` : smaller or equal to
    - `>` : larger than
    - `>=` : larger or equal to

    Which are often time combined with conditional operators `and`, `or`.
    """
    )
    return


@app.cell
def _():
    3 == 3.14
    return


@app.cell
def _():
    3.14 < 4
    return


@app.cell
def _():
    p = 3.14 
    p >= 3 and p < 3.3
    return (p,)


@app.cell
def _(p):
    p == 3.1415 or ( p > 3 and p < 3.3 )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### _if_ statements

    Conditionals are conveniently used in so-called _if_ statements.

    The syntax for _if_ statements in Python is:

    ```python
    if ...condition :
        execute...
    ```

    where the condition after the _if_ must evaluate to `True` or `False` (or 1 or 0), whereas the following statements are only to be executed if the condition was `True`.
    """
    )
    return


@app.cell
def _(p):
    print("p =",p)
    if p > 3 and p < 3.3:
        print("This looks like an approximation of π.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    An important point here is that there are four **blank spaces** before the _print_ statement in the above function: This is called **indentation**. 

    The indentation rules for Python [are as follows](https://docs.python.org/2.0/ref/indentation.html):

    _Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements._

    _First, tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight (this is intended to be the same rule as used by Unix). The total number of spaces preceding the first non-blank character then determines the line's indentation. Indentation cannot be split over multiple physical lines using backslashes; the whitespace up to the first backslash determines the indentation._

    This means that you can use anything between 1 and 8 spaces for defining the indentation level of a block, or alternatively a _Tab_. However, commonly used, also by editors, are 4 spaces.

    This may appear tideous at first sight, but
    - it reduces the number of brackets `{}` or semicolons `;` throughout the code
    - and it increases readability.

    The indentation levels reflect the logic of the code.

    Note that in Python **indentation does not define a scope** like in C/C++ or other languages. This means, variables in Python are available also after leaving the indentation level - and not deleted from memory.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ####  _else_ statements
    We can go on, introducing `else`, which defines the course of action, in cases where the conditions of a `if` statement or not fulfilled. 

    ```python
    if ...condition :
        execute...
    else:
        execute...
    ```

    In other words, the statements after the `else` are executed if the condition after the `if` becomes  `False`.
    """
    )
    return


@app.cell
def _():
    r = 5
    print("r =",r)

    if r > 3 and r < 3.3:
        print("This looks like an approximation of π.")
    
    else:
        print('Your number ist not approximate to π.')
    return (r,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Sometimes one wishes to subsequently evaluate a set of mutally exclusive conditions. This can be done using `elif`, which is a mash-up of else+if:

    ```python
    if ...condition1:
        execute...
    elif ...condition2 :
        execute...
    elif ...condition3 :
        execute...
    else:
        execute...
    ```
    """
    )
    return


@app.cell
def _(r):
    print("r =",r)

    if r > 3 and r < 3.3:
        print("This looks like an approximation of π.")

    elif r % 2 == 0:    # here we use the modulus operator to check is a number is odd or even
        print('Your number ist not approximate to π and is even.')

    else:
        print('Your number ist not approximate to π and is odd.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If, for some reason, you wish to do nothing in a certain case, then use the statement `pass`:

    ```python
    if ... :
        ...
    elif ... :
        pass
    else:
        ...
    ```
    """
    )
    return


@app.cell
def _(p):
    print("p =",p)

    if p > 3 and p < 3.3:
        print("This looks like an approximation of π.")

    elif p == 3:  
        pass

    else:
        print('Your number ist not approximate to π.')
    return


if __name__ == "__main__":
    app.run()
