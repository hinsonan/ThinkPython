'''
Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''

def print_row():
    print('+ - - - - + - - - - +')

def print_column():
    print("|\t  |\t    |")

def print_grid():
    print_row()
    repeat_function_three_times(print_column)
    print_row()
    repeat_function_three_times(print_column)
    print_row()

def repeat_function_three_times(func):
    func()
    func()
    func()

def main():
    print_grid()

main()