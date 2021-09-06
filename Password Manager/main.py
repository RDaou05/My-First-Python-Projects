from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog
from tabulate import tabulate
from Crypto.Cipher import AES
import tkinter as tk
import pyperclip
import pathlib
import smtplib
import hashlib
import sqlite3
import getpass
import random
import string
import time
import csv
import os


username = getpass.getuser()
path_of_db = f'{pathlib.Path.home()}\Password Manager\Vault.db'
# Enter your email
#email_for_code = " "
# Enter your password
#password_for_code = "Testing95"


def check_dirs():
    path_of_pass_folder = fr'C:\Users\{username}\Password Manager'
    if os.path.isdir(path_of_pass_folder) == False:
        os.mkdir(path_of_pass_folder)


def master_pass_settings():
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()

    def read_db_for_mass_pass():
        try:
            c.execute("""SELECT * FROM masspass""")
            stored_hash = str(c.fetchall()[0][0])
            mass_pass_guess = getpass.getpass(
                prompt='[+] Please enter your master password: ', stream=None)
            mass_pass_guess_hash = hashlib.sha512(
                mass_pass_guess.encode()).hexdigest()
            if stored_hash == mass_pass_guess_hash:
                print('\n[+] Unlocked!')
            else:
                print('\n[-] Please try again\n')
                read_db_for_mass_pass()
        except sqlite3.OperationalError:
            def make_mass_pass_table():
                c.execute(
                    """CREATE TABLE IF NOT EXISTS masspass(master_password)""")
                conn.commit()

            def set_mass_pass():
                global new_mass_pass_inp_hash
                new_mass_pass_inp_ = getpass.getpass(
                    prompt='[+] What would you like your master password to be: ', stream=None)
                new_mass_pass_inp_hash = hashlib.sha512(
                    new_mass_pass_inp_.encode()).hexdigest()

            def update_mass_pass():
                c.execute("""INSERT INTO masspass
                    VALUES (?)""", (new_mass_pass_inp_hash,))
                conn.commit()
                c.close()
                conn.close()
            make_mass_pass_table()
            set_mass_pass()
            update_mass_pass()

    read_db_for_mass_pass()


def store_encrypted_pass(encrypted_info_to_store):
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()

    def create_pass_table():
        c.execute(
            """CREATE TABLE IF NOT EXISTS passwords (username_or_email, encrypted_password, website_url_or_name)""")
        conn.commit()

    def add_encrypted_pass():
        c.execute("""INSERT INTO passwords VALUES (?, ?, ?)""",
                  (encrypted_info_to_store[0], encrypted_info_to_store[1], encrypted_info_to_store[2]))
        conn.commit()
    create_pass_table()
    add_encrypted_pass()
    c.close()
    conn.close()


def encrypt_info(user_to_encrypt, pass_to_encrypt, url_to_encrypt):
    encrypt_info_list = []
    for num in range(3):
        if num == 0:
            info_to_encrypt = user_to_encrypt
        elif num == 1:
            info_to_encrypt = pass_to_encrypt
        elif num == 2:
            info_to_encrypt = url_to_encrypt

        password_for_encryption = 'mytestingpasswordabc123randomthingshere*'.encode()
        key = hashlib.sha256(password_for_encryption).digest()
        mode = AES.MODE_CBC
        IV = 'This is an IV456'.encode()

        def pad_message(message_to_add):
            message_to_add = str(message_to_add)
            while len(message_to_add) % 16:
                message_to_add += ' '
            return message_to_add.encode()

        cipher = AES.new(key, mode, IV)

        message = info_to_encrypt.encode()
        padded_message = pad_message(message)

        encrypted_message = cipher.encrypt(padded_message)
        encrypt_info_list.append(encrypted_message)
    store_encrypted_pass(encrypt_info_list)


def decrypt_text(byte_text):
    password = 'mytestingpasswordabc123randomthingshere*'.encode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'This is an IV456'.encode()

    cipher = AES.new(key, mode, IV)

    decrypted_text = cipher.decrypt(byte_text).strip()
    decrypted_text = repr(decrypted_text)[4:-2]
    return decrypted_text


