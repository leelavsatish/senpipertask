def is_braces_balanced(input_string):
    # Initialize an empty stack
    stack = []

    # Traverse through each character in the input string
    for char in input_string:
        # If an opening brace is found, push it onto the stack
        if char == '{':
            stack.append(char)
        # If a closing brace is found
        elif char == '}':
            # Check if there is a corresponding opening brace in the stack
            if not stack:
                return False  # No opening brace for this closing brace
            stack.pop()  # Pop the matching opening brace

    # If the stack is empty, it means all braces are balanced
    return len(stack) == 0

input_string = input("Enter a string: ")
if is_braces_balanced(input_string):
    print("True: The braces are balanced.")
else:
    print("False: The braces are not balanced.")