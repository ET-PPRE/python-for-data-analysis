import io
import contextlib
import pandas as pd

class CodeChecker:
    def __init__(self):
        self.total = 20       # Total possible score
        self.no_tests = 4     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        #self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check if the expected dataframes have been defined
            try:
                assert 'df' in globals(), "Error: The DataFrame 'df' is not defined."
                df = namespace['df']

                assert 'eligible_for_promotion' in globals(), "Error: The DataFrame 'eligible_for_promotion' is not defined."
                eligible_for_promotion = namespace['eligible_for_promotion']

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if eligible_for_promotion and df are DataFrames
            try:   
                assert isinstance(df, pd.DataFrame), f"Error: 'df' should be a pandas DataFrame."
                assert isinstance(eligible_for_promotion, pd.DataFrame), f"Error: 'eligible_for_promotion' should be a pandas DataFrame."
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check if the filtered employees are correct
            try:   
                expected_columns = ['Employee_ID', 'Name', 'Age', 'Performance_Score']
                assert all(col in eligible_for_promotion.columns for col in expected_columns), "Error: Missing one or more required columns."

                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check if correct columns exist in 'eligible_for_promotion'
            try:   
                expected_ids = [2, 3]  # Based on criteria: Age > 30 and Performance_Score >= 70
                actual_ids = eligible_for_promotion['Employee_ID'].tolist()
                assert actual_ids == expected_ids, f"Errir: Incorrect filtered employees. Expected IDs: {expected_ids}, but got {actual_ids}"
                
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