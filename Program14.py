#Remove special strings
import string
import re
sample_str = "Test&[88]%%$$$#$%-+String/@"
# Create a regex pattern to match all special characters in string
pattern = r'[' + string.punctuation + ']'
# Remove special characters from the string
sample_str = re.sub(pattern, '', sample_str)
print(sample_str)