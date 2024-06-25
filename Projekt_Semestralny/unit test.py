'''#1. Write a Python unit test program to check if a given number is prime or not.
import unittest

# Define a function 'is_prime' to check if a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.TestCase'.
class PrimeNumberTestCase(unittest.TestCase):
    # Define a test method 'test_prime_numbers' to test prime numbers.
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        # You can use the alternative 'prime_numbers' list by uncommenting it.
        # prime_numbers = [2, 3, 4, 8, 11, 13, 17, 19, 23, 30, 31]
        print("Prime numbers:", prime_numbers)
        # Iterate through prime numbers and assert that they are recognized as prime.
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f"{number} is not recognized as a prime number")

    # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        # You can use the alternative 'non_prime_numbers' list by uncommenting it.
        # non_prime_numbers = [4, 6, 8, 9, 11, 12, 14, 17, 16, 18, 20]
        print("Non-prime numbers:", non_prime_numbers)
        # Iterate through non-prime numbers and assert that they are not recognized as prime.
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number), f"{number} is incorrectly recognized as a prime number")

# Check if the script is run as the main program.
if __name__ == '__main__':
    unittest.main()

#2. Write a Python unit test program to check if a list is sorted in ascending order.
import unittest

# Define a function 'is_sorted_ascending' to check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    # Check if all elements at index i are less than or equal to elements at index i+1.
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Define a test case class 'TestSortedAscending' that inherits from 'unittest.TestCase'.
class TestSortedAscending(unittest.TestCase):
    # Define a test method 'test_sorted_list' to test a sorted list.
    def test_sorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [5, 7, 2, 8, 1, 9]
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Sorted list: ", lst)
        # Assert that the list is sorted in ascending order.
        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")

    # Define a test method 'test_unsorted_list' to test an unsorted list.
    def test_unsorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [1, 2, 3]
        lst = [5, 7, 2, 8, 1, 9]
        print("Unsorted list: ", lst)
        # Assert that the list is not sorted in ascending order.
        self.assertFalse(is_sorted_ascending(lst), "The list is sorted in ascending order")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#3. Write a Python unit test program that checks if two lists are equal.
import unittest

# Define a function 'lists_are_equal' to check if two lists are equal.
def lists_are_equal(nums1, nums2):
    return nums1 == nums2

# Define a test case class 'TestListsEquality' that inherits from 'unittest.TestCase'.
class TestListsEquality(unittest.TestCase):
    # Define a test method 'test_equal_lists' to test equal lists.
    def test_equal_lists(self):
        # Define two lists 'nums1' and 'nums2' for testing equal or unequal lists.
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        # Uncomment one pair of 'nums1' and 'nums2' for testing equal or unequal lists.
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 50]
        print("\nEqual list test:\n", nums1, "\n", nums2)
        # Assert that the lists are equal.
        self.assertTrue(lists_are_equal(nums1, nums2), "The lists are not equal")

    # Define a test method 'test_unequal_lists' to test unequal lists.
    def test_unequal_lists(self):
        # Define two lists 'nums1' and 'nums2' for testing equal or unequal lists.
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        # Uncomment one pair of 'nums1' and 'nums2' for testing equal or unequal lists.
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 40]
        print("\nUnequal list test:\n", nums1, "\n", nums2)
        # Assert that the lists are not equal.
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#4. Write a  Python  unit test program to check if a string is a palindrome.
import unittest
# Define a function 'is_palindrome' to check if a string is a palindrome.
def is_palindrome(string):
    return string == string[::-1]
# Define a test case class 'TestPalindrome' that inherits from 'unittest.TestCase'.
class TestPalindrome(unittest.TestCase):
    # Define a test method 'test_palindrome_string' to test palindrome strings.
    def test_palindrome_string(self):
        # Define a string 'palindrome' for testing palindrome or non-palindrome strings.
        #palindrome = "madam"
        palindrome = "hello"
        print("Test palindrome:", palindrome)
        # Assert that the string is a palindrome.
        self.assertTrue(is_palindrome(palindrome), "The string is not a palindrome")

    # Define a test method 'test_non_palindrome_string' to test non-palindrome strings.
    def test_non_palindrome_string(self):
        # Define a string 'non_palindrome' for testing palindrome or non-palindrome strings.
        #non_palindrome = "hello"
        non_palindrome = "madam"
        print("Test non palindrome:", non_palindrome)
        # Assert that the string is not a palindrome.
        self.assertFalse(is_palindrome(non_palindrome), "The string is a palindrome")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#5. Write a  Python  unit test program to check if a file exists in a specified directory.
import os
import unittest

# Define a function 'file_exists' to check if a file exists in a specified directory.
def file_exists(directory, filename):
    # Create the full file path by joining the directory and filename.
    file_path = os.path.join(directory, filename)
    # Check if the file exists at the specified path.
    return os.path.exists(file_path)

# Define a test case class 'TestFileExists' that inherits from 'unittest.TestCase'.
class TestFileExists(unittest.TestCase):
    # Define a test method 'test_existing_file' to test the existence of an existing file.
    def test_existing_file(self):
        # Define the directory and filename for an existing file.
        directory = '/path/txt'
        filename = 'test1.txt'
        # Assert that the file exists in the specified directory.
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    # Define a test method 'test_nonexistent_file' to test the non-existence of a non-existing file.
    def test_nonexistent_file(self):
        # Define the directory and filename for a non-existing file.
        directory = '/path/txt'
        filename = 'test2.txt'
        # Assert that the file does not exist in the specified directory.
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#6. Write a Python unit test that checks if a function handles floating-point calculations accurately.
import unittest

# Define a test case class 'TestFloatingPointCalculations' that inherits from 'unittest.TestCase'.
class TestFloatingPointCalculations(unittest.TestCase):
    # Define a test method 'test_addition' to test floating-point addition.
    def test_addition(self):
        # Perform the addition operation.
        result = 0.3 + 0.5
        # Assert that the result is approximately equal to 0.8 within 6 decimal places.
        self.assertAlmostEqual(result, 0.8, places=6)

    # Define a test method 'test_multiplication' to test floating-point multiplication.
    def test_multiplication(self):
        # Perform the multiplication operation.
        result = 0.3 * 0.5
        # Assert that the result is approximately equal to 0.15 within 6 decimal places.
        self.assertAlmostEqual(result, 0.15, places=6)

    # Define a test method 'test_division' to test floating-point division.
    def test_division(self):
        # Perform the division operation.
        result = 0.7 / 0.3
        # Assert that the result is approximately equal to 2.333333 within 6 decimal places.
        self.assertAlmostEqual(result, 2.333333, places=6)

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#7. Write a Python unit test program to check if a function handles multi-threading correctly.
import unittest
import threading

# Define a function 'perform_task' that simulates some computational task.
def perform_task():
    # Initialize a result variable.
    result = 0
    # Simulate a task by summing numbers from 1 to 99999.
    for i in range(1, 100000):
        result += i
    # Return the result of the task.
    return result

# Define a test case class 'Test_Multi_Threading' that inherits from 'unittest.TestCase'.
class Test_Multi_Threading(unittest.TestCase):
    # Define a test method 'test_multi_threading' to test multi-threading.
    def test_multi_threading(self):
        # Define the number of threads to create.
        num_threads = 10
        # Create an empty list to store thread objects.
        threads = []

        # Create and start multiple threads.
        for _ in range(num_threads):
            # Create a thread, specifying the target function 'perform_task'.
            t = threading.Thread(target=perform_task)
            # Append the thread to the 'threads' list.
            threads.append(t)
            # Start the thread's execution.
            t.start()

        # Wait for all threads to finish.
        for t in threads:
            t.join()

        # Assert that all threads have completed successfully (not alive).
        for t in threads:
            self.assertFalse(t.is_alive())

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#8. Write a Python unit test program to check if a database connection is successful.
# Import the 'unittest' module for writing unit tests.
import unittest
# Import the 'sqlite3' module for working with SQLite databases.
import sqlite3
# Define a test case class 'TestDatabaseConnection' that inherits from 'unittest.TestCase'.
class TestDatabaseConnection(unittest.TestCase):
    # Define a test method 'test_database_connection' to test database connection.
    def test_database_connection(self):
        # Create a database connection in memory.
        conn = sqlite3.connect(':memory:')
        # Create a cursor to interact with the database.
        cursor = conn.cursor()
        # Execute a simple query to select the value 1.
        cursor.execute("SELECT 1")
        # Fetch the result of the query.
        result = cursor.fetchone()
        # Close the cursor and the database connection.
        cursor.close()
        conn.close()
        # Assert that the fetched result is as expected, which should be a tuple containing 1.
        self.assertEqual(result, (1,))
# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()

#9. Write a Python unit test program to check if a database query returns the expected results.
import unittest
import sqlite3

# Define a test case class 'TestDatabaseQuery' that inherits from 'unittest.TestCase'.
class TestDatabaseQuery(unittest.TestCase):
    # Define a method 'setUp' that is executed before each test.
    def setUp(self):
        # Create a database connection in memory and insert test data.
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        # Create an 'employees' table and insert test records.
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
        self.conn.commit()

    # Define a method 'tearDown' that is executed after each test.
    def tearDown(self):
        # Close the database cursor and the database connection.
        self.cursor.close()
        self.conn.close()

    # Define a test method 'test_database_query' to test a database query.
    def test_database_query(self):
        # Execute a SQL query to select employee names and salaries, ordered by name.
        self.cursor.execute("SELECT name, salary FROM employees ORDER BY name")
        results = self.cursor.fetchall()

        # Define the expected results as a list of tuples.
        expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]

        # Assert that the results match the expected results.
        self.assertEqual(results, expected_results)

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()
'''
#10. Write a Python unit test program to check if a function correctly parses and validates input data.
# Import the 'unittest' module for writing unit tests.
import unittest

# Define a function 'parse_and_validate_input' for parsing and validating input data.
def parse_and_validate_input(data):
    # Check if the input data is a string and contains only numeric characters.
    if isinstance(data, str) and data.isnumeric():
        # Convert the string to an integer and check if it's greater than 0.
        return int(data) > 0
    return False

# Define a test case class 'TestInputParsing' that inherits from 'unittest.TestCase'.
class TestInputParsing(unittest.TestCase):
    # Define a test method 'test_valid_input' to test valid input data.
    def test_valid_input(self):
        # Define valid input data as a string containing a positive integer.
        data = "100"
        # Call the 'parse_and_validate_input' function with the valid input data.
        result = parse_and_validate_input(data)
        # Assert that the result is 'True' (indicating valid input).
        self.assertTrue(result)

    # Define a test method 'test_invalid_input' to test invalid input data.
    def test_invalid_input(self):
        # Define invalid input data as a string containing non-numeric characters.
        data = "Hello"
        # Call the 'parse_and_validate_input' function with the invalid input data.
        result = parse_and validate_input(data)
        # Assert that the result is 'False' (indicating invalid input).
        self.assertFalse(result)

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()
