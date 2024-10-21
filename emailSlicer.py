email = input("Enter you email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"You username is {username} and you domain is {domain}")