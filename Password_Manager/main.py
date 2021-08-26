def main():
    import os
    import sys
    import time
    import random
    import re
    import getpass
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from subprocess import check_call

    yes_list = ['yes', 'yeah', 'y', 'sure']
    no_list = ['no', 'nah', 'n', 'nope']
    one_list = ['1', 'one', 'uno', 'one ', 'uno ']
    two_list = ['2', 'two', 'dos', 'two ', 'dos ']
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "12345678910111213141516171819202122232425262728293031323334353637383940"
    single_numbers = '1234567890'
    combined = lower_letters + upper_letters + single_numbers
    special_characters = r'''`~!@#$%^&*()_+-={}|[]\:";'<>?,./'''

    def copy2clip(txt):
        cmd = 'echo ' + txt.strip() + '|clip'
        return check_call(cmd, shell=True)
    ###########################################################################

    username = getpass.getuser()
    path_of_folder = r'C:\Users\%s\Password_Manager' % username
    path_of_file = r'C:\Users\%s\Password_Manager\Password.txt' % username
    is_folder = os.path.isdir(path_of_folder)
    is_file = os.path.isfile(path_of_file)
    if is_folder == False:
        os.mkdir(path_of_folder)
        #print("Folder False")
    if is_file == False:
        with open(path_of_file, 'w') as placeholder:
            placeholder.close()
        # print("Why is it false)
        # print(path_of_file)

    ##########################################################

    def make_email():
        global email_ask
        email_ask = input(
            "[+] Your email is requried incase you forget your master password and need to reset it\n[+] Please enter your email: ")
        len_of_email = len(email_ask)
        last_10 = email_ask[len_of_email - 4:]
        last_10 = str(last_10)

        def email_verify_func():
            time.sleep(1)
            if last_10 != '.com':
                print(
                    '[+] Something went wrong. Please make sure that this is a valid email.')
                print("\nPlease retype your email\n")
                time.sleep(1.5)
                make_email()
            is_this_your_email = input(
                "[+] Is this your correct email?\n" + email_ask + "\nType Here: ")
            if is_this_your_email in yes_list:
                print("Ok")
                time.sleep(1)
            elif is_this_your_email in no_list:
                print("Ok, Resetting...\n")
                time.sleep(1)
                make_email()
            else:
                print("That is not a valid answer. Please try again\n")
                time.sleep(1)
                email_verify_func()
        email_verify_func()
        with open(path_of_email, 'w') as email_file:
            email_file.write(email_ask)
            email_file.close()

    def make_mass_pass():
        global master_password
        master_password = input(
            "[+] Please enter what you would like your master password to be: ")

        def verify_mass_pass():
            time.sleep(1)
            is_this_mass_pass = input(
                "[+] Is this your correct master password?\n" + master_password + "\n[+] Type Here: ")
            if is_this_mass_pass in yes_list:
                print("[+] Ok")
                time.sleep(1)
            elif is_this_mass_pass in no_list:
                print("[+] Ok, Resetting...")
                time.sleep(1)
                make_mass_pass()
            else:
                print("[+] That is not a valid answer. Please try again")
                time.sleep(1)
                verify_mass_pass()
        verify_mass_pass()
        pass_characters_plus_four_randoms_list = []
        for each_character in master_password:
            # print("okokokoko")
            random1 = random.choice(combined)
            random2 = random.choice(combined)
            random3 = random.choice(combined)
            random4 = random.choice(combined)
            pass_characters_plus_four_randoms_list.append(
                each_character + random1 + random2 + random3 + random4)
        pass_characters_plus_four_randoms_str = ''.join(
            pass_characters_plus_four_randoms_list)
        with open(path_of_mass_pass, 'w') as mass_pass_file:
            mass_pass_file.write(pass_characters_plus_four_randoms_str)
            mass_pass_file.close()
    ###########################################################################

    def verify_files_and_folder():
        global username
        global path_of_folder
        global path_of_file
        global is_folder
        global is_file
        global path_of_mass_pass
        global path_of_email
        global currect_master_password
        global currect_email
        global currect_master_password

        username = getpass.getuser()
        path_of_folder = r'C:\Users\%s\Password_Manager' % username
        path_of_file = r'C:\Users\%s\Password_Manager\Password.txt' % username
        path_of_email = r'C:\Users\%s\Password_Manager\Email.txt' % username
        path_of_mass_pass = r'C:\Users\%s\Password_Manager\MP.txt' % username
        is_folder = os.path.isdir(path_of_folder)
        is_file = os.path.isfile(path_of_folder)
        is_email = os.path.isfile(path_of_email)
        is_mass_pass = os.path.isfile(path_of_mass_pass)
        if is_mass_pass == False:
            make_mass_pass()
            with open(path_of_mass_pass) as path_of_mass_pass_read:
                currect_master_password = path_of_mass_pass_read.read()
                path_of_mass_pass_read.close()
            z = 0
            corret_mp_list = []
            with open(path_of_mass_pass) as path_of_mass_pass_read:
                currect_master_password = path_of_mass_pass_read.read()
                path_of_mass_pass_read.close()
                #
            currect_master_password_list = list(currect_master_password)
            currect_master_password_list_len = len(
                currect_master_password_list)
            currect_master_password_list_len_div_5 = currect_master_password_list_len/5
            currect_master_password_list_len_div_5 = int(
                currect_master_password_list_len_div_5)
            for i in range(currect_master_password_list_len_div_5):
                to_append = currect_master_password_list[z]
                # print(to_append)

                z += 5
                corret_mp_list.append(to_append)
            corret_mp_list_joined = ''.join(corret_mp_list)
            currect_master_password = corret_mp_list_joined
            # print(currect_master_password)
        else:
            with open(path_of_mass_pass) as path_of_mass_pass_read:
                currect_master_password = path_of_mass_pass_read.read()
                path_of_mass_pass_read.close()
            z = 0
            corret_mp_list = []
            with open(path_of_mass_pass) as path_of_mass_pass_read:
                currect_master_password = path_of_mass_pass_read.read()
                path_of_mass_pass_read.close()
                #
            currect_master_password_list = list(currect_master_password)
            currect_master_password_list_len = len(
                currect_master_password_list)
            currect_master_password_list_len_div_5 = currect_master_password_list_len/5
            currect_master_password_list_len_div_5 = int(
                currect_master_password_list_len_div_5)
            for i in range(currect_master_password_list_len_div_5):
                to_append = currect_master_password_list[z]
                # print(to_append)

                z += 5
                corret_mp_list.append(to_append)
            corret_mp_list_joined = ''.join(corret_mp_list)
            currect_master_password = corret_mp_list_joined
        if is_email == False:
            make_email()
            with open(path_of_email) as path_of_email_read:
                currect_email = path_of_email_read.read()
                path_of_email_read.close()
            # print(currect_email)
        else:
            with open(path_of_email) as path_of_email_read:
                currect_email = path_of_email_read.read()
                path_of_email_read.close()
            # print(currect_email)

    verify_files_and_folder()

    def see_pass():
        my_email = "pythontesting1219@gmail.com"
        my_password = "Testing95"
        user_email = currect_email
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
                    #your_otp_is {
                        font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                        font-weight: 550;
                        position: relative;
                        padding-top: 1.5%;
                        font-size: 65px;
                        color: whitesmoke;
                        padding-left: 1%;
                        padding-right: 30%;
                    }
                    #otp_number {
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
                    #warning {
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
                    print("\n[+] Incorrect code. Please try again.")
                    time.sleep(1)
                else:
                    print("\n[+] Correct OTP!\n")
                    time.sleep(1)
                    z = 0
                    corret_mp_list = []

                    with open(path_of_mass_pass) as path_of_mass_pass_read:
                        currect_master_password = path_of_mass_pass_read.read()
                        path_of_mass_pass_read.close()
                    #
                    currect_master_password_list = list(
                        currect_master_password)
                    currect_master_password_list_len = len(
                        currect_master_password_list)
                    currect_master_password_list_len_div_5 = currect_master_password_list_len/5
                    currect_master_password_list_len_div_5 = int(
                        currect_master_password_list_len_div_5)
                    for i in range(currect_master_password_list_len_div_5):
                        to_append = currect_master_password_list[z]
                        # print(to_append)

                        z += 5
                        corret_mp_list.append(to_append)
                    corret_mp_list_joined = ''.join(corret_mp_list)
                    currect_master_password = corret_mp_list_joined
                    print(
                        f"Your master password is {currect_master_password}")
                    break

        func_for_loop()
