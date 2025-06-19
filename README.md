# 🐍 Python Course

A self-paced interactive Python course with theory, practice, and autograded assignments. This repository contains structured theory chapters and autograded assignments for a beginner Python course. All teaching materials, exercises, and testing scripts are integrated into a website through an external Django-based Python Course Platform.

---

## 🚀 Features

- ✅ Interactive Theory with Jupyter Notebooks
- ✅ Assignments managed externally and autograded via a [Django-based platform](https://github.com/ET-PPRE/python-course-platform)
- ✅ Beginner-friendly progression through Python fundamentals

---

## 🏗️ Repository Structure

```
python-course/
├── README.md                          
├── book/                          # Jupyter notebooks for self-paced theory
│   ├── intro_to_python.ipnyb      # Chapter 1: Introduction to Python
│   ├── functions_loops.ipnyb      # Chapter 2: Functions, Looping and Classes
│   ├── data_structures.ipnyb      # Chapter 3: Data Structures, Dictionaries and Touples
│   ├── numpy.ipnyb                # Chapter 4: Numerical Python: Numpy
│   ├── pandas.ipnyb               # Chapter 5: DataFrames: Pandas
│   ├── matplotlib.ipnyb           # Chapter 6: Plotting: Matplotlib
│   ├── _config.yml                # Jupyter Book configuration settings
│   ├── _toc-dev.yml               # List of theory chapter to be included on the Jupyter Book in the development server
│   └── _toc-main.yml              # List of theory chapter to be included on the Jupyter Book in the production server

├── intro_to_python/               # Chapter 1 assignments - Autograded exercises organized per theory chapter
│   ├── hello_world                # Assignment 1.1
│   │   ├── description.md         # Instructions (Markdown)
│   │   ├── description.html       # Instructions (.html) this is displayed on the website 
│   │   ├── solution.py            # Sample solution (used for testing)
│   │   └── test_runner.py         # Autograder for this assignment
│   ├── area_circle_sphere         # Assignment 1.2
│   │   └── ...
├── functions_loops/               # Chapter 2 assignments
│   ├── check_even_odd/
│   └── ...
├── test_1/                        # Chapter Test - the assignment submision has a deadline
│   ├── check_even_odd/
│   └── ...
└── ...                            # Additional chapters and their assignments
├── toc-dev.yml                    # Structured list of chapters and their corresponding assignment, publishing date and submission deadline (if any) 
├── toc-main.yml                   # The same as above, this is used only on the production server, the one above on the development server
```

---

## 🌐 Platform Integration

The content in this repo is meant to be used alongside:

🔧 [Python Course Platform](https://github.com/ET-PPRE/python-course-platform).

This Django-based platform provides the backend with user management, submission handling, and autograder support. Here the theory section is converted in Jupyterbook format and the assignments are displayed for the users.

### 🔄 Assignment Integration

The autograding of the user sumbission is based on the `test_runner.py` code of each assignment and is also handled by the [Python Course Platform](https://github.com/ET-PPRE/python-course-platform) backend. This is done through the **Dynamic Cloning** of this repo to the website platform repository. The content and testing than is performed through the backend of the platform. 

---

## 🧪 Autograding

As mentioned, the assignments will be autograded through `test_runner.py`. Each assignment has such a script that inclused a `CodeChecker` that checks the submission of the students. In this class the maximal possible score of te assignment is stated (which should also be noted on the toc-dev.yml and toc-main.yml files) and the number of unit-tests which are implemented in the autograding.

The test of the autograding are implemented in within try-execpt statements. The general structure of `CodeChecker` is shown below.

```python
class CodeChecker:
    def __init__(self):

        self.total = 25       # Total possible score
        self.no_tests = 5     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
                        
            # Test 1: Check that the function 'matrix_operations' is defined
            try:
                assert ...

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED: {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check matrixes
            try:
                ...

                self.passed += 1
                print("Test 2 PASSED")    

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            ...

        # Collect number of points
        self.score = self.passed * self.total/self.no_tests        

        # Save output
        self.output = buffer.getvalue()
        return self.result  # Return results from the tests

    @property
    def result(self):
        return {
            "passed": self.passed,
            "total": self.total,
            "score": self.score,
            "output": self.output.strip(),
            #"errors": self.errors,
        }
```

The class will then return the number of tests passed by the user and the score they got for the assignment.

Within the `test_runner.py` this class is called, the results are collected and ready to be passed on the backend of the platform.