import io
import os
import contextlib
import matplotlib.pyplot as plt
from plotchecker import LinePlotChecker

class CodeChecker:
    def __init__(self):
        self.total = 5        # Total possible score
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
                        
            # Test 1: Check if x and y variables are defined
            try:
                assert 'x' in globals() and 'y' in globals(), "Error: Variables 'x' and 'y' must be defined."
                x = namespace['x']
                y = namespace['y']

                assert len(x) == len(y), "Error: 'x' and 'y' must have the same length."

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if fig and ax exist
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

            # Test 3: Validate the plot properties
            try:   
                pc = LinePlotChecker(ax)
                pc.assert_num_lines(1)

                line = ax.lines[0]
                assert line.get_color() == 'red', "Error: The line color is not red."
                assert ax.get_xlabel() != "", "Error: The plot does not have a label in the x-axis"
                assert ax.get_ylabel() != "", "Error: The plot does not have a label in the y-axis"

                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            
            # Test 4: Check if the plot is saved correctly
            try:   
                assert os.path.exists("sales_plot.png"), "Error: The plot file 'sales_plot.png' was not found."

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