import math
import io
import contextlib

class CodeChecker:
    def __init__(self):
        self.total = 15       # Total possible score
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

            # Test 1: Check if student_grades is defined 
            try:
                assert 'student_grades' in namespace, "Error: The 'student_grades' dictionary is not defined."
                student_grades = namespace['student_grades']
                assert isinstance(student_grades, dict), "Error: student_grades should be a dictionary."

                # Ensure that the names are strings and each student has three exams
                for k, v in student_grades.items():
                    assert isinstance(k, str), "Error: Student names must be strings."
                    assert isinstance(v, list), f"Error: The value for {k} must be a list."
                    assert len(v) == 3, f"Error: Each student should have three exam scores, but found {len(v)} for {k}."
                    assert all(isinstance(x, int) for x in v), f"Error: All scores for {k} should be integers."
                
                self.passed += 1
                print("Test 1 PASSED")
                
            except Exception as e:
                msg = f"Test 1 FAILED : {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Test the avg_grade function
            try:    
                assert 'avg_grade' in namespace, "Error: The function 'avg_grade' is not defined."
                avg_grade = namespace['avg_grade']
                assert callable(avg_grade), "Error: 'avg_grade' must be a function."

                # Test dictionary 
                test_dict = {"Aria": [90, 80, 70], "Eva": [100, 100, 90], "Fynn": [60, 70, 80]}
                expected_averages = {
                    "Aria": sum([90,80,70]) / 3,
                    "Eva": sum([100,100,90]) / 3,
                    "Fynn": sum([60,70,80]) / 3
                }
                for k, v in test_dict.items():
                    got = avg_grade(v)
                    expect = expected_averages[k]
                    assert abs(got-expect)<1e-6, f"Error: avg_grade([scores of {k}]) should be {expect}, got {got}"
            
                self.passed += 1
                print("Test 2 PASSED")

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check top_student 
            try:
                assert 'top_student' in namespace, "Error: The variable'top_student' is not defined."    
                top_student = namespace['top_student']

                expected_top = max(student_grades, key=lambda k: avg_grade(student_grades[k]))

                assert top_student == expected_top, f"Error: 'top_student' should be {expected_top}, got {top_student}"

                self.passed += 1
                print("Test 3 PASSED")
                
            except Exception as e:
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