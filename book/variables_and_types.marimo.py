import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Data Structures""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

    In many situation you wish to store and handle several objects in a common container - think of a list, or an array in other programming languages. There are several options for doing so in python, with different properties and purposes. In the following we will get to know some of the 'native' Python data structures.

    #### Sequences
    A **sequence** is a specific type of data structure that is **ordered** and supports **indexing**. The key characteristics of sequences include:

    - **Ordered**: The elements have a defined order.
    - **Indexing**: You can access elements by their index (position in the sequence).
    - **Slicing**: Sequences support slicing to retrieve subsets of elements.
    - **Iteration**: Sequences can be iterated through, element by element.

    Python has several built-in sequences. They either store _references_ to the data, i.e. the pointer-like variables as above, in which case they are called _container sequences_, or they instead hold the _data_ itself and are called _flat sequences_ :

    - **container sequences**, they can hold _references_ to objects of different types:
      - _list_, _tuple_, _deque_
    - **flat sequences**, they hold _objects_ of one type:
      - _str_, _bytes_, _bytearray_, _memoryview_, _array_

    Another way of classifying the above sequences is their _mutability_ :

    - **Mutable sequences**, whose elements can be modified:
      - _list_, _bytearray_, _array_, _deque_, _memoryview_
    - **Immutable sequences**, whose elements cannot be changed:
      - _tuple_, _str_, _bytes_

    #### Non-Sequence Data Structures:
    Some Python data structures, like **dictionaries** and **sets**, are not considered sequences because:

    - **Dictionaries**: They are unordered, and they are accessed by keys, not by index.
    - **Sets**: They are unordered collections of unique elements, so indexing and slicing are not possible.

    We will not go through all the data structures in detail here, just a selection. 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Lists""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    As mentioned, lists in Python are _mutable container sequences_ , particularly suitable if you
    - need to collect objects of different types into one list,
    - need to change the length of the list (e.g. by adding or deleting elements on the fly),
    - plan to do more than just applying the same mathematical operation to each element (in such cases, the numpy library is a better choice, as discussed in the upcoming lecture).

    An empty list is created like this:
    """
    )
    return


@app.cell
def _():
    list = []
    print("List =",list,", type =",type(list))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Examples for non-empty lists:""")
    return


@app.cell
def _():
    # a list of integers:
    a = [1, 2, -3]
    print("a =",a)

    # a list of floats:
    b = [1.1, 2.2, -3.14]
    print("b =",b)

    # a list of strings:
    c = ["I", "am", "a", "list"]
    print("c =",c)

    # a list of lists:
    d = [a, b, c]
    print("d =",d)
    return a, b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""To get the length of a list (or any other sequence), use the `len()` function:""")
    return


@app.cell
def _(a):
    print("length a =",len(a))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can access the element number **`i`** by the subscript operator **`[i]`**:""")
    return


@app.cell
def _():
    mixed_list = ["Hello",3.14,42]
    print("mixed_list =",mixed_list)

    # 1st elemement i=0
    x = mixed_list[0]
    print("x =",x)

    # 2nd element i=1
    y = mixed_list[1]
    print("y =",y)

    # 3rd element i=2
    z = mixed_list[2]
    print("z =",z)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""As stated above, the _list_ is mutable - this means we are allowed to change data:""")
    return


@app.cell
def _(a):
    # list info:
    print("a =", a,", id =", id(a))
    print("1st Element of the a =", a[0],", type =",type(a[0]),", id =",id(a[0]))

    # change data:
    a[0] = 5      # changing the 1st element from 'Hello' to 5

    # list info:
    print()
    print("a =", a, ", id =",id(a))
    print("1st Element of the a =", a[0],", type =", type(a[0]),", id =", id(a[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can also add members to the list by the _append_ function:""")
    return


@app.cell
def _(a):
    # list info:
    print("a =",a,", len =",len(a))
    print()

    # add an element to the end:
    a.append("Banana")

    # list info:
    print("a =",a,", len =",len(a))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It is possible insert an element at a specific position:""")
    return


@app.cell
def _(a):
    # list info:
    print("a =",a)

    # insert at position 2:
    a.insert(2,"Spam")
    print("a =",a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Of course, elements can also be deleted:""")
    return