def encrypt_text(info_to_encrypt):
    password_for_encryption = 'mytestingpasswordabc123randomthingshere*'.encode()
    key = hashlib.sha256(password_for_encryption).digest()
    mode = AES.MODE_CBC
    IV = 'This is an IV456'.encode()

    def pad_message(message_to_add):
        message_to_add = str(message_to_add)
        while len(message_to_add) % 16:
            message_to_add += ' '
        return message_to_add.encode()

    cipher = AES.new(key, mode, IV)

    message = info_to_encrypt.encode()
    padded_message = pad_message(message)

    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message


def send_code_to_email(ask_for_email, the_user_email):
    my_email = email_for_code
    my_password = password_for_code
    if ask_for_email == True:
        user_email = input(
            "Please enter your email (This is for incase you ever need to reset your master password)\n[+] Type Here: ")
    elif ask_for_email == False:
        user_email = the_user_email
    ###########################################################
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digits_choice = []

    random.choice(digits)
    for i in range(6):
        the_choice = random.choice(digits)
        digits_choice.append(the_choice)
    final_otp = "".join(digits_choice)

    ###########################################################
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = my_email
    msg['To'] = user_email

    html = """\
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                .otp_box {
                    position:absolute;
                    height: 48%;
                    width: 60%;
                    background-color: #333333;
                    opacity: .76;
                    border-radius: 10px;
                    left: 20%;
                    top: 20%;
                    padding-bottom: 3%;
                    padding-top: 1.5%;
                }
                # your_otp_is {
                    font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                    font-weight: 550;
                    position: relative;
                    padding-top: 1.5%;
                    font-size: 65px;
                    color: whitesmoke;
                    padding-left: 1%;
                    padding-right: 30%;
                }
                # otp_number {
                    font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                    font-weight: 400;
                    position: sticky;
                    /* background-color: black; */
                    font-size: 50px;
                    color: whitesmoke;
                    padding-left: 38%;
                    padding-right: 30%;
                    top: 10%;
                    margin-left: 5%;
                }
                # warning {
                    position: relative;
                    color: white;
                    /* background-color: black; */
                    font-family: Arial, Helvetica, sans-serif;
                    font-weight: bolder;
                    font-size: 140%;
                    top: 12%;
                    margin-left: 15%;
                    margin-right: 10%;
                }

                .otp_mini_box {
                    position: relative;
                    background-color: #2299b5;
                    padding-top: 5%;
                    padding-bottom: 5%;
                    padding-left: 2%;
                    padding-right: 2%;
                    margin-right: 15%;
                    margin-left: 15%;
                    margin-top: 3.5%;
                    border-radius: 15px;
                    top: 4%;
                }
            </style>
        </head>
        <body>
            <div class="otp_box">
                <div class="otp_mini_box">
                    <strong id=your_otp_is>OTP For Login:</strong>
                </div>
                <strong id=otp_number> """ + final_otp + """</strong>
                <div id=warning><p>This OTP is a code only for you to login. Please do not share this with anyone.</p></div>
            </div>
        </body>
    </html>
    """

    part_html = MIMEText(html, 'html')
    msg.attach(part_html)
    content = str(msg)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(my_email, my_password)
    s.sendmail(my_email, user_email, content)
    s.quit()

    def func_for_loop():
        while True:
            enter_otp = input(
                "\n[+] Please enter the 6 digit number that you have recived to your email: ")

            if enter_otp != final_otp:
                print("[+] Incorrect code. Please try again.")
                time.sleep(1)
            else:
                break
        print("\nCorrect OTP")

    func_for_loop()
    return user_email


def email_settings():
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()

    try:
        c.execute('''SELECT * FROM email''')
        c.fetchall()[0]
    except sqlite3.OperationalError:
        user_email_encryped = encrypt_text(send_code_to_email(True, ''))
        c.execute('''CREATE TABLE IF NOT EXISTS email (encrypted_email)''')
        conn.commit()
        c.execute("""INSERT INTO email VALUES (?)""", (user_email_encryped,))
        conn.commit()
    c.close()
    conn.close()