#

    def delete_passwords():
        while True:
            enter_mass_pass = input(
                '\n[+] If you dont know your master password, please type "forgot123()"\n[+] Please enter your master password: ')
            if enter_mass_pass == currect_master_password:
                break
            elif enter_mass_pass == 'forgot123()':
                see_pass()
                break
            else:
                print(
                    f'"{enter_mass_pass}" is not the correct master password. Please try again.')
                time.sleep(1)

        def delete_pass_no_mass():
            with open(path_of_file, 'r') as pass_cont:
                pass_cont_cont = pass_cont.read()
                pass_cont_cont_split = pass_cont_cont.split("+++===")
                del pass_cont_cont_split[-1]
                pass_cont.close()
            decrypted_del_list = []
            y = 0
            what_name_of_site = input(
                "\n[+] Please enter the name of the website you want to delete: ")
            what_name_of_site = what_name_of_site.lower()
            pass_file_read_content_joined = ''.join(
                pass_cont_cont_split)
            what_name_of_site_with_colon = what_name_of_site + ":"
            if what_name_of_site_with_colon in pass_file_read_content_joined:
                for each_set in pass_cont_cont_split:
                    each_set_split = each_set.split(": ")
                    if what_name_of_site == each_set_split[0]:
                        each_set_split_random_characters_thing = each_set_split[1]
                        each_set_split_random_characters_thing_list = list(
                            each_set_split_random_characters_thing)
                        amount_of_characters_in_encoded_pass = len(
                            each_set_split_random_characters_thing_list)
                        amount_of_characters_in_decoded_pass = amount_of_characters_in_encoded_pass/5
                        amount_of_characters_in_decoded_pass = int(
                            amount_of_characters_in_decoded_pass)
                        for i in range(amount_of_characters_in_decoded_pass):
                            char = each_set_split_random_characters_thing_list[y]
                            decrypted_del_list.append(char)
                            y += 5
                        decrypted_str = ''.join(decrypted_del_list)

                        def confirm_del_info():
                            with open(path_of_file, 'r') as pass_read_again:
                                pass_read_again_content = pass_read_again.read()
                                pass_read_again_content_split = pass_read_again_content.split(
                                    "+++===")
                                pass_read_again.close()
                            is_correct_info = input(
                                f"\n[+] Is the correct website {what_name_of_site} with a password of " + '"' + decrypted_str + '" ?\n[+] Type Here: ')
                            if is_correct_info in yes_list:
                                what_name_of_site_with_colon_ = what_name_of_site + ": "
                                for each_seg in pass_read_again_content_split:
                                    if what_name_of_site_with_colon_ in each_seg:
                                        index_of_sect = pass_read_again_content_split.index(
                                            each_seg)
                                del pass_read_again_content_split[index_of_sect]
                                pass_read_again_content_split_joined = '+++==='.join(
                                    pass_read_again_content_split)
                                with open(path_of_file, 'w') as path_write:
                                    path_write.write(
                                        pass_read_again_content_split_joined)
                                    path_write.close()
                                print(
                                    "\n[+] Password Manager Has Been Updated!\n")

                            elif is_correct_info in no_list:
                                print("[+] Ok. Restarting...")
                                time.sleep(1)
                                delete_passwords()
                            else:
                                print(
                                    "[+] That is not a correct answer. Please try again\n")
                                time.sleep(1)
                                confirm_del_info()
                            # or just split it into a list and grab certain elements
                        confirm_del_info()
            else:
                print(
                    "\n[+] That website has not been saved in your manager. If you are sure that it is, please try re-entering the website name.\n")
                time.sleep(2.5)
                delete_pass_no_mass()
        delete_pass_no_mass()

    def change_pass():

        my_email = "pythontesting1219@gmail.com"
        my_password = "Testing95"
        user_email = currect_email
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
                    #your_otp_is {
                        font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                        font-weight: 550;
                        position: relative;
                        padding-top: 1.5%;
                        font-size: 65px;
                        color: whitesmoke;
                        padding-left: 1%;
                        padding-right: 30%;
                    }
                    #otp_number {
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
                    #warning {
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
                    print("\n[+] Incorrect code. Please try again.")
                    time.sleep(1)
                else:
                    print("\n[+] Correct OTP!")

                    def reset():
                        global input_new_mass_pass
                        with open(path_of_mass_pass, 'w') as new_mass_pass:
                            input_new_mass_pass = input(
                                "\n[+] Please enter your new master password: ")
                            time.sleep(.5)

                            def confirm_new_func():
                                confirm_new_mass_pass = input(
                                    f"[+] Is this your correct new master password?\n{input_new_mass_pass}\n[+] Type Here: ")
                                if confirm_new_mass_pass in yes_list:
                                    pass_characters_plus_four_randoms_list = []
                                    for each_character in input_new_mass_pass:
                                        # print("okokokoko")
                                        random1 = random.choice(combined)
                                        random2 = random.choice(combined)
                                        random3 = random.choice(combined)
                                        random4 = random.choice(combined)
                                        pass_characters_plus_four_randoms_list.append(
                                            each_character + random1 + random2 + random3 + random4)
                                    pass_characters_plus_four_randoms_str = ''.join(
                                        pass_characters_plus_four_randoms_list)
                                    new_mass_pass.write(
                                        pass_characters_plus_four_randoms_str)
                                    print("[+] Done!")
                                elif confirm_new_mass_pass in no_list:
                                    print("\n[+] Ok. Resetting...")
                                    time.sleep(1)
                                    reset()
                                else:
                                    print(
                                        "[+] That is not a valid answer. Please try again.")
                                    time.sleep(1)
                                    confirm_new_func()
                            confirm_new_func()
                            new_mass_pass.close()
                    reset()
                    break

        func_for_loop()

    def change_email():
        while True:
            enter_mass_pass = input(
                '\n[+] If you dont know your master password, please type "forgot123()"\n[+] Please enter your master password: ')
            if enter_mass_pass == currect_master_password:
                break
            elif enter_mass_pass == 'forgot123()':
                see_pass()
                break
            else:
                print(
                    f'"{enter_mass_pass}" is not the correct master password. Please try again.')
                time.sleep(1)
        input_new_email = input(
            "[+] Please enter your new email: ")
        input_new_email_len = len(input_new_email)
        last_ten = input_new_email[input_new_email_len - 4:]
        last_ten = str(last_ten)
        if last_ten == '.com':
            def confirm_new_email_func():
                is_correct_new_email = input(
                    f"[+] Is this your correct new email?\n[+] {input_new_email}\n[+] Type Here: ")
                if is_correct_new_email in yes_list:
                    print("\n[+] Ok\n")
                    time.sleep(1)
                    print("[+] Your email has been changed!\n")
                    with open(path_of_email, 'w') as new_email_write:
                        new_email_write.write(input_new_email)
                        new_email_write.close()
                elif is_correct_new_email in no_list:
                    print("\n[+] Ok. Resetting...")
                    time.sleep(1)
                    change_email()
                else:
                    print(
                        "\n[+] That is not a valid answer. Please try again.\n")
                    time.sleep(1)
                    confirm_new_email_func()
            confirm_new_email_func()
        else:
            print(
                '[+] Something went wrong. Please make sure that this is a valid email.')
            print("\n[+] Please retype your email\n")
            time.sleep(1.5)
            change_email()

    def password_generator():
        while True:
            enter_mass_pass = input(
                '\n[+] If you dont know your master password, please type "forgot123()"\n[+] Please enter your master password: ')
            if enter_mass_pass == currect_master_password:
                break
            elif enter_mass_pass == 'forgot123()':
                see_pass()
                break
            else:
                print(
                    f'"{enter_mass_pass}" is not the correct master password. Please try again.')
                time.sleep(1)
        ############Defining Values############

        # class bcolors:
        #     GREEN = '\033[92m'
        #     YELLOW = '\033[93m'
        #     RED = '\033[91m'
        #     BLUE = '\033[94m'

        w = 0
        x = 0
        y = 0
        z = 0
        Incorrect = 1
        move_on = 1
        random_var = 0

        ############Defining Values############

        def gen_pass(num_lo, num_up, num_num, num_special_char):
            special_characters = r'''`~!@#$%^&*()_+-={}|[]\:";'<>?,./'''
            if num_lo == "":
                num_lo = "0"
            if num_up == "":
                num_up = "0"
            if num_num == "":
                num_num = "0"
            if num_special_char == "":
                num_special_char = "0"
            num_lo = int(num_lo)
            num_up = int(num_up)
            num_num = int(num_num)
            num_special_char = int(num_special_char)
            global w, x, y, z
            #################
            empty_lower = ""
            empty_upper = ""
            empty_number = ""
            empty_special_characters = ""
            while True:
                if num_lo != 0:
                    for i in range(num_lo):
                        empty_lower = empty_lower + \
                            random.choice(lower_letters)
                else:
                    empty_lower = ""
                if num_up != 0:
                    for i in range(num_up):
                        empty_upper = empty_upper + \
                            random.choice(upper_letters)
                else:
                    empty_upper = ""
                if num_num != 0:
                    for i in range(num_num):
                        empty_number = empty_number + \
                            random.choice(numbers)
                else:
                    empty_number = ""
                if empty_special_characters != 0:
                    for i in range(num_special_char):
                        empty_special_characters = empty_special_characters + \
                            random.choice(special_characters)
                else:
                    empty_special_characters = ""
                final_str_empty = empty_lower + empty_upper + \
                    empty_number + empty_special_characters
                final_list = list(final_str_empty)
                random.shuffle(final_list)
                final = "".join(final_list)
                print("\nGenerated Password: " + final)

                def add_to_clipboard_yes_or_no_function():
                    add_to_clipboard_yes_or_no = input(
                        "\n[+] Would you like to add this password to your clipboard?\n(y/n)\n[+] Type Here: ")
                    if add_to_clipboard_yes_or_no in yes_list:
                        copy2clip(final)
                    elif add_to_clipboard_yes_or_no in no_list:
                        print("Ok")
                        time.sleep(1)
                    else:
                        print(
                            "That is not a vaild answer choice. Please try again.")
                        time.sleep(1)
                        add_to_clipboard_yes_or_no_function()

                add_to_clipboard_yes_or_no_function()

                break

        #############################INPUTS#############################
        while move_on == 1:
            lo = input(
                "\n[+] How many lower case letters would you like: ")
            if lo == "" or lo == "0":
                w = 1
                break
            if lo != "" and lo not in numbers:
                Incorrect = True
            if lo not in numbers:
                print("Error")
            if lo != "" and lo in numbers:
                move_on = 0
        move_on = 1
        while move_on == 1:
            up = input(
                "\n[+] How many upper case letters would you like: ")
            if up == "" or up == "0":
                x = 1
                break
            if up != "" and up not in numbers:
                Incorrect = True
            if up not in numbers:
                print("Error")
            if up != "" and up in numbers:
                move_on = 0
        move_on = 1
        while move_on == 1:
            num = input("\n[+] How many numbers would you like: ")
            if num == "" or num == "0":
                y = 1
                break
            if num != "" and num not in numbers:
                Incorrect = True
            if num not in numbers:
                print("Error")
            if num != "" and num in numbers:
                move_on = 0
        move_on = 1
        while move_on == 1:
            special_char = input(
                "\n[+] How many special_characters would you like: ")
            if special_char == "" or special_char == "0":
                z = 1
                random_var = 1
                break
            if special_char != "" and special_char not in numbers:
                Incorrect = True
            if special_char not in numbers:
                print("Error")
            if special_char != "" and special_char in numbers:
                move_on = 0
        move_on = 1

        if random_var != 1:
            while True:
                de = input("\n[+] Type a character that is not allowed then click enter to type it again\n"
                           "if there are no characters that you would like to replace, type in the number\n"
                           "9 and hit enter. Or as always, just click enter without typing anything to say none or no more: ")
                if de == "9":
                    break
                if de == "":
                    break
                elif de not in special_characters:
                    print("[+] That is not a character\n")
                else:
                    special_characters = special_characters.replace(de, "")
        gen_pass(lo, up, num, special_char)
        #############################INPUTS#############################

    def password_manager_saver():

        while True:
            enter_mass_pass = input(
                '\n[+] If you dont know your master password, please type "forgot123()"\n[+] Please enter your master password: ')
            if enter_mass_pass == currect_master_password:
                break
            elif enter_mass_pass == 'forgot123()':
                see_pass()
                break
            else:
                print(
                    f'"{enter_mass_pass}" is not the correct master password. Please try again.')
                time.sleep(1)

        def raw_password_saver():

            password_to_be_saved = input(
                "\n[+] Please enter the password you would like to be saved to your manager: ")
            time.sleep(.5)

            def verify_pass():
                is_this_correct_pass = input(
                    "[+] Is this your correct password?\n" + password_to_be_saved + "\n[+] Type Here: ")
                if is_this_correct_pass in yes_list:
                    print("\n[+] Ok")
                    time.sleep(.5)
                elif is_this_correct_pass in no_list:
                    print("\nOk\nRestarting...")
                    time.sleep(1)
                    password_manager_saver()
                else:
                    print("\nThat is not a correct answer. Please try again.")
                    time.sleep(1)
                    verify_pass()
            verify_pass()
            pass_characters_plus_four_randoms_list = []
            for each_character in password_to_be_saved:
                random1 = random.choice(combined)
                random2 = random.choice(combined)
                random3 = random.choice(combined)
                random4 = random.choice(combined)
                pass_characters_plus_four_randoms_list.append(
                    each_character + random1 + random2 + random3 + random4)
            pass_characters_plus_four_randoms_str = ''.join(
                pass_characters_plus_four_randoms_list)
            ######################################################

            def get_site_name_func():
                global name_of_site
                name_of_site = input(
                    "\n[+] Please enter the name of the webite that this password belongs to: ")
                name_of_site = name_of_site.lower()
                time.sleep(1)

                def verify_site_name_func():
                    is_this_correct_site = input(
                        "\n[+] Is this the correct name of the website?\n" + name_of_site + "\n[+] Type Here: ")
                    if is_this_correct_site in yes_list:
                        print("\nOk")
                        time.sleep(.5)
                    elif is_this_correct_site in no_list:
                        print("\nOk\nRestarting...")
                        time.sleep(1)
                        get_site_name_func()
                    else:
                        print("\nThat is not an answer. Please try again")
                        time.sleep(1)
                        verify_site_name_func()
                verify_site_name_func()
            get_site_name_func()

            def check_if_already_exists():
                with open(path_of_file, 'r') as temp_cont:
                    temp_cont_cont = temp_cont.read()
                    temp_cont.close()
                name_of_site_with_checks = name_of_site + ": "
                if name_of_site_with_checks in temp_cont_cont:
                    print(
                        "[+] ERROR\n\n[+] You already have a password saved in your manager for that website")
                    time.sleep(1.5)
                    raw_password_saver()
            check_if_already_exists()

            def write_encrypted_pass_and_site_to_file():
                with open(path_of_file, 'a') as password_file:
                    password_file.write(name_of_site + ": " +
                                        pass_characters_plus_four_randoms_str + "+++===")
                    password_file.close()
            write_encrypted_pass_and_site_to_file()
        raw_password_saver()

    def password_manager_viewer():
        while True:
            enter_mass_pass = input(
                '\n[+] If you dont know your master password, please type "forgot123()"\n[+] Please enter your master password: ')
            if enter_mass_pass == currect_master_password:
                break
            elif enter_mass_pass == 'forgot123()':
                see_pass()
                break
            else:
                print(
                    f'"{enter_mass_pass}" is not the correct master password. Please try again.')
                time.sleep(1)
        with open(path_of_file, 'r') as pass_file_read:
            pass_file_read_content = pass_file_read.read()
            pass_file_read.close()
        pass_file_read_content_split = pass_file_read_content.split(
            "+++===")
        del pass_file_read_content_split[-1]
        # print(pass_file_read_content_split)

        def view_passwords_func():
            decrypted_list = []
            de_decode_list = []
            all_or_one = input(
                "\n[+] Would you like to view all of your passwords, or just a specific one?\n\n[+] Type 1 to see all passwords\n[+] Type 2 to search for a specific one\n\n[+] Type Here: ")
            if all_or_one in one_list:
                for def_ in pass_file_read_content_split:
                    ungrouped_show_all_one = re.search(
                        "(.*:)( )(.*)", def_)
                    web_name = ungrouped_show_all_one.group(1)
                    encoded_pass = ungrouped_show_all_one.group(3)
                    encoded_pass_list = list(encoded_pass)
                    encoded_pass_list_len = len(encoded_pass_list)
                    encoded_pass_list_len_div_5 = encoded_pass_list_len/5
                    encoded_pass_list_len_div_5 = int(
                        encoded_pass_list_len_div_5)
                    xy = 0
                    for i in range(encoded_pass_list_len_div_5):
                        ting_t_append = encoded_pass_list[xy]
                        de_decode_list.append(ting_t_append)
                        xy += 5
                    de_decode_str = ''.join(de_decode_list)
                    print(f"[+] {web_name} {de_decode_str}")
                    de_decode_list.clear()
                    # for
                    #print("[+] " + def_)
            elif all_or_one in two_list:
                def enter_website_func():
                    x = 0
                    what_name_of_site = input(
                        "\n[+] Please enter the name of the website you are seaching for: ")
                    what_name_of_site = what_name_of_site.lower()
                    pass_file_read_content_joined = ''.join(
                        pass_file_read_content_split)
                    what_name_of_site_with_colon = what_name_of_site + ":"
                    if what_name_of_site_with_colon in pass_file_read_content_joined:
                        for each_set in pass_file_read_content_split:
                            each_set_split = each_set.split(": ")
                            if what_name_of_site == each_set_split[0]:
                                each_set_split_random_characters_thing = each_set_split[1]
                                each_set_split_random_characters_thing_list = list(
                                    each_set_split_random_characters_thing)
                                amount_of_characters_in_encoded_pass = len(
                                    each_set_split_random_characters_thing_list)
                                amount_of_characters_in_decoded_pass = amount_of_characters_in_encoded_pass/5
                                amount_of_characters_in_decoded_pass = int(
                                    amount_of_characters_in_decoded_pass)
                                for i in range(amount_of_characters_in_decoded_pass):
                                    char = each_set_split_random_characters_thing_list[x]
                                    decrypted_list.append(char)
                                    x += 5
                                decrypted_str = ''.join(decrypted_list)
                                print(
                                    f"\n[+] The password for {what_name_of_site} is " + '"' + decrypted_str + '"')
                                # or just split it into a list and grab certain elements
                    else:
                        print(
                            "That website is not saved in your manager. Please try again.\n")
                        time.sleep(1)
                        enter_website_func()
                enter_website_func()

            else:
                print("[+] That is not a correct response please try again.")
                time.sleep(1)
                view_passwords_func()
        view_passwords_func()

    def run_again_q():
        again_or_no = input(
            "\n[+] Would you like to run this program again?\n[+] Type Here: ")
        if again_or_no in yes_list:
            print("Ok")
            time.sleep(1.5)
            main()
        elif again_or_no in no_list:
            print("Ok")
            time.sleep(.5)
            quit()
        else:
            print("That is not a correct answer. Please try again")
            time.sleep(1)
            run_again_q()

    def main_question():
        generate_or_save = input(
            "\n[+] Would you like to generate a password, save a password, view your saved passwords, see master password, or change your master password?\n\n[+] Type 1 to generate password\n[+] Type 2 to save a password\n[+] Type 3 to see your saved passwords\n[+] Type 4 to delete a password in your manager\n[+] Type 5 to see your master password\n[+] Type 6 to change your master password\n[+] Type 7 to change your email\n\n[+] Type Here: ")
        generate_or_save = generate_or_save.lower()
        if '1' in generate_or_save or 'one' in generate_or_save:
            password_generator()
            run_again_q()
        elif '2' in generate_or_save or 'two' in generate_or_save:
            password_manager_saver()
            run_again_q()
        elif '3' in generate_or_save or 'three' in generate_or_save:
            password_manager_viewer()
            run_again_q()
        elif '4' in generate_or_save or 'four' in generate_or_save:
            delete_passwords()
            run_again_q()
        elif '5' in generate_or_save or 'five' in generate_or_save:
            see_pass()
            run_again_q()
        elif '6' in generate_or_save or 'six' in generate_or_save:
            change_pass()
            run_again_q()
        elif '7' in generate_or_save or 'seven' in generate_or_save:
            change_email()
            run_again_q()
        else:
            print("That is not a correct response. Please try again.\n")
            time.sleep(1)
            main_question()

    main_question()


main()
