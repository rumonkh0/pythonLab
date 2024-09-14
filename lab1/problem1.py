def character_frequency(string):
  """Calculates the frequency of each character in a given string.

  Args:
    string: The input string.

  Returns:
    A dictionary containing character frequencies.
  """

  frequency = {}
  for char in string:
    if char in frequency:
      frequency[char] += 1
    else:
      frequency[char] = 1
  return frequency

# Get input from the user
input_string = input("Enter a string: ")

# Calculate character frequencies
result = character_frequency(input_string)

# Print the results
for char, freq in result.items():
  print(f"'{char}': {freq}")