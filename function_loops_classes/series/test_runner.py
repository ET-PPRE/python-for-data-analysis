import io
import contextlib

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
            
            # Test 1: Check if the geometric series in explicit function is defined
            try:
                assert 'geometric_series_explicit' in namespace, "Error: Function 'geometric_series_explicit' is missing"
                geometric_series_explicit = namespace['geometric_series_explicit']

                self.passed += 1
                print("Test 1 PASSED")                

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
            
            # Test 2: Check if the closed geometric series function is defined
            try:
                assert 'geometric_series_closed' in namespace, "Error: Function 'geometric_series_closed' is missing"
                geometric_series_closed = namespace['geometric_series_closed']
                
                self.passed += 1
                print("Test 2 PASSED")     

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check if predefined x_values list exists and is correct
            try:
                assert 'x_values' in namespace, "Error: Variable 'x_values' is missing"
                x_values = namespace['x_values']
                correct_x_values = [0.1, 0.5, 0.9, 0.99]

                assert x_values == correct_x_values, f"Error: 'x_values' should be {correct_x_values}, got {x_values}"
                
                self.passed += 1
                print("Test 3 PASSED")                

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
            
            # Test 4: Check if functions give approximately the same results
            try:
                test_values = [(0.1, 10), (0.5, 20), (0.9, 30), (0.99, 40)]
                for x, N in test_values:
                    explicit = geometric_series_explicit(x, N)
                    closed = geometric_series_closed(x, N)
                    assert abs(explicit - closed) < 1e-6, f"Error: Mismatch for x={x}, N={N}: Explicit={explicit}, Closed={closed}"
                
                self.passed += 1
                print("Test 4 PASSED")
            
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