import sys

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

# Check if correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python multiply.py <num1> <num2>")
    sys.exit(1)

# Get arguments and convert to integers

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("Error: Both arguments must be intgers")
    sys.exit(1)


if __name__=='__main__':
    result = multiply(num1, num2)
    print(result)
