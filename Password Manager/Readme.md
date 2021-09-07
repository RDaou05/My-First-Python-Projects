# Password Manager

## Requirements

You have to have pycryptodome, tabulete, and pyperclip installed. Do to that, run the following commands in your terminal

1. `pip install tabulete`
2. `pip install pycryptodome`
3. `pip install pyperclip`

Also, this password manager, sends you an email incase you forget your master password. So, you will have to put in an email and the password for the email, for the OTP to be send from. If you want to compile the passoword manager to an exe, you should put in the email and password that you want the OTP messages to be sent from, and then compile it. (You can do this on `line 21` and `line 23`)

FOR THE OTP TO WORK YOU HAVE TO ALLOW THIS SETTING FOR YOUR EMAIL (If your using gmail). `https://myaccount.google.com/lesssecureapps`

## How it works

This password manager hashes your master password with a sha512 encryption and stores it in a sqlite database. All of the passwords, emails, usernames, etc., that are entered, also get encrypted and stored in an sqlite database.

## Features

- This script also has a password generator and a feature where you can add the generated password to the password manager.

- You can update and delete querys

- You can search for querys using email, password, or app/url

- You can import passwords from other password managers

- You can change your master password using a OTP sent to your email (You can also change your email using your master password)
