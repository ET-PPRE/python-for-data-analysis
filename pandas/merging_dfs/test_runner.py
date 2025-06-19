import io
import contextlib

class CodeChecker:
    def __init__(self):
        self.total = 10       # Total possible score
        self.no_tests = 2     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        #self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check if the expected variables and dataframes have been defined
            try:
                assert 'A' in globals(), "Error: The DataFrame 'A' is not defined."
                A = namespace['A']

                assert 'B' in globals(), "Error: The DataFrame 'B' is not defined."
                B = namespace['B']

                assert 'merged_df1' in globals(), "Error: The DataFrame 'merged_df1' is not defined."
                merged_df1 = namespace['merged_df1']

                assert 'average_salary' in globals(), "[Fail]: Score 0/5 : 'average_salary' is not defined."
                average_salary = namespace['average_salary']

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if the calculation for 'average_salary' is correct
            try:   
                expected_avg_salary = 75000

                assert abs(average_salary - expected_avg_salary) < 1e-2, f"Error: Incorrect average salary calculation. Expected {expected_avg_salary}, got {average_salary}"
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
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