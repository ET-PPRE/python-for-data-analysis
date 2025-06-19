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

            # Test 1: Check if 'vectors' is defined
            try:
                assert 'vectors' in namespace, "Error: The 'vectors' list is not defined. Did you leave the cell empty?"
                vectors = namespace['vectors']
                assert isinstance(vectors, list), "Error: Vectors should be a list."
                
                # Check that all elements are lists or tuples
                assert all(isinstance(v, (list, tuple)) for v in vectors), \
                    f"Test 1 FAILED: Error: All elements of 'vectors' should be lists or tuples, but found: {[type(v) for v in vectors]}"

                # Ensure each vector has 3 components
                for v in vectors:
                    assert len(v) == 3, f"Error: Each vector should have exactly 3 components, but found: {v} with length {len(v)}"
                
                self.passed += 1
                print("Test 1 PASSED")
                
            except Exception as e:
                msg = f"Test 1 FAILED : {str(e)}"
                print(msg)
                self.errors.append(msg)

            # Test 2: Test the vmag function
            try:    
                vmag = namespace['vmag']   
                # Test function with predefined vectors and their expected magnitudes
                assert math.isclose(vmag([23, 11, 73]), 77.32, rel_tol=1e-2)
                assert math.isclose(vmag([0, 12, -74]), 74.97, rel_tol=1e-2)
                assert math.isclose(vmag([-28, -12, -8]), 31.50, rel_tol=1e-2)
            
                self.passed += 1
                print("Test 2 PASSED")

            except Exception as e:
                msg = f"Test 2 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)


            # Function to compare two vectors element-wise
            def compare_vectors(vec1, vec2, minmax):
                assert len(vec1) == len(vec2), "Error: Vectors must have the same length."
                for a, b in zip(vec1, vec2):
                    assert a == b, f"Error: {minmax} vector is not correct."


            # Test 3: Check min value
            try:    
                magnitudes_test = [vmag(v) for v in vectors]
                min_V_index_t = magnitudes_test.index(min(magnitudes_test)) 
                min_vector_test = vectors[min_V_index_t]

                # Compare min vector
                min_vector = namespace['min_vector']
                compare_vectors(min_vector, min_vector_test, "Min")

                self.passed += 1
                print("Test 3 PASSED")
                
            except Exception as e:
                msg = f"Test 3 FAILED {str(e)}"
                print(msg)
                self.errors.append(msg)
            
            # Test 4: Check max value
            try: 
                max_V_index_t = magnitudes_test.index(max(magnitudes_test))
                max_vector_test = vectors[max_V_index_t]

                # Compare max vector
                max_vector = namespace['max_vector']
                compare_vectors(max_vector, max_vector_test, "Max")

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