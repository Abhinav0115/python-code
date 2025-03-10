'''
Join Method:
    - The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.
    - The separator is a string object that will be inserted between the elements of the sequence.

    syntax:
        stringSeparator.join(iterable)
            - stringSeparator: The string to be joined
            - iterable: The iterable to be joined

'''

a = ["python", "CPP", "java", "csharp", "php", "javascript"]

language = "-".join(a)
b = "XXXXX".join(a)
print(language)  # Output: python_CPP_java_csharp_php_javascript
print(b)  # Output: pythonXXXXXCPPXXXXXjavaXXXXXcsharpXXXXXphpXXXXXjavascript



