'''
Match Case:
    - The match statement is a new feature in Python 3.10 that allows you to write more readable code by using pattern matching.
    - The match statement is similar to the switch statement in other programming languages.
    - The match statement is used to compare a value against a series of patterns.
    - The case statement is used to define the patterns.

'''


# Example 1: Match Case

def http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"
        
print("200:" , http_status(200))  # Output: OK
print("400:",http_status(400))  # Output: Bad Request
print("404:",http_status(404))  # Output: Not Found
print("500:",http_status(500))  # Output: Internal Server Error
print("600:",http_status(600))  # Output: Unknown Status Code