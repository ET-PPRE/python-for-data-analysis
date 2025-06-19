import io
import contextlib
import numpy as np

class CodeChecker:
    def __init__(self):

        self.total = 25       # Total possible score
        self.no_tests = 6     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check that the function 'matrix_operations' is defined
            try:
                assert 'matrix_operations' in namespace, "Error: The function 'matrix_operations' is missing."

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED: {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check matrixes
            try:
                matrix_operations = namespace['matrix_operations']
                A, B, C, D = matrix_operations()

                assert isinstance(A, np.ndarray), "Error: Matrix A is not a numpy array"
                assert isinstance(B, np.ndarray), "Error: Matrix B is not a numpy array"
                assert isinstance(C, np.ndarray), "Error: Matrix C is not a numpy array"
                assert isinstance(D, np.ndarray), "Error: Matrix D is not a numpy array"

                self.passed += 1
                print("Test 2 PASSED")    

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check matrixes shapes
            try:   
                assert A.shape == (3, 2), f"Error: Matrix A shape incorrect: {A.shape}"
                assert B.shape == (2, 3), f"Error: Matrix B shape incorrect: {B.shape}"
                assert C.shape == (3, 3), f"Error: Matrix C shape incorrect: {C.shape}"
                assert D.shape == (3, 3), f"Error: Matrix D shape incorrect: {D.shape}"
                
                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check that C = A dot B
            try:
                expected_C = np.dot(A, B)
                assert np.array_equal(C, expected_C), "Error: Matrix C (A*B) calculation is wrong."

                self.passed += 1
                print('Test 4 PASSED')  

            except Exception as e:
                msg = f"Test 4 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 5: Check that D is transpose of C
            try:
                expected_D = expected_C.T
                assert np.array_equal(D, expected_D), "Error: Matrix D is not the transpose of C."

                self.passed += 1
                print('Test 5 PASSED')  

            except Exception as e:
                msg = f"Test 5 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 6: Check if the function prints the matrixes 
            try:
                captured_output = io.StringIO()
                output = captured_output.getvalue()
                assert "Matrix A:" in output, "Error: Printout missing 'Matrix A:'"
                assert "Matrix B:" in output, "Error: Printout missing 'Matrix B:'"
                assert "Matrix C" in output, "Error: Printout missing 'Matrix C'"
                assert "Matrix D" in output, "Error: Printout missing 'Matrix D'"

                self.passed += 1
                print('Test 6 PASSED')  

            except Exception as e:
                msg = f"Test 6 FAILED {str(e)}"
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