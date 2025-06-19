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

            # Constants 
            D = 154.0
            u0 = 9.0
            ct = 0.763
            k = 0.02
            beta = (1 + (1 - ct)**0.5) / (2 * (1 - ct)**0.5)
                        
            # Test 1: Check for required variables and functions 
            try:
                assert 'recovery_distance' in namespace, "Error: Variable 'recovery_distance' is not defined."
                assert callable(sigma), "Error: Function 'sigma(x)' is not defined or not callable."
                assert callable(u), "Error: Function 'u(x)' is not defined or not callable."

                self.passed += 1
                print('Test 1 PASSED')    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
            
            sigma = namespace['sigma']
            u = namespace['u']

            # Test 2: Test sigma(x)
            try:   
                x_test = 100
                student_sigma = sigma(x_test)
                expected_sigma = k * x_test + 0.25 * (beta**0.5) * D
                assert (student_sigma - expected_sigma) < 1e-3, f"Error: sigma({x_test}) expected {expected_sigma:.4f}, got {student_sigma:.4f}"
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
                
            # Test 3: Test u(x)
            try:
                expected_u = u0 * (1 - ct / 8 * (D / expected_sigma)**2)**0.5
                student_u = u(x_test)
                assert abs(student_u - expected_u) < 1e-3, f"Error: u({x_test}) expected {expected_u:.4f}, got {student_u:.4f}"
                
                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check recovery distance
            try:
                expected_distance = 20213
                recovery_distance = namespace['recovery_distance']
                assert recovery_distance == expected_distance, f"Error: Expected recovery_distance = {expected_distance}, got {recovery_distance}"
                
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