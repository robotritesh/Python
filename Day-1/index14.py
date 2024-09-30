def compress_string(string):
  """Compresses a string by counting consecutive occurrences of characters.

  Args:
    string: The input string.

  Returns:
    The compressed string.
  """

  compressed_string = ""
  count = 1

  for i in range(1, len(string)):
    if string[i] == string[i-1]:
      count += 1
    else:
      compressed_string += string[i-1] + str(count)
      count = 1

  compressed_string += string[-1] + str(count)
  return compressed_string

# Example usage:
input_string = "abbcccccdaa"
output_string = compress_string(input_string)
print(output_string)  # Output: a1b2c5d1a2