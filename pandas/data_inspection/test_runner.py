import io
import contextlib
import pandas as pd

class CodeChecker:
    def __init__(self):
        self.total = 10       # Total possible score
        self.no_tests = 5     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        #self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
                        
            # Test 1: Check if the correct data is imported 
            try:
                assert 'power_data' in globals(), "Error: The variable 'power_data' is missing."
                power_data = namespace['power_data']
                assert isinstance(power_data, pd.DataFrame), "Error: 'power_data' is not a Pandas DataFrame."
                
                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if the data inspection is performed
            try:   
                assert 'data_inspection' in globals(), "Error: The variable 'data_inspection' is missing."
                data_inspection = namespace['data_inspection']
                assert isinstance(data_inspection, pd.DataFrame), "Error: 'data_inspection' is not a Pandas DataFrame."

                assert data_inspection.shape == (5, 8) or data_inspection.shape == (5, 7), "Error: The shape of data_inspection is incorrect"
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check if the missing values were inspected
            try:   
                assert 'missing_values' in globals(), "Error: The variable 'missing_values' is missing."
                missing_values = namespace['missing_values']
                assert missing_values.shape == (8,) or missing_values.shape == (7,), "[FAIL] 0/2 The shape of 'missing_values' is incorrect"

                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check if the missing values were filled using forward filling
            try:   
                assert 'clean_data' in globals(), "Error: The variable 'clean_data' is missing."
                clean_data = namespace['clean_data']
                assert isinstance(clean_data, pd.DataFrame), "Error: 'clean_data' is not a Pandas DataFrame."
                
                self.passed += 1
                print('Test 4 PASSED')  

            except Exception as e:
                msg = f"Test 4 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 5: Check if the missing values were properly filled 
            try:   
                assert clean_data.isnull().sum().sum() == 0, "Error: There are still missing values in the DataFrame."
                
                self.passed += 1
                print('Test 5 PASSED')  

            except Exception as e:
                msg = f"Test 5 FAILED {str(e)}"
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