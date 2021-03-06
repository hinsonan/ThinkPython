"""
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
print('spam')
do_twice(print_spam)
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your script.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
5. Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
"""
def do_twice(function, string):
    function(string)
    function(string)

def print_spam(string):
    print(string)

def do_four(func):
    do_twice(func, 'four')
    do_twice(func, 'four')

do_twice(print_spam, 'spam')

do_four(print_spam)
