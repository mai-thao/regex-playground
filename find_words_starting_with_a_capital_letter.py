import re

# Find all words that start with a capital letter

text = "A Monstera Deliciosa plant is also known as the Swiss Cheese Plant because it can grow holes and slits in its leaves!"
pattern = r"[A-Z][a-z]*"
matches = re.findall(pattern, text)
print("Matches found:", matches)

# Pattern explain: 
#   [A-Z]     -> The first letter must be a capital letter
#   [a-z]*    -> It can have 0 or more lowercase letters after it
