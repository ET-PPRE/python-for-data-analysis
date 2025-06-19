import math
import io
import contextlib

class CodeChecker:
    def __init__(self):

        self.total = 10       # Total possible score
        self.no_tests = 2     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):

            # Test 1: Check 'a_circle'
            try:
                assert 'a_circle' in namespace, "Error: Variable 'a_circle' is missing"
                a_circle = namespace['a_circle']

                assert math.isclose(a_circle, 78.5, rel_tol=0.1), \
                    f"Error: Incorrect area for the circle: {a_circle}. Expected ≈ 78.5 m²."
                
                self.passed += 1
                print("Test 1 PASSED")
                
            
            except AssertionError as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check 'a_sphere'
            try:
                assert 'a_sphere' in namespace, "Error: Variable 'a_sphere' is missing"
                a_sphere = namespace['a_sphere']

                assert math.isclose(a_sphere, 314, rel_tol=0.1), \
                    f"Error: Incorrect area for the sphere: {a_sphere}. Expected ≈ 314 m²."
                
                self.passed += 1
                print("Test 2 PASSED")
            
            except AssertionError as e:
                msg = f"Test 2 FAILED {str(e)}"
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