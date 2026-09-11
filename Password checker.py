# User Input (Username and password)
username = input("Enter your username: ")
password = input("Enter your password: ")
print('*'*50)

def check_password(password):
    final_result = True
    # Security check:
    # length (Minimum 8 characters)
    if len(password) < 8:
        final_result = False
        print('Your password is too short❌')

    # Contain at least one digit
    # for i in password:
        # if not any(i.isdigit()): [any() expects a list or string or generator to iterate.]
    if not any(i.isdigit() for i in password):
        final_result = False
        print('Your password does not contain any digit 🔢')

    # Contain at least one uppercase letter
    if not any(i.isupper() for i in password):
        final_result = False
        print('Your password does not contain any uppercase letter 🆎')

    # Contain at least one lowercase letter
    if not any(i.islower() for i in password):
        final_result = False
        print('Your password does not contain any lowercase letter ⚠️')

    # Contain at least one special character
    symbol = '!#$%&_@'
    if not any(i in symbol for i in password):
        final_result = False
        print(f'Your password does not contain any of these symbols ({symbol})')

    if final_result:
        print('Password is accepted!')
    return final_result
# check_password(password)





