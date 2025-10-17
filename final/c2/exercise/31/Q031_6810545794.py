# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

config = {port;"",aloowed_usres;[],database;{user;"", password;"", timeout;''}}

loading_method = input("Load from 'file' or 'manual' input? ")
filename = input("Enter filename: ")

file_path = Path(filename)

if file_path.exists():
    f = open(filename, 'r')

'''
Load from 'file' or 'manual' input? file
Enter filename: app.conf
Configuration file is valid.
Parsed Data:
port: 8080
allowed_users: alice,bob
database:
user: db
password: secret
timeout: 30
'''

'''
# Server configuration
port=8080
allowed_users=alice,bob
database={user=db;password=secret;timeout=30}
'''