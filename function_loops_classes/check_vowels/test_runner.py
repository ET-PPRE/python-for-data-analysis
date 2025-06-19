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
            
            # Test 1: # Check if the function is defined
            try:
                assert 'contains_only_vowels' in namespace, "Error: 'contains_only_vowels' function is missing."
                contains_only_vowels = namespace['contains_only_vowels']
                
                self.passed +=1
                print("Test 1 PASSED")

            except Exception as e:
                msg = f"Test 1 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            
            # Test 2: Check if the correct list name is used

            # Predefined correct test strings (must match exactly)
            correct_list_name = "test_strings"
            correct_test_strings = ["eiou", "hello", "AaEeIiOoUu"]
            expected_results = ["Only Vowels", "Not Only Vowels", "Only Vowels"]

            try:
                assert correct_list_name in namespace, f"Error: The list must be named exactly '{correct_list_name}'."
                student_test_strings = namespace.get(correct_list_name, None)

                # Check if the list values match exactly
                assert student_test_strings == correct_test_strings, \
                    f"Error: You must use the exact predefined test strings {correct_test_strings}. Your test cases were: {student_test_strings}"
                
                self.passed +=1
                print("Test 2 PASSED")
            
            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 3: Check the output for each test string if the list is correct
            all_passed = True

            for i, test_string in enumerate(correct_test_strings):
                try:
                    result = contains_only_vowels(test_string)
                    expected_output = expected_results[i]
                    assert result == expected_output, (
                        f"Error: Incorrect output for '{test_string}': "
                        f"Expected '{expected_output}', but got '{result}'."
                    )
                except Exception as e:
                    msg = f"Test 3 FAILED: {str(e)}"
                    print(msg)
                    self.errors.append(msg)
                    all_passed = False  # mark test 3 as failed

            if all_passed:
                self.passed += 1
                print("Test 3 PASSED")

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