# Advanced Keylogger

## Features

- Shows public and private ip
- Shows what application they are on and when the time they switch applications
- Shows username
- Shows internet provider
- Shows Location
- Shows keys pressed
- Adds keylogger to the startup registry
- Shows a log of what was copied to the clipboard

## How it works and How to use it

The program will attempt to install the nessecary modules for the keylogger automatically.

Before you user the program, go to `lines 26 and 26` to enter the email and password that you want the logs to be emailed to. Type your email and pass between the quotes and take away the hashtags in the beginning. Also if you are using gmail, you will have to allow third party apps. You can do that by going to this link `https://myaccount.google.com/lesssecureapps`.

This keylogger will email you the information after a certain amount of time has passed and a certain amount of keys have been pressed. The default is 5 seconds and 20 keys. You can change these setting by going to `lines 112 and 114`.

## How to convert to exe

If you want to convert this program to an exe, just run the following commands in order:

1. `pip install pyinstaller`

2. `pyinstaller --onefile --noconsole .\main.pyw`

If you want to add an icon, run this command instead of step 2: `pyinstaller --onefile --icon=(path_of_icon)--noconsole .\main.pyw`

WARNING!!
If you want to add an icon, the icon file must be in a .ico file format