def search_and_display_database(search_catagory, enter_search_info_prompt, ispass, findall):
    table_headers = ['Username', 'Password', 'Website']
    list_of_decoded_tuples = []

    if findall == False:
        if ispass:
            search_catagory_info = getpass.getpass(
                prompt=enter_search_info_prompt, stream=None)
        else:
            search_catagory_info = input(enter_search_info_prompt)
    else:
        pass
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    for tuple_info in c.fetchall():
        list_of_tuple_info = []
        for info in tuple_info:
            list_of_tuple_info.append(decrypt_text(info))
        decrypted_tuple = (
            list_of_tuple_info[0], list_of_tuple_info[1], list_of_tuple_info[2])
        list_of_decoded_tuples.append(decrypted_tuple)
    if findall == False:
        list_of_tuples_to_display = []
        if search_catagory == 'username_or_email':
            for tuple_info in list_of_decoded_tuples:
                if search_catagory_info.lower() in tuple_info[0].lower():
                    list_of_tuples_to_display.append(
                        (tuple_info[0], tuple_info[1], tuple_info[2]))

        elif search_catagory == 'encrypted_password':
            for tuple_info in list_of_decoded_tuples:
                if search_catagory_info.lower() in tuple_info[1].lower():
                    list_of_tuples_to_display.append(
                        (tuple_info[0], tuple_info[1], tuple_info[2]))
        elif search_catagory == 'website_url_or_name':
            for tuple_info in list_of_decoded_tuples:
                if search_catagory_info.lower() in tuple_info[2].lower():
                    list_of_tuples_to_display.append(
                        (tuple_info[0], tuple_info[1], tuple_info[2]))
        else:
            print('\n\n[-] AN ERROR HAS OCCURED. PLEASE TRY AGAIN LATER.')
    else:
        list_of_tuples_to_display = list_of_decoded_tuples
    print(tabulate(list_of_tuples_to_display, headers=table_headers))


def delete_query():
    list_of_valid_ids = []
    list_of_confirmed_rowids = []

    def show_table():
        global starting_row_id

        conn = sqlite3.connect(path_of_db)
        c = conn.cursor()
        table_headers = ['ID  ', 'Username', 'Password', 'Website']
        list_of_decoded_tuples = []

        def get_row_id(tuple_index):
            c.execute('SELECT rowid, * FROM passwords')
            starting_row_id = int(c.fetchall()[tuple_index][0])
            # print(starting_row_id)
            return starting_row_id
        c.execute("SELECT * FROM passwords")
        for num, tuple_info in enumerate(c.fetchall()):
            list_of_tuple_info = []
            for info in tuple_info:
                list_of_tuple_info.append(decrypt_text(info))
            list_of_confirmed_rowids.append(get_row_id(num))
            list_of_valid_ids.append(num + 1)
            decrypted_list = [f'{num + 1}  ', list_of_tuple_info[0],
                              list_of_tuple_info[1], list_of_tuple_info[2]]
            list_of_decoded_tuples.append(decrypted_list)
        print(tabulate(list_of_decoded_tuples, headers=table_headers))
        c.close()
        conn.close()

    def get_query():
        conn = sqlite3.connect(path_of_db)
        c = conn.cursor()
        id_to_delete = input(
            '\n\n[+] Please enter the id that you would like to delete (If you want to delete multiple IDs, separate them with a comma): ')
        try:
            id_to_delete = id_to_delete.replace(' ', '')
        except:
            pass
        if ',' in id_to_delete:
            list_of_entered_ids = []

            # Makes sure all characters are numbers
            modded_id_to_delete = id_to_delete.strip().split(',')
            for item in modded_id_to_delete:
                if item == '':
                    modded_id_to_delete.remove('')
            for char in modded_id_to_delete:
                try:
                    list_of_entered_ids.append(int(char))
                    print(f'{char} has been appended')
                except ValueError:
                    print(
                        f'\n[-] {char} is not a vaild ID. Please try again.\n')
                    c.close()
                    conn.close()
                    time.sleep(.5)
                    get_query()

            for number in list_of_entered_ids:  # Confirms that all numbers are valid ID's
                if number not in list_of_valid_ids:
                    print(
                        f'\n[-] {number} is not a vaild ID. Please try again.\n')
                    c.close()
                    conn.close()
                    time.sleep(.5)
                    get_query()
                else:
                    pass

            # This will delete all valid ID's
            def confirm_delete_func():
                print()
                for valid_id in list_of_entered_ids:
                    valid_id = int(valid_id)
                    rowid_to_delete = list_of_valid_ids.index(valid_id)
                    rowid_to_delete = list_of_confirmed_rowids[rowid_to_delete]
                    c.execute('SELECT rowid, * FROM passwords WHERE rowid=?',
                              (rowid_to_delete,))
                    query_content = c.fetchall()[0]
                    print(f'{decrypt_text(query_content[1])} | ', f'{decrypt_text(query_content[2])} | ', decrypt_text(
                        query_content[3]), end='\n')

                while True:
                    confirm_delete = input(
                        '\n[+] Are you sure you want to delete the following rows: ')
                    confirm_delete_modified = confirm_delete.strip().lower()
                    if confirm_delete_modified == 'y' or confirm_delete_modified == 'yes':
                        for valid_id in list_of_entered_ids:
                            valid_id = int(valid_id)
                            rowid_to_delete = list_of_valid_ids.index(valid_id)
                            rowid_to_delete = list_of_confirmed_rowids[rowid_to_delete]
                            c.execute('DELETE FROM passwords WHERE rowid=?',
                                      (rowid_to_delete,))
                            conn.commit()
                        print('\n[+] Queries have been deleted!')
                        break
                    elif confirm_delete_modified == 'n' or confirm_delete_modified == 'no':
                        print("\n[+] Ok those queries won't be deleted")
                        c.close()
                        conn.close()
                        break
                    else:
                        print(
                            '\n[-] That is not a vaild response please try again')
            confirm_delete_func()
        else:
            try:
                id_to_delete = int(id_to_delete)
            except ValueError:
                print("\n[-] That is not a vaild ID please try again\n")
                c.close()
                conn.close()
                time.sleep(.5)
                get_query()
            if id_to_delete not in list_of_valid_ids:
                print(
                    f"\n[-] {id_to_delete} is not a vaild ID please try again\n")
                c.close()
                conn.close()
                time.sleep(.5)
                get_query()
            else:
                rowid_to_delete = list_of_valid_ids.index(id_to_delete)
                rowid_to_delete = list_of_confirmed_rowids[rowid_to_delete]
                c.execute(
                    'SELECT rowid, * FROM passwords WHERE rowid=?', (rowid_to_delete,))
                query_info = c.fetchall()[0]
                print()
                print(f'{decrypt_text(query_info[1])} | ', f'{decrypt_text(query_info[2])} | ', decrypt_text(
                    query_info[3]), end='\n')
                while True:
                    confirm_delete = input(
                        '\n[+] Are you sure you want to delete the query above: ')
                    confirm_delete_modified = confirm_delete.strip().lower()
                    if confirm_delete_modified == 'y' or confirm_delete_modified == 'yes':
                        c.execute('''DELETE FROM passwords WHERE rowid = ?''',
                                  (rowid_to_delete,))
                        conn.commit()
                        c.close()
                        conn.close()
                        print('\n[+] Query have been deleted!')
                        break
                    elif confirm_delete_modified == 'n' or confirm_delete_modified == 'no':
                        print("\n[+] Ok those queries won't be deleted")
                        c.close()
                        conn.close()
                        time.sleep(1)
                        delete_query()
                        break
                    else:
                        print(
                            '\n[-] That is not a vaild response please try again')

    show_table()
    get_query()