@app.cell
def _(a):
    print("a =",a)

    # this removes the first occuring 1 from the list:
    a.remove(5)
    print()
    print("a =",a)

    # this removes element at position 3 from the list:
    del a[3]
    print()
    print("a =",a)

    # this returns an element, and removes it from the list:
    popped = a.pop(1)
    print()
    print("pop =",popped)
    print("a =",a)

    # this clears the whole list:
    a.clear()
    print()
    print("a =",a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Whole lists can be added to an existing list by the + operator, or by the _extend_ function. This is called _concatenation_.""")
    return


@app.cell
def _(a, b):
    # create lists:
    list1 = ["Hello", 3.14, 42]
    list2 = [3, 4, 5]

    print("List 1 =", list1)
    print("List 2 =", list2)

    # create a list that adds the elements of list2 to those of list1:
    concatenation = a + b
    print("Concatenated List =", concatenation, id(concatenation))

    # add another list to concatenation, without creating a new list object:
    concatenation.extend([11, 22, 34, "Additional"])
    print("Extended List =", concatenation, id(concatenation))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It is easy to check if a specific element is contained in the list, by the _in_ operator:""")
    return


@app.cell
def _():
    # check if element is in a list:
    numbers = [1, 2, 3, 4, 5, 1, 1, 1]
    num = 3

    isin = num in numbers

    print(num,"is in the list", numbers, "=", isin)
    return (numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Also finding the position of first occurance of an element in the list is easy, using the _index_ function:""")
    return


@app.cell
def _(numbers):
    print("List =",numbers)

    var1 = 3
    i = numbers.index(var1)
    print(var1,"found at position",i)

    var2 = 1
    i = numbers.index(var2)
    print(var2,"found at position",i)
    return (var2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Counting occurences is straight-forward with _count_ :""")
    return


@app.cell
def _(numbers, var2):
    print("List =",numbers)

    n = numbers.count(var2)
    print(var2,"found",n,"times in the list.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Furthermore, we can _reverse_ and _sort_ the list (in-place):""")
    return


@app.cell
def _(numbers):
    # Original list:
    print("Original list =", numbers)

    # reverse the list:
    numbers.reverse()
    print("Reversed list =", numbers)

    # sort the list:
    numbers.sort()
    print("Sprted list =", numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Other useful built-in functions that act on sequences are:""")
    return


@app.cell
def _(numbers):
    print("List =",numbers)

    # calculate the minimum:
    min_number = min(numbers)
    print("min =",min_number)

    # calculate the maximum:
    max_number = max(numbers)
    print("max =", max_number)

    # calculate the sum:
    sum_numbers = sum(numbers)
    print("sum =",sum_numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Dictionaries""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A dictionary is a data structure used to store collections of key-value pairs. They are one of the core data structures in Python and are extremely flexible and useful for various tasks.

    Key characteristics of dictionaries:

    - **Key-Value Pairs**: Dictionaries consist of key-value pairs. Each key is associated with a corresponding value. Keys are typically unique within a dictionary.
    - **Mutable**: Dictionaries are mutable, which means you can add, modify, or remove key-value pairs after creating a dictionary.
    - **Keys Are Immutable**: Keys in a dictionary must be of an immutable data type, such as strings or numbers. Values can be of any data type.
    - **Fast Lookup**: Dictionaries are implemented as so-called hash tables, making key lookups and insertions very fast on average, even for large dictionaries.
    """
    )
    return


@app.cell
def _():
    empty_dict = {}  # Create an empty dictionary

    person = {
        "name": "Alice", 
        "age": 30
        } 

    print(person)
    type(person)
    return (person,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""To access the values of a dictionary you call them through their key:""")
    return


@app.cell
def _(person):
    name = person["name"]  # Access the value associated with the "name" key
    print(name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""As mentioned dictionaries are mutable.""")
    return


@app.cell
def _(person):
    print(person)

    person["age"] = 31  # Change the age value to 31
    print(person)
    return


@app.cell
def _(person):
    person["city"] = "Oldenburg"  # Add a new key-value pair
    print(person)
    return


