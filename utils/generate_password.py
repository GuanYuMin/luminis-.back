from random import choice

long =14
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-'

def generate_password():
    password = ''
    for i in range(long):
        password += choice(chars)
    return password