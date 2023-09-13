"""
This code generates 400 random valid and invalid emails, saves them in a CSV file,
reads the CSV file and categorizes the emails as valid or invalid, and prints the list of valid and invalid emails.

The `generate_email()` function now uses the following list of domains:

    ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'outlook.com']

This list of domains is not exhaustive, but it includes some of the most popular email providers.
"""

import random
import csv

def generate_email(is_valid):
    if is_valid:
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 15))) 
        domain = ''.join(random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'outlook.com']))
        return f'{name}@{domain}'
    else:
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(random.randint(5, 20)))

def main():
    with open('emails.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(10000):
            email = generate_email(random.randint(0, 1))
            writer.writerow([email])

    with open('emails.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        valid_emails = []
        invalid_emails = []
        for row in reader:
            if row:
                email = row[0]
                if is_valid_email(email):
                    valid_emails.append(email)
                else:
                    invalid_emails.append(email)

    print('The number of valid emails is:', len(valid_emails))
    print('The list of valid emails is:')
    for email in valid_emails:
        print(f'    * {email}')
        
    print('The number of invalid emails is:', len(invalid_emails))
    print('The list of invalid emails is:')
    for email in invalid_emails:
        print(f'    * {email}')

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.]+$'
    match = re.match(regex, email)
    return bool(match)

if __name__ == '__main__':
    main()