@app.cell
def _(person):
    del person["age"]  # Remove the "age" key-value pair
    print(person)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It is possible to add dictionaries within a dictionary (or even lists), this process is called nesting.""")
    return


@app.cell
def _():
    # Nesting Dictionaries
    database = {
        "Name": "Alice",
        "Age": 31,
        "Address": {                                    # Values can be dictionaries
            "Street": "Haupstrasse 123",
            "City": "Oldenburg"},
        "Hobbies": ["Python", "Dancing", "Reading"]     # Values can be lists 
    }

    print(database)

    print(database["Address"])

    print(database["Address"]["Street"])

    print(database["Hobbies"])
    return (database,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""There are different methods you can extract data from a dictionary.""")
    return


@app.cell
def _(database):
    keys_list = database.keys()    # Get keys
    print(keys_list)

    values_list = database.values() # Get values
    print(values_list)

    items_list = database.items()   # Get key-value tuples
    print(items_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""According to the last method you extract the keys and values of a key-value pair, which in Python is called a _tuple_ which will be briefly explained in the following.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Tuples""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Tuples are Python sequences that hold data in pairs. They are useful when you want to store a collection of values that shouldn't be changed. They are widely used in cases where data integrity is important or when you need to return multiple values from a function. 

    Key characteristics:

    - **Ordered**: The items in a tuple have a defined order, and the order will not change.
    - **Immutable**: Unlike dictionaries and lists after creation, the items in a tuple cannot be changed.
    """
    )
    return


@app.cell
def _():
    # creating a tuple
    tuple1 = (1, 2, 3)
    print(tuple1)

    # the data can be assigned with or without paranthesis 
    tuple2 = 1, 2, 3  
    print(tuple2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Tuples are can heterogeneous, meaning they contain elements of different data types (integers, strings, lists, etc.).""")
    return


@app.cell
def _():
    mixed_tuple = (10, "Hello", 3.14, True)
    print(mixed_tuple)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Like with lists, the elements of a tuple can be accessed using their index:""")
    return


@app.cell
def _():
    my_tuple = (10, 20, 30)
    print(my_tuple[1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Sets""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Technically, sets are dictionaries without value data (keys only). This means they are collections of **unique** immutable data, since keys can only exist once.

    There are two types of sets in python:

    - **set** : Mutable set type,
    - **frozenset** : Immutable set type.

    Sets also use the curly brackets as their indicator symbols:
    """
    )
    return


@app.cell
def _():
    # create sets by curly brackets:
    food_order = {"Spam", "Eggs", "Sausage"}
    print(food_order)

    # this is the mutable version:
    food_order.add('Bacon')
    print(food_order)

    # However, adding an existing element does not change the set:
    food_order.add('Spam')
    print(food_order)
    return


@app.cell
def _():
    # Alternatively, we can create the set by using the constructor:
    order = set(["Spam", "Eggs", "Sausage"])
    print(order)
    return


@app.cell
def _():
    # The frozenset is created similarly:
    frozen_order = frozenset(["Spam", "Eggs", "Sausage"])
    print(frozen_order)
    return (frozen_order,)


@app.cell
def _(frozen_order):
    #...but we cannot add elements:
    frozen_order.add('Bacon')
    print(frozen_order)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The **set** has more functions that are related to its mutability. Try them on your own:

    - remove
    - pop
    - clear
    - discard

    The following functions on the other hand are shared by **set** and **frozenset** :
    """
    )
    return


@app.cell
def _():
    # create example sets:
    my_food = {"Spam", "Eggs"}
    your_food = {"Spam"}
    print("my food:",my_food)
    print("your food:",your_food)

    # Test if every element of first is in second set:
    print()
    print(my_food <= your_food)
    print(your_food <= my_food)
    print(your_food <= your_food)

    # Test if first is unequal subset of the second set:
    print()
    print(my_food < your_food)
    print(your_food < my_food)
    print(your_food < your_food)

    # Other way round:
    print()
    print(my_food > your_food)
    print(your_food > my_food)
    print(your_food > your_food)
    return my_food, your_food


@app.cell
def _(my_food, your_food):
    # return the intersection:
    print(my_food & your_food)
    return


@app.cell
def _(my_food, your_food):
    # return elements in first set, but not in the second:
    print(my_food - your_food)
    print(your_food - my_food)
    return


@app.cell
def _(my_food, your_food):
    # return elements in either first or in the second, but not both
    print(my_food ^ your_food)
    return


@app.cell
def _(my_food, your_food):
    # return the union of both sets:
    print(my_food | your_food)
    return


if __name__ == "__main__":
    app.run()
