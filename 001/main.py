# We will create several variables, a variable is the object that holds our data.

# A variable containing a string value
variable = "string variable"

# A variable containing an integer number
varnumber = 1

# A variable containing a floating point number
varfloat = 1.1

# Here we use the language builtin function named print to output the string variable.
# Notice that we also use a formatted string to output the value of the string variable.
print(f"variable: {variable}")

# Here we create our own function to output the data received in the argument parameter.
def myfunction(argument): # def FUNCTION_NAME(PARAMETER)
    # Indentation is important.
    # Python knows what is included in the function by the indentation.
    print(argument) # Use the builtin print function to print
                    # the value delivered in the parameter.

# Use the function we created to output the value of the integer variable.
# Notice again we use a formatted string to give some detail to what we're outputting.
myfunction(f'varnumber: {varnumber}')

# This is the end of our first Python program.
# We explain a few basics of Python.
## Different datatypes
## Variables to hold our data
## Using builtin functions to do work
## Creating our own function
## The importance of indentation within the Python language
## And also the use of comments within the programming.

## Your instructor: Earnest Boyd, A.K.A. SSAdvisor
## Questions can be sent to: ssadvisor@seasonedsolutionsadvisor.com