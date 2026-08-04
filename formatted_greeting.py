# Ask the user for their name
name = input("What's your name? ")

# Remove extra whitespace from the start/end
name = name.strip()

# Capitalize the user's name
name = name.capitalize()

# Greet the user
print(f"Hello, {name}")
