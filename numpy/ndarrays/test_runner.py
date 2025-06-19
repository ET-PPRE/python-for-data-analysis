import io
import contextlib
import numpy as np

class CodeChecker:
    def __init__(self):
        self.total = 15       # Total possible score
        self.no_tests = 3     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check that the function 'array_operations' is defined
            try:
                assert 'array_operations' in namespace, "Error: The function 'array_operations' is missing"

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Test sum 
            try:   
                expected_sum = np.sum(np.arange(1, 11))  # Expected sum is 55

                assert 'arr_sum' in namespace, "The variable 'arr_sum' is missing"
                arr_sum = namespace['arr_sum']
                assert (arr_sum - expected_sum) < 1e-3, f"Error: The expected sum is {expected_sum:.2f}, got {arr_sum:.2f}"
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Test mean
            try:
                expected_mean = np.mean(np.arange(1, 11))  # Expected mean is 5.5

                assert 'arr_mean' in namespace, "The variable 'arr_mean' is missing"
                arr_mean = namespace['arr_mean']
                assert (arr_mean - expected_mean) < 1e-3, f"Error: The expected mean is {expected_mean:.2f}, got {arr_mean:.2f}"
                
                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
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
            "output": self.output.strip(),
            #"errors": self.errors,
        }

if __name__ == "__main__":
    import json, io, contextlib, runpy
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        ns = runpy.run_path("user_submission.py")
    checker = CodeChecker()
    res = checker.check(ns)
    print(json.dumps(res))