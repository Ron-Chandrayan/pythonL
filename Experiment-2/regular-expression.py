import re

text = "The quick brown fox jumps over the lazy dog. Phone: 123-456-7890"

match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group()}")

numbers = re.findall(r"\d+", text)
print(f"Numbers found: {numbers}")

new_text = re.sub(r"lazy", "energetic", text)
print(f"New text: {new_text}")