def update_query():
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()

    list_of_valid_ids = []
    list_of_confirmed_rowids = []

    def show_table():
        global starting_row_id

        table_headers = ['ID  ', 'Username', 'Password', 'Website']
        list_of_decoded_tuples = []

        def get_row_id(tuple_index):
            c.execute('SELECT rowid, * FROM passwords')
            starting_row_id = int(c.fetchall()[tuple_index][0])
            # print(starting_row_id)
            return starting_row_id
        c.execute("SELECT * FROM passwords")
        for num, tuple_info in enumerate(c.fetchall()):
            list_of_tuple_info = []
            for info in tuple_info:
                list_of_tuple_info.append(decrypt_text(info))
            list_of_confirmed_rowids.append(get_row_id(num))
            list_of_valid_ids.append(num + 1)
            decrypted_list = [f'{num + 1}  ', list_of_tuple_info[0],
                              list_of_tuple_info[1], list_of_tuple_info[2]]
            list_of_decoded_tuples.append(decrypted_list)
        print(tabulate(list_of_decoded_tuples, headers=table_headers))

    def get_query_to_update():
        while True:
            try:
                query_to_update = int(input(
                    '\n[+] Please enter the ID of the query you would like to be updated: '))
                break
            except ValueError:
                print('\n[-] That is not a vaild response. Please try again.\n')

        if query_to_update not in list_of_valid_ids:
            print(
                f'\n[-] {query_to_update} is not a vaild ID. Please try again.')
            get_query_to_update()
        else:
            return int(query_to_update)

    def confirm_update_selection():
        c.execute(
            'SELECT rowid, * FROM passwords WHERE rowid=?', (rowid_to_delete,))
        query_info = c.fetchall()[0]
        print()
        print(f'{decrypt_text(query_info[1])} | ', f'{decrypt_text(query_info[2])} | ', decrypt_text(
            query_info[3]), end='\n')
        while True:
            confirm_query_above = input(
                '\n[+] Are you sure you want to update the query above: ')
            confirm_query_above_modded = confirm_query_above.lower().strip().replace(' ', '')
            if confirm_query_above_modded == 'yes' or confirm_query_above_modded == 'y':
                print()
                break
            elif confirm_query_above_modded == 'no' or confirm_query_above_modded == 'n':
                print('Query has been unselected\n')
                time.sleep(1)
                c.close()
                conn.close()
                update_query()
                break
            else:
                print(
                    f'{confirm_query_above} is not a vaild response. Please try again.\n')

    show_table()
    custom_id_to_update = get_query_to_update()
    rowid_to_delete = list_of_valid_ids.index(custom_id_to_update)
    rowid_to_delete = list_of_confirmed_rowids[rowid_to_delete]
    confirm_update_selection()

    while True:
        what_to_update = input(
            '\n[+] Would you like to update the username/email, password, or app/url: ')
        what_to_update_modded = what_to_update.strip().lower().replace(' ', '')
        if what_to_update_modded == 'username' or what_to_update_modded == 'user' or what_to_update_modded == 'email':
            username_to_replace = input(
                '\n[+] Please enter the new username you would like for this query: ')
            c.execute('UPDATE passwords SET username_or_email=? WHERE rowid=?',
                      (encrypt_text(username_to_replace), rowid_to_delete))
            conn.commit()
            print('\n[+] Username has been updated')
            break
        elif what_to_update_modded == 'pass' or what_to_update_modded == 'password':
            password_to_replace = getpass.getpass(
                prompt='[+] Please enter your NEW password: ', stream=None)
            c.execute('UPDATE passwords SET encrypted_password=? WHERE rowid=?',
                      (encrypt_text(password_to_replace), rowid_to_delete))
            conn.commit()
            print('\n[+] Password has been updated')
            break
        elif what_to_update_modded == 'app' or what_to_update_modded == 'url' or what_to_update_modded == 'website' or what_to_update_modded == 'site' or what_to_update_modded == 'app/url':
            website_to_replace = input(
                '\n[+] Please enter the new App/URL you would like for this query: ')
            c.execute('UPDATE passwords SET website_url_or_name=? WHERE rowid=?',
                      (encrypt_text(website_to_replace), rowid_to_delete))
            conn.commit()
            print('\n[+] App/URL has been updated')
            break
        else:
            print(
                f'"{what_to_update}" is not a valid response. Please try again')

    c.close()
    conn.close()


