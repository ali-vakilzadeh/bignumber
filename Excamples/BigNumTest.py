# import the class bignumber.py before running the example:
# to install the class, use pip:
#           pip install git+http://github.com/ali-vakilzadeh/bignumber.git

From BigNumber import bignumber

# Example usage
num1 = BigNumber("123456789012345678901234567890")
num2 = BigNumber("1234567890")
print("Default display:", num1.display())
print("Grouped by 3, comma separator:", num1.display(3, ','))
print("Scientific notation:", num1.to_scientific())

# Testing arithmetic operations
print("Addition:", num1.add(num2).display())
print("Subtraction:", num1.subtract(num2).display())
print("Multiplication:", num1.multiply(num2).display())
print("Division:", num1.divide(num2).display())

# Testing length function
print("Number of digits in num1:", num1.length())
print("Number of digits in num2:", num2.length())
