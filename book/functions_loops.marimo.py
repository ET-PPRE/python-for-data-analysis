import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Functions and Loops""")
    return


@app.cell
def _(mo):
    mo.md(r"""In this chapter, you will learn about two important concepts in Python: functions and loops. Functions help you organize your code into reusable blocks, while loops allow you to repeat actions efficiently. We'll explore how to define and use functions, as well as different ways to loop in Python using for loops, ranges, and while loops. Finally, you will also be introduced to classes, which let you group data and functions together to build more advanced programs.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Functions""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Functions are collections of Python statements with an associated _function name_ that can be _called_ from other places in the code. A simple example of a function with name _print_hello_ in python, and its call, look like this:""")
    return


@app.cell
def _():
    # Define the function
    def print_hello():
        print("Hello!")

    # Call the function
    print_hello()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Notice the indentation after the colon in the function definition, all statements in the function block are part of the function definition. Furthermore note the keyword _def_ , telling Python that a function definition is coming, and the brackets _()_ after the function name. 

    Functions have their own _scope_ , i.e., variables defined within a function are not known elsewhere:
    """
    )
    return


@app.cell
def _(aaa):
    def printing_hello():
        aaa = 3.14
        print("hello! aaa =", aaa)
    
    printing_hello()
    print("aaa =", aaa)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Function can take input data, called _arguments_. These arguments appear as comma seperated lists within the parentheses following the function name, without any type specification. Python is simply executing all statements in the function block on the given variable:""")
    return


@app.cell
def _():
    # Define function:
    def print_value(x):
        print("Input is =", x)

    # Call function:
    a = 3.14
    print_value(a)
    print_value(42)
    print_value(42 > 40)
    print_value("Yeah!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    It is important to note that **the function argument's names are part of the function's scope, hence they have nothing to do with other variables elsewhere.**

    Think of functions as fully independent pieces of code. Their argument variables will be filled with data from outside, but otherwise the function has no 'contact' to outside data. In other words, you can always understand functions when reading them, even if you do not know anything about the code that is using them. However, globally known variables are of course also known to functions - but relying on those is often not the best style of coding.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Functions can take multiple arguments, seperated by comma:""")
    return


@app.cell
def _():
    # Define function:
    def print_power(x, n):
        print(x, "to the power of", n, "equals", x**n)

    # Call function:
    print_power(3, 2)

    # Also possible:
    print_power(x = 3, n = 2)
    print_power(n = 2, x = 3)

    # Different output
    print_power(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Function arguments can have default values:""")
    return


@app.cell
def _():
    # Define function:
    def power(x = 42, n = 2):
        print(x, "to the power of", n, "equals", x**n)

    # Call the function with default arguments:
    power()

    # Call the function with default value for second argument:
    power(3)

    # Also possible:
    power(x = 3)
    power(n = 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Functions can _return_ data to the calling statement: """)
    return


@app.cell
def _():
    # Define function:
    def calc_sum(a, b):
        return a + b

    # Call function:
    res = calc_sum(40, 2)
    print("Sum =", res)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Functions can also return multiple values:""")
    return


@app.cell
def _():
    # Define function:
    def calc_sumdiff(a, x):
        return a + x, a - x

    # Call function:
    sum, diff = calc_sumdiff(40, 2)
    print("Sum =", sum)
    print("Difference =", diff)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Functions can be defined _locally_ in the current scope. They will then only be known there, and they can use variables from the local scope as well:""")
    return


@app.function
def f(x):
    
    p = 2 * x
    
    def g(y):
        return y**2 + p
    
    return g(p)


@app.cell
def _():
    f(2) # this is working
    return


@app.cell
def _(g):
    g(2) # this is not working - g is unknown here
    return


@app.cell
def _(p):
    p # also p is unknown here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If you are doing proper coding, you should always add a comment that explains your function. If you add it directly after the function definition, it can be found by your IDE and is shown when hovering above the function name with the mouse. There are also ways to extract all such comments into html or other documentation, but we will not go deeper into this topic right now.  

     An example:
    """
    )
    return


@app.cell
def _():
    def print_moin():
        """ 
        This is our test function.
        It simply prints 'Moin!'. 
    
        Also note that it is possible to write
        a multiline comment here, explaining 
        the purpose of the function.
    
        In fact, in real-life coding, this is
        exactly what you should do in any function 
        that you write. Always have in mind that
        someone else whom you do not know has to be
        able to properly use your function, so
        imagine you are writing comments for this
        unknown person.
        """
        print("Moin!")

    print_moin()
    return


@app.cell
def _(mo):
    mo.md(r"""You do not have to process all return data from a function:""")
    return


