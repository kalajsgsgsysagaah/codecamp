# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

# Test the function with the example
test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = mean_var_std.calculate(test_input)

print("Testing with input:", test_input)
print("\nResult:")
for key, value in result.items():
    print(f"'{key}': {value}")

# Test error case
print("\n" + "="*50)
print("Testing error case with less than 9 numbers:")
try:
    mean_var_std.calculate([1, 2, 3, 4, 5])
except ValueError as e:
    print(f"Caught expected error: {e}")

# Run unit tests if they exist
print("\n" + "="*50)
print("Running unit tests...")
main(module='test_module', exit=False)
