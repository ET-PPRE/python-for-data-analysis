import io
import contextlib
import numpy as np

class CodeChecker:
    def __init__(self):
        
        self.total = 15       # Total possible score
        self.no_tests = 4     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check that the function 'reshape_array' is defined
            try:
                assert 'reshape_array' in namespace, "Error: The function 'reshape_array' is missing"

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check the original array
            try:
                reshape_array = namespace['reshape_array']
                arr, reshaped_arr = reshape_array()

                expected_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                assert np.array_equal(arr, expected_arr), f"Error: Original array is incorrect, expected sum is {expected_arr}, got {arr}"

                self.passed += 1
                print("Test 2 PASSED")    

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check that the reshaped array has the correct shape
            try:   
                assert reshaped_arr.shape == (3, 4), f"Error: Reshaped array does not have shape (3, 4), got {reshaped_arr.shape}"
                
                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check that the reshape didn't change the total number of elements
            try:
                assert arr.size == reshaped_arr.size, f"Error: Number of elements changed after reshaping. Expected: {arr.size} but got: {reshaped_arr.size}"
                
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