@app.cell
def _():
    def fun(a,b):
        return a+b, a-b , a*b

    # simply write underscore "_" for all skipped returns:
    c, _, _ = fun(8,3)
    print("c =",c)

    # alternative
    c, *_, = fun(8,3)
    print("c =",c)

    # not the same
    *_, c = fun(8,3)
    print("c =",c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Looping""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### _for_ - Loops""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    For any sequence we can define a _for_ loop, stepping from element to element:

    ```python
    for x in sequence:
        (execute...)
    ```

    Here a simple example for a _list_ :
    """
    )
    return


@app.cell
def _():
    list = [1,2,3,4,5,1,8,6]
    print("list =",list)

    for x in list:
        print("This is x =", x)
    return (list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If you need not only the element _x_ , but also the position of _x_ in the list, you can use the built-in function _enumerate_ :""")
    return


@app.cell
def _(list):
    print("List =",list)

    for i, j in enumerate(list):
        print("Position", i, ": value =", j) 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Note that this also works on mixed lists:""")
    return


@app.cell
def _():
    mixed_list = ["Hi", 3.14, 42]
    print("List =",mixed_list)

    for pos, val in enumerate(mixed_list):
        print("Position", pos, ": element =", val, "type =", type(val))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    This is a very useful feature. However, this is one of the reasons why Python can be slower than other languages, if for-loops are used where they shouldn't be. Python always first has to check the type of a list member before operating on it, and this can take time. Thus, **explicit loops over container sequences should be avoided whenever possible.**

    However, for-loops are always a good starting point when thinking about a new problem, especially is you are new to programming, or to Python - a solution with a for-loop is better than no solution at all.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""To jump or skip an element in a loop `continue` is used. While, to interrupt or leave the loop early `break` is used. """)
    return


@app.cell
def _(list):
    print("List =",list)

    for element in list:
    
        # ignore odd entries:
        if element % 2 != 0:
            continue
    
        print("element =",element)
    
        # stop loop if element larger 5:
        if element > 5:
            break
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Ranges""")
    return


@app.cell
def _(mo):
    mo.md(r"""Often we need to loop over a range of integers. This can be achieved by the _range()_ function:""")
    return


@app.cell
def _(list):
    print("List =", list)
    print("Length of list = ", len(list))
    print()

    for var in range(len(list)):
        print("i =", var, ", element =", list[var])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Notice that the stop value i = 8 is not included in the output.

    The starting point of the range is by default 0, but it also can be explicitly given:
    ```python
    range(start,stop_not_included)
    ```
    """
    )
    return


@app.cell
def _():
    for number in range(2,10):
        print("i =",number)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Furthermore, the step size can be given as third argument, if not 1:
    ```python
    range(start,stop_not_included,step)
    ```
    """
    )
    return


@app.cell
def _():
    for p in range(2,10,2):
        print("p =", p)

    print()
    for r in range(10, -3, -2):
        print("r =", r)
    return (p,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### _while_ - Loops""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""While loops are another very useful loop form, which runs for as long as their test condition evaluates to true:""")
    return


@app.cell
def _():
    n = 0
    while n**2 <= 20:
        print(n, n**2)
        n += 1 # inceasing n by 1
    return


@app.cell
def _(mo):
    mo.md(r"""Note that `continue` and `break` also work in while-loops. These are useful features in cases where potentially the code could run in cases where infinite looping over a certain condition is possible.""")
    return


@app.cell
def _():
    m = 0
    while m**2 <= 20:
    
        m += 1
    
        if m % 2 != 0:
            continue
        
        print(m, m**2)
    
        if m > 3:
            break
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Classes""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""A class is like a container for functions and data, for example:""")
    return


@app.class_definition
class MyData:                   # class names are usually in CamelCase
    
    def __init__(self, x):
        self.x = x
    
    def calc_y(self):
        return self.x**2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can see that the class with name "MyData" contains two functions, called "\_\_init\_\_" and "calc_y". We can now create a so-called _object_ of that class by the following syntax:""")
    return


@app.cell
def _():
    data = MyData(3.14)              # data is an object from the MyData class
    print("data x =", data.x)
    print("data y =", data.calc_y())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There are three things to notice here:

    - using the dot-syntax "object.attribute" you can access the data and the functions of the class
    - the \_\_init\_\_ function is called not by its name, but directly by the name of the class, here "MyClass". This returns the object, hence `data = MyData(...)`. This function is often called "constructor" of the class. You don't have to define a constructor, by default the object is created without any stored input data.
    - In the definition of the class, we have an additional argument called "self". This is automatically given by the dot-syntax (and replaced by the object), hence just give the other arguments to the function.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can create as many more objects of this class as we wish, they are all independent quantities in memory.""")
    return


@app.cell
def _():
    data_2 = MyData(4)
    print("data_2 x =", data_2.x)
    print("data_2 y =", data_2.calc_y())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Note that **everything in Python is an object of some class**, as indicated by the fact that you can use the dot on any variable. 

    The topics of classes and object-oriented programming are not covered in this course. However, it should be noted that this is behind (almost) all the dots we will encounter.
    """
    )
    return


if __name__ == "__main__":
    app.run()
