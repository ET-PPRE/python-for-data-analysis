import io
import contextlib
import inspect

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
            
            # Test 1: Check function
            try:
                assert 'check_even_odd' in namespace, "Error: 'check_even_odd' is not defined."
                check_even_odd = namespace['check_even_odd']   # <-- get it first
                assert callable(check_even_odd), "Error: 'check_even_odd' exists but is not a function."
                check_even_odd = namespace['check_even_odd']
                
                sig = inspect.signature(check_even_odd)
                assert len(sig.parameters) == 1, f"Error: 'check_even_odd' must take exactly one parameter, found {len(sig.parameters)}."
                                
                self.passed += 1
                print("Test 1 PASSED ")
            
            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check for numbers_to_test
            try:
                assert 'numbers_to_test' in namespace, "Error: 'numbers_to_test' is not defined."
                numbers_to_test = namespace['numbers_to_test']

                assert isinstance(numbers_to_test, list), "Error: 'numbers_to_test' should be a list."
                
                assert len(numbers_to_test) == 5, "Error: `numbers_to_test` must have 5 elements."
                
                self.passed += 1
                print("Test 2 PASSED")
            
            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
            
            
            # Test 3: Check results
            try:
                assert check_even_odd(2) == "Even", "Error: 'check_even_odd' did not return 'Even' for input 2."
                assert check_even_odd(3) == "Odd", "Error: 'check_even_odd' did not return 'Odd' for input 3."
                
                self.passed += 1
                print("Test 3 PASSED")
            
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