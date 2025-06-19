import math
import io
import contextlib

class CodeChecker:
    def __init__(self):
        self.total = 20       # Total possible score
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

            # Test 1: Check if panel_output is defined and correct
            try:
                assert 'panel_output' in namespace, "Error: 'panel_output' is not defined."
                panel_output = namespace['panel_output']
                assert isinstance(panel_output, dict), "Error: panel_output must be a dictionary."

                # Ensure that the content of the dictionary is correct
                for panel in ['Panel1', 'Panel2', 'Panel3']:
                    assert panel in panel_output, f"Error: {panel} missing from panel_output."
                    vals = panel_output[panel]
                    assert isinstance(vals, list), f"Error: {panel} value must be a list."
                    assert len(vals) == 7, f"Error: {panel} must have 7 daily outputs"
                    assert all(isinstance(x, int) for x in vals), f"Error: all values in {panel} must be integers."
                
                self.passed += 1
                print("Test 1 PASSED")
                
            except Exception as e:
                msg = f"Test 1 FAILED : {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check panel_output_cleaned
            try:    
                assert 'panel_output_cleaned' in namespace, "Error: 'panel_output_cleaned' is not defined."
                cleaned = namespace['panel_output_cleaned']
                assert isinstance(cleaned, dict), "Error: panel_output_cleaned must be a dictionary."

                # Check if the negative values are replaced in Panel2
                for orig, new in zip(panel_output['Panel2'], cleaned['Panel2']):
                    if orig < 0:
                        assert new == 0, f"Error: Value {orig} in Panel2 not replaced by 0."
                    else:
                        assert new == orig, f"Error: Value {orig} in Panel2 was incorrectly changed."
            
                self.passed += 1
                print("Test 2 PASSED")

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check weekly_production function
            try:
                assert 'weekly_production' in namespace, "Error: The function 'weekly_production' is not defined."
                fn = namespace['weekly_production']
                assert callable(fn), "Error: 'weekly_production' must be a function."

                # Test function
                test_values = [10, 20, 30, 0, 25, 10, 5]
                try:
                    res = fn(test_values)
                except Exception as e:
                    raise AssertionError(f"Error: The test for 'weekly_production' raised an exception: {str(e)}. The argument must be a list.")
                assert isinstance(res, (int, float)), "Error: 'weekly_production' must return a value."

                assert abs(res - 100) < 1e-8, f"Error: 'weekly_production' gives {res} for {test_values}, expected 100."

                self.passed += 1
                print("Test 3 PASSED")
                
            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 4: Check the calculation for most_produced
            try:
                assert isinstance(res, (int, float)), "Error: 'weekly_production' must return a value."
                assert 'most_produced' in namespace, "Error: The variable 'most_produced' is not defined."

                most_produced = namespace['most_produced']

                # Find which should be the answer
                try:
                    panel_sums = {p: fn(cleaned[p]) for p in cleaned}
                except Exception as e:
                    raise AssertionError(f"Error: The test for 'weekly_production' raised an exception: {str(e)}. The argument must be a list.")
                
                expected_best = max(panel_sums, key=lambda k: panel_sums[k])
                assert most_produced == expected_best, f"Error: most_produced should be {expected_best}, got {most_produced}"

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