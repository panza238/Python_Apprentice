import time

print(time.ctime())


def show_default(my_time=time.ctime()):
    print(my_time)

# IMPORTANT!
# function arguments are evaluated AT RUNTIME. So, if I import this as a module in the REPL,
# my_time local variable will be evaluated at the moment of the import, NOT WHENEVER I USE THE FUNCTION.
# So, It will always return the same output once the module has been imported.
# IT WILL ALWAYS REFERENCE THE SAME OBJECT!
# So... Be careful with deafult arguments
