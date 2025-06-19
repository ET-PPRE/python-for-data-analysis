import ast
import re
import io
import contextlib

class CodeChecker:
    def __init__(self):

        self.total = 3       # Total possible score
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
            import importlib
            import user_submission 
            importlib.reload(user_submission)
            actual_output = buffer.getvalue().strip().splitlines()
            buffer.truncate(0)
            buffer.seek(0)
            
            # Test 1: Check that there are exactly three print statements in the source code
            try:
                with open("user_submission.py", encoding="utf-8") as f:
                    source_code = f.read()
                tree = ast.parse(source_code)

                # Count print() function calls
                print_calls = [
                    node for node in ast.walk(tree)
                    if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "print"
                ]
                print_count = len(print_calls)
            except Exception as e:
                source_code = ""

            try:
                assert print_count == 3, f"Error: Expected 3 print statements, found {print_count}."
                self.passed += 1
                print("Test 1 PASSED")
            
            except AssertionError as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check that the printed output is correct 
            expected_text = [
                "Hello, User!",
                "We are practicing.",
                "This is test = 1.00."
            ]

            try:
                for got, exp in zip(actual_output, expected_text):
                    assert got.strip() == exp, f"Error: Expected: '{exp}', got: '{got}'"
                
                self.passed += 1
                print("Test 2 PASSED")  
            
            except AssertionError as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check that test=1
            try:
                assert 'test' in namespace, "Error: Variable 'test' is missing"
                test = namespace['test']

                assert test==1, f"Error: Incorrect value assigned to the variable 'test'. Got: {test}, expected: 1."
                
                self.passed += 1
                print("Test 3 PASSED")
            
            except AssertionError as e:
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