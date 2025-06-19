import io
import os
import contextlib
import pandas as pd
import matplotlib.pyplot as plt
from plotchecker import LinePlotChecker

class CodeChecker:
    def __init__(self):
        self.total = 10        # Total possible score
        self.no_tests = 4     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        #self.output = ""     # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check if 'ws100' is defined and has the correct shape
            try:
                assert 'ws100' in globals(), "Error: Variable 'ws100' must be defined."
                ws100 = namespace['ws100']
                assert ws100.shape == (17520,), "Error: The shape of ws100 is incorrect."

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if the plot exists
            try:   
                assert 'fig' in globals() and 'ax' in globals(), "Error: Figure and axes must be defined."
                fig = namespace['fig']
                ax = namespace['ax']
                assert isinstance(fig, plt.Figure), "Error: 'fig' should be a matplotlib Figure object."

                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Validate the data content of the plot
            try:   
                data_test = pd.read_csv("measurements_2009.csv", delimiter=",")
                ws100_test = data_test['WS-100']
                ws100_test_reshaped = ws100_test.values.reshape(1, -1)

                # Check if the plot shows correct values (plot must contain 'WS-100' values)
                pc = LinePlotChecker(ax)
                pc.assert_y_data_equal(ws100_test_reshaped)

                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            
            # Test 4: Check if the properties of the plot 
            try:   
                pc = LinePlotChecker(ax)

                # Checking if the title and axis labels are created
                assert ax.get_title()  != "", "Error: The plot does not contain a title"
                assert ax.get_xlabel()  != "", "Error: The plot does not have a bel in the x-axis"
                assert ax.get_ylabel()  != "", "Error: The plot does not have a bel in the y-axis"

                self.passed += 1
                print('Test 4 PASSED')  

            except Exception as e:
                msg = f"Test 4 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)


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
            #"output": self.output.strip(),
            "errors": self.errors,
        }

if __name__ == "__main__":
    import json, io, contextlib, runpy
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        ns = runpy.run_path("user_submission.py")
    checker = CodeChecker()
    res = checker.check(ns)
    print(json.dumps(res))