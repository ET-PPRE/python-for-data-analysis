import io
import contextlib
import numpy as np

class CodeChecker:
    def __init__(self):
        self.total = 45       # Total possible score
        self.no_tests = 9     # Total number of test within the autograding function
        self.passed = 0       # Student's passed tests
        self.score =  0       # Student's earned points
        self.errors = []      # Collect error messages
        self.output = ""      # Captured stdout

    def check(self, namespace = None):
        
        if namespace is None:
            namespace = globals()
            
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            # Part A      
            # Test 1: Check if 'irradiance_data' is imported
            try:
                assert 'irradiance_data' in namespace, "Error: 'irradiance_data' is not defined"
                irradiance_data = namespace['irradiance_data']

                self.passed += 1
                print("Test 1 PASSED")    

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Check if 'irradiance_data' is a NumPy array
            try:   
                assert isinstance(irradiance_data, np.ndarray), f"Error: irradiance_data is not a NumPy array but a {type(irradiance_data).__name__}"
                
                self.passed += 1
                print('Test 2 PASSED')  

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check the shape of the NumPy array
            try:
                assert irradiance_data.shape == (24, 7), f"Error: The shape of the NumPy array is incorrect. Expected shape is (24, 7), got {irradiance_data.shape}." 
                
                self.passed += 1
                print('Test 3 PASSED')  

            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Part B
            # Test 4: Check if the variable 'average_irradiance' exists
            try:
                assert 'average_irradiance' in namespace, "Error: 'average_irradiance' is not defined"
                average_irradiance = namespace['average_irradiance']
                
                self.passed += 1
                print("Test 4 PASSED")  

            except Exception as e:
                msg = f"Test 4 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 5: Check if average solar irradiance per day is calculated correctly
            try:

                irradiance_test = np.genfromtxt('solar_irradiance.txt', skip_header=1, usecols=range(1, 8))
                expected_average_irradiance = np.mean(irradiance_test, axis=0)

                assert np.allclose(average_irradiance, expected_average_irradiance, rtol=1e-2), f"Error: Average solar irradiance per day is incorrect: \nExpected: \n{expected_average_irradiance}\n"
                f"Calculated: \n{average_irradiance} W/m²"

                self.passed += 1
                print("Test 5 PASSED")  

            except Exception as e:
                msg = f"Test 5 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Part C
            # Test 6: Check if the variable 'daily_energy_output_pv' exists 
            try:
                assert 'daily_energy_output_pv' in namespace, "Error: The variable'daily_energy_output_pv' is not defined"
                daily_energy_output_pv = namespace['daily_energy_output_pv']

                self.passed += 1
                print("Test 6 PASSED")  

            except Exception as e:
                msg = f"Test 6 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 7: Check if the variable 'daily_energy_output_pv' is a numpy array
            try:
                assert isinstance(daily_energy_output_pv, np.ndarray), f"Error: daily_energy_output_pv is not a NumPy array but a {type(daily_energy_output_pv).__name__}."
                
                self.passed += 1
                print("Test 7 PASSED")  

            except Exception as e:
                msg = f"Test 7 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 8: Check the shape of 'daily_energy_output_pv' 
            try:
                assert daily_energy_output_pv.shape == (7,), f"Error: daily_energy_output_pv does not represent 7 days of a week. Expected shape is (7,) but got {daily_energy_output_pv.shape}."
                
                self.passed += 1
                print("Test 8 PASSED")  

            except Exception as e:
                msg = f"Test 8 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 9: Check if the daily energy output is calculated correctly
            try:
                
                # Constants
                area_of_module = 1.8  # m²
                efficiency = 0.2
                number_of_modules = 10000
                t = 24  # hours/day

                # Calculate expected daily energy output
                expected_energy_output_pv = ((average_irradiance * area_of_module * efficiency) / 1e6 * number_of_modules * t)

                assert np.allclose(daily_energy_output_pv, expected_energy_output_pv, rtol=1e-2), f"Error: The daily energy output values are incorrect. \nExpected: {expected_energy_output_pv} \n"
                f"Calculated: {daily_energy_output_pv}"
    
                self.earned += 1
                print("Test 9 PASSED")  

            except Exception as e:
                msg = f"Test 9 FAILED {str(e)}"
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
        try:
            ns = runpy.run_path("user_submission.py")
            print("[DEBUG] User namespace keys:", list(ns.keys()))
        except Exception as e:
            print("[DEBUG] Failed to run user code:", e)
        # ns = runpy.run_path("user_submission.py")
    checker = CodeChecker()
    res = checker.check(ns)
    print(json.dumps(res))