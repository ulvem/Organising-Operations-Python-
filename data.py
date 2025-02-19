# Global variable
this_text = "Hello, this is a simple function example!"

# Function definition
def log_into_terminal():
    print(this_text)

# Function invocation
log_into_terminal()

# Function definition
def log_into_terminal():
    local_text = "This is a local variable inside the function."
    print(local_text)

# Function invocation
log_into_terminal()

# Trying to access local_text outside the function will result in an error
# print(local_text)  # Uncommenting this line will cause a NameError

# Global variable
this_text = "Hello, this is a simple function example!"

# Function definition
def log_into_terminal():
    local_text = "This is a local variable inside the function."
    print(this_text)
    print(local_text)

# Another function that calls log_into_terminal
def another_function():
    log_into_terminal()

# Function invocation
another_function()

# Global variable
this_text = "Hello, this is a simple function example!"

# Function definition
def log_into_terminal():
    local_text = "This is a local variable inside the function."
    print(this_text)
    print(local_text)

# Assigning the function to a variable
third_function = log_into_terminal

# Calling the function through the variable
third_function()

# Global variable
this_text = "Hello, this is a simple function example!"

# Function definition
def log_into_terminal():
    local_text = "This is a local variable inside the function."
    print(this_text)
    print(local_text)
    
    # Defining a function within log_into_terminal
    def fourth_function():
        print("This is a message from fourth_function inside log_into_terminal.")
    
    # Calling the inner function
    fourth_function()

# Calling the outer function
log_into_terminal()

# Function definition
def log_into_terminal(message):
    print(message)

# Another function that calls log_into_terminal
def another_function():
    log_into_terminal("This is a message passed from another_function.")

# Calling the function
another_function()

# Function definition
def log_into_terminal(message):
    print(message)

# Another function that calls log_into_terminal
def another_function():
    log_into_terminal("This is a message passed from another_function.")

# Assigning the function to a variable
third_function = lambda: log_into_terminal("This is a message passed from third_function.")

# Calling the functions
another_function()
third_function()

# Function definition
def log_into_terminal(message, second_to_log):
    print(message)
    print(second_to_log)

# Another function that calls log_into_terminal
def another_function():
    first_message = "This is a message passed from another_function."
    second_message = "This is the second message from another_function."
    log_into_terminal(first_message, second_message)

# Assigning the function to a variable
third_function = lambda: log_into_terminal(
    "This is a message passed from third_function.",
    "This is the second message from third_function."
)

# Calling the functions
another_function()
third_function()

# Function definition
def greetings(name):
    return f"Hello, {name}!"

# Calling the function with different names
print(greetings("Alice"))
print(greetings("Bob"))
print(greetings("Charlie"))
print(greetings("Diana"))
print(greetings("Eve"))