def open_file_explorer():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def password_manager_start():
    feature_to_run = input(
        '\n\n[+] Press 1 to add a password\n[+] Press 2 to see your passwords\n[+] Press 3 to update or delete a query\n[+] Press 4 to change your Master Password or email\n[+] Press 5 to import passwords\n\n[+] Type Here: ')
    if feature_to_run.strip() == '1' or feature_to_run.strip().lower() == 'one':
        user_or_email_input = input(
            "\n[+] Please enter your username or email for the app/site: ")
        password_input = getpass.getpass(
            prompt='[+] Please enter your password that you would like to store: ', stream=None)
        url_or_app_input = input(
            "\n[+] Please enter the url or name of the app this is for: ")
        encrypt_info(user_or_email_input, password_input, url_or_app_input)
        print("\n\n[+] Info has been successfully added to database")
    elif feature_to_run.strip() == '2' or feature_to_run.strip().lower() == 'two':
        while True:
            how_to_search = input(
                '\n[+] Press 1 to search using username or email\n[+] Press 2 to search using password\n[+] Press 3 to search using app name or url\n[+] Press 4 to show all info\n[+] Type Here: ')
            if how_to_search.strip() == '1' or how_to_search.strip().lower() == 'one':
                search_and_display_database(
                    'username_or_email', '\n\n[+] Please enter the username or email you want to search with: ', False, False)
                break
            elif how_to_search.strip() == '2' or how_to_search.strip().lower() == 'two':
                search_and_display_database(
                    'encrypted_password', '\n\n[+] Please enter the password you want to search with: ', True, False)
                break
            elif how_to_search.strip() == '3' or how_to_search.strip().lower() == 'three':
                search_and_display_database(
                    'website_url_or_name', '\n\n[+] Please enter the URL or app name you want to search with: ', False, False)
                break
            elif how_to_search.strip() == '4' or how_to_search.strip().lower() == 'four':
                search_and_display_database(
                    '', '', False, True)
                break
            else:
                print('\n[-] That is not a vaild response. Please try again.\n')
    elif feature_to_run.strip() == '3' or feature_to_run.strip().lower() == 'three':
        # delete_query()
        while True:
            update_or_delete = input(
                '\n[+] Are you trying to update or delete query(s): ')
            if update_or_delete.strip().lower() == 'update':
                update_query()
                break
            elif update_or_delete.strip().lower() == 'delete':
                delete_query()
                break
            else:
                print('\n[-] That is not a vaild response. Please try again.\n')
    elif feature_to_run.strip() == '4' or feature_to_run.strip().lower() == 'four':
        while True:
            email_or_pass = input(
                '\n[+] Press 1 to change your master password\n[+] Press 2 to change your email\n\n[+] Type Here: ')
            email_or_pass_modified = email_or_pass.strip().lower()
            if email_or_pass_modified == '1' or email_or_pass_modified == 'one':
                conn = sqlite3.connect(path_of_db)
                c = conn.cursor()
                c.execute('''SELECT * FROM email''')
                encrypted_email = c.fetchall()[0][0]
                decrypted_email = decrypt_text(encrypted_email)
                send_code_to_email(False, decrypted_email)
                c.execute('''DROP TABLE masspass''')
                conn.commit()
                master_pass_settings()
                break

            elif email_or_pass_modified == '2' or email_or_pass_modified == 'two':
                master_pass_settings()
                conn = sqlite3.connect(path_of_db)
                c = conn.cursor()
                while True:
                    confirm_email_change = input(
                        '\n[+] Are you sure you want to change your email: ')
                    confirm_email_change_modified = confirm_email_change.lower().strip()
                    if confirm_email_change_modified == 'yes' or confirm_email_change_modified == 'y':
                        c.execute('''DROP TABLE email''')
                        conn.commit()
                        c.close()
                        conn.close()
                        email_settings()
                        break
                    elif confirm_email_change_modified == 'no' or confirm_email_change_modified == 'n':
                        print("\n[+] Ok. Your email won't be changed")
                        break
                    else:
                        print(
                            '\n[-] That is not a vaild response. Please try again.\n')
                break
            else:
                print('\n[+] That is not a vaild response. Please try again')
    elif feature_to_run.strip() == '5' or feature_to_run.strip().lower() == 'five':
        email_settings()
        master_pass_settings()
        all_csv_lines = []

        with open(open_file_explorer(), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                all_csv_lines.append((line[2], line[3], line[0]))
            csv_file.close()
        for info_tuple in all_csv_lines:
            encrypt_info(info_tuple[0], info_tuple[1], info_tuple[2])
    else:
        print('\n[-] That is not a vaild response. Please try again.\n')
        password_manager_start()


def password_generator():
    generated_password = ''
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    all_numbers = string.digits
    special_characters = string.punctuation

    ##########################################

    def prompt_for_amount(character_to_ask_for):
        prompt = f"\n[+] Please enter the amount of {character_to_ask_for} you want\n(If you don't want any, type 0, or just press ENTER)\n[+] Type Here: "
        return input(prompt)

    def get_amount_of_characters_wanted(characters_to_ask_for):
        while True:
            amount_of_characters_wanted = prompt_for_amount(
                characters_to_ask_for)
            # Checks if no input was provided (meaning the user doesn't want any of thoses characters)
            if len(amount_of_characters_wanted.strip()) == 0:
                amount_of_characters_wanted = 0
                break
            else:
                try:
                    amount_of_characters_wanted = int(
                        amount_of_characters_wanted)
                    break
                except ValueError:
                    print(
                        f'[-] "{amount_of_characters_wanted}" is not a valid response. Please try again.')

        return amount_of_characters_wanted

    #----------------Getting Requirements For Password-----------------#
    amount_of_lowercase_letters_wanted = get_amount_of_characters_wanted(
        'lowercase letters')
    amount_of_uppercase_letters_wanted = get_amount_of_characters_wanted(
        'uppercase letters')
    amount_of_numbers_wanted = get_amount_of_characters_wanted('numbers')
    amount_of_special_characters_wanted = get_amount_of_characters_wanted(
        'special characters')
    #----------------Getting Requirements For Passoword-----------------#

    def choose_random_characters(string_to_choose_from, amount_of_characters_to_generate):
        generated_string = ''
        for i in range(amount_of_characters_to_generate):
            generated_string += random.choice(string_to_choose_from)
        return generated_string
    #-------------------------Generating Characters-------------------------#
    lower_letters_generated = choose_random_characters(
        lower_letters, amount_of_lowercase_letters_wanted)
    upper_letters_generated = choose_random_characters(
        upper_letters, amount_of_uppercase_letters_wanted)
    numbers_generated = choose_random_characters(
        all_numbers, amount_of_numbers_wanted)
    special_characters_generated = choose_random_characters(
        special_characters, amount_of_special_characters_wanted)
    #-------------------------Generating Characters-------------------------#

    combined_string_list = list(lower_letters_generated + upper_letters_generated +
                                numbers_generated + special_characters_generated)
    random.shuffle(combined_string_list)
    generated_password = ''.join(combined_string_list)
    while True:
        ask_to_store = input(
            f'\n\n[+] Your generated password is: " {generated_password} ". Would you like to copy it to your clipboard?\n[+] Type Here: ')
        ask_to_store_modified = ask_to_store.strip().lower()
        if ask_to_store_modified == 'yes' or ask_to_store_modified == 'y':
            pyperclip.copy(generated_password)
            break
        elif ask_to_store_modified == 'no' or ask_to_store_modified == 'n':
            print(
                "\n[+] Ok your generated password will not be copied to clipboard\n")
            break
        else:
            print('\n[+] That is not a vaild response. Please try again.')
    while True:
        ask_to_store = input(
            f'\n\n[+] Would you like to store your generated password in your password manager?\n[+] Type Here: ')
        ask_to_store_modified = ask_to_store.strip().lower()
        if ask_to_store_modified == 'y' or ask_to_store_modified == 'yes':
            # Login To Password Manager
            email_settings()
            master_pass_settings()
            #--------------Encrypt and Store in Password Manager--------------#
            user_or_email_input = input(
                "\n[+] Please enter your username or email for the app/site: ")
            url_or_app_input = input(
                "\n[+] Please enter the url or name of the app this is for: ")
            encrypt_info(user_or_email_input,
                         generated_password, url_or_app_input)
            print("\n\n[+] Info has been successfully added to database")
            #--------------Encrypt and Store in Password Manager--------------#
            break
        elif ask_to_store_modified == 'n' or ask_to_store_modified == 'no':
            print('Ok. Your generated password will not be stored.')
            break
        else:
            print('\n[+] That is not a vaild response. Please try again.')


def options():
    what_to_do = input(
        '\n[+] Press 1 to access the password manager\n[+] Press 2 to access the password generator\n\n[+] Type Here: ')
    if what_to_do.strip() == '1' or what_to_do.strip().lower() == 'one':
        check_dirs()
        email_settings()
        master_pass_settings()
        password_manager_start()
    elif what_to_do.strip() == '2' or what_to_do.strip().lower() == 'two':
        password_generator()
    else:
        print('\n[-] That is not a vaild response. Please try again.\n')
        options()


def ask_to_run_again():
    while True:
        run_again_question = input(
            '\n[+] Would you like to run this program again: ')
        run_again_question_modified = run_again_question.strip().lower()
        if run_again_question_modified == 'yes' or run_again_question_modified == 'y':
            options()
            break
        elif run_again_question_modified == 'no' or run_again_question_modified == 'n':
            quit()
        else:
            print('\n[-] That is not a vaild response. Please try again.')


def testing():
    username = getpass.getuser()
    path_of_db = fr'C:\Users\{username}\Password Manager\vault.db'
    path_of_pass_folder = fr'C:\Users\{username}\Password Manager'
    if os.path.isdir(path_of_pass_folder) == False:
        os.mkdir(path_of_pass_folder)
    conn = sqlite3.connect(path_of_db)
    c = conn.cursor()

    c.execute('select rowid from passwords')
    print(c.fetchall())
    c.close()
    conn.close()


options()
while True:
    ask_to_run_again()
