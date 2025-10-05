# Condition: Check if user can vote
print("Checking voting eligibility:")
age = 25
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print()  # Add spacing

# Else if: Find the highest score among three students
print("Finding the highest score among three students:")
score1 = 85
score2 = 92
score3 = 78
if score1 >= score2 and score1 >= score3:
    highest = score1
elif score2 >= score1 and score2 >= score3:
    highest = score2
else:
    highest = score3
print("The highest score is:", highest)
print()  # Add spacing

# Loop: Send emails to a list of users
print("Sending emails to users:")
users = ["alice@example.com", "bob@example.com", "carol@example.com"]
for user in users:
    print(f"Sending email to {user}")
print()  # Add spacing

# While: Retry connecting to a server until successful
print("Connecting to server...")
attempt = 0
connected = False
while not connected and attempt < 3:
    print(f"Attempt {attempt + 1}: Connecting to server...")
    # Simulate connection success on 2nd try
    if attempt == 1:
        connected = True
        print("Connected!")
    attempt += 1
if not connected:
    print("Failed to connect after 3 attempts.")
print()  # Add spacing

# Break: Find the first even number in a list
print("Finding the first even number in a list:")
numbers = [1, 3, 7, 8, 9]
for n in numbers:
    if n % 2 == 0:
        print("First even number found:", n)
        break
else:
    print("No even number found.")
print()  # Add spacing

# Continue: Print all file names except hidden files
print("Listing non-hidden files:")
files = ["data.csv", ".env", "report.pdf", ".gitignore"]
for file in files:
    if file.startswith('.'):
        continue
    print("Processing file:", file)
print()  # Add spacing

# Pass: Placeholder for future feature in a class
print("Creating a payment processor:")
class PaymentProcessor:
    def process_payment(self, amount):
        # Placeholder for future implementation
        print(f"Processing payment of ${amount} (feature not implemented yet).")
print()
