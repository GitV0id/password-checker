# This is the logic for setting up the checks
def special_character_check(password):
    special_chars = "!@#$%^&*()[]{}/?.>,<-_=+:;'"
    for char in password:
        if char in special_chars:
            return True
    return False

def password_has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_password_length(password):
    if len(password) >= 8:
        return True
    return False


def check_password_has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def check_password_has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False
    
# This is the scoring logic
def calculate_final_score(password):

    score = 0

    if special_character_check(password):
        score += 1
    if password_has_lowercase(password):
        score += 1
    if check_password_length(password):
        score += 1
    if check_password_has_number(password):
        score += 1
    if check_password_has_uppercase(password):
        score += 1
    return score

# This is the user input and the final score check
password = input('Enter your password: ')
score = calculate_final_score(password)

# This is the checking for how secure the password is
if special_character_check(password):
    print('Password has special characters!')
else:
    print('Password has no special characters')

if password_has_lowercase(password):
    print('Password has lowercase characters')
else:
    print('Password has no lowercase characters')

if check_password_length(password):
    print('Password is good! 8+ Characters')
else:
    print('Password is vulnerable! <8 characters')


if check_password_has_uppercase(password):
    print('Has uppercase!')
else:
    print('Has no uppercase!')

if check_password_has_number(password):
    print('Password has a number!')
else:
    print('Password has no numbers!')

# This is giving the user recommendations and score
print(f'\n Password strength score: {score}/5 ')

if score == 5:
    print('Your password is strong!')
elif score >= 3:
    print('Your password is average.')
else:
    print('Your password is weak, please upgrade it.')

