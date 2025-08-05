''' Mask Email Address
Masks the middle characters of the username (before @) with *.
john.doe@example.com →jo****oe@example.com
johndoe@example.com →jo***oe@example.com'''

def mask(email):
    username, domain = email.split('@')

    if len(username) <= 4:
        if len(username) <= 2:
            masked_username = username[0] + '*' * (len(username) - 1)
        else:
            masked_username = username[0] + '*' * (len(username) - 2) + username[-1]
    else:
        masked_username = username[:2] + '*' * (len(username) - 4) + username[-2:]

    masked_id = masked_id + '@' + domain
    print("Masked email:", masked_id)

email_id = input("Enter your email address: ")
mask(email_id)