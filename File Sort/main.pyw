import time
import os
import shutil
import time
import getpass
import threading
import re
import threading
import keyboard
try:
    def main_program():
        try:
            username = getpass.getuser()
            desktop_path = r'C:\Users\%s\Desktop' % username
            downloads_path = r'C:\Users\%s\Downloads' % username
            ldesktop = os.listdir(desktop_path)
            ldownloads = os.listdir(downloads_path)
            ##########################################################

            ##################IDENTIFY PATHS########################
            desktop_path_exe = desktop_path + "\\" + 'EXE'
            downloads_path_exe = downloads_path + "\\" + 'EXE'
            #
            desktop_path_lnk = desktop_path + "\\" + 'Shortcuts'
            downloads_path_lnk = downloads_path + "\\" + 'Shortcuts'
            #
            desktop_path_txt = desktop_path + "\\" + 'TXT'
            downloads_path_txt = downloads_path + "\\" + 'TXT'
            #
            desktop_path_url = desktop_path + "\\" + 'Games'
            downloads_path_url = downloads_path + "\\" + 'Games'
            #
            desktop_path_MP3 = desktop_path + "\\" + 'MP3'
            downloads_path_MP3 = downloads_path + "\\" + 'MP3'
            #
            desktop_path_MP4 = desktop_path + "\\" + 'MP4'
            downloads_path_MP4 = downloads_path + "\\" + 'MP4'
            #
            desktop_path_ICO = desktop_path + "\\" + 'ICO'
            downloads_path_ICO = downloads_path + "\\" + 'ICO'
            #
            desktop_path_PNG = desktop_path + "\\" + 'PNG'
            downloads_path_PNG = downloads_path + "\\" + 'PNG'
            #
            desktop_path_py = desktop_path + "\\" + 'Python'
            downloads_path_py = downloads_path + "\\" + 'Python'
            ##################IDENTIFY PATHS########################

            def get_extention(file):
                try:
                    file_re = re.search("(.*\.)(.*)", file)
                    file_extention = file_re.group(2)
                    file_extention_with_period = "." + file_extention
                    return file_extention_with_period
                except AttributeError:
                    return '-+'

            ##########################################################

            #################CHECKING FOR DIRS######################
            # check_if_downloads_exe = os.path.isdir(downloads_path_exe)
            # check_if_downloads_lnk = os.path.isdir(downloads_path_lnk)
            # check_if_downloads_txt = os.path.isdir(downloads_path_txt)
            # check_if_downloads_url = os.path.isdir(downloads_path_url)
            # check_if_downloads_MP3 = os.path.isdir(downloads_path_MP3)
            # check_if_downloads_MP4 = os.path.isdir(downloads_path_MP4)
            # check_if_downloads_ICO = os.path.isdir(downloads_path_ICO)
            # check_if_downloads_PNG = os.path.isdir(downloads_path_PNG)
            # check_if_downloads_py = os.path.isdir(downloads_path_py)
            #################CHECKING FOR DIRS######################

            ########MAKE FOLDERS#########
            # if check_if_downloads_exe == False:
            #     os.mkdir(downloads_path_exe)
            # if check_if_downloads_lnk == False:
            #     os.mkdir(downloads_path_lnk)
            # if check_if_downloads_txt == False:
            #     os.mkdir(downloads_path_txt)
            # if check_if_downloads_url == False:
            #     os.mkdir(downloads_path_url)
            # if check_if_downloads_MP3 == False:
            #     os.mkdir(downloads_path_MP3)
            # if check_if_downloads_MP4 == False:
            #     os.mkdir(downloads_path_MP4)
            # if check_if_downloads_ICO == False:
            #     os.mkdir(downloads_path_ICO)
            # if check_if_downloads_PNG == False:
            #     os.mkdir(downloads_path_PNG)
            # if check_if_downloads_py == False:
            #     os.mkdir(downloads_path_py)
            #################### MAKE FOLDERS#########

            ####################  DESKTOP  ########################

            def main_desktop():
                try:
                    desktop_path = r'C:\Users\%s\Desktop' % username
                    # while True:
                    ########################################################
                    check_if_desktop_exe = os.path.isdir(desktop_path_exe)
                    check_if_desktop_lnk = os.path.isdir(desktop_path_lnk)
                    check_if_desktop_txt = os.path.isdir(desktop_path_txt)
                    check_if_desktop_url = os.path.isdir(desktop_path_url)
                    check_if_desktop_MP3 = os.path.isdir(desktop_path_MP3)
                    check_if_desktop_MP4 = os.path.isdir(desktop_path_MP4)
                    check_if_desktop_ICO = os.path.isdir(desktop_path_ICO)
                    check_if_desktop_PNG = os.path.isdir(desktop_path_PNG)
                    check_if_desktop_py = os.path.isdir(desktop_path_py)
                    ########################################################
                    time.sleep(.01)
                    list_of_desktop_files = []
                    for each_file in ldesktop:
                        # print(each_file)
                        extent = get_extention(each_file)
                        if extent != '-+':
                            list_of_desktop_files.append(extent)

                    if '.exe' in list_of_desktop_files or '.EXE' in list_of_desktop_files:
                        if check_if_desktop_exe == False:
                            os.mkdir(desktop_path_exe)
                        ldesktop_for_exe = os.listdir(desktop_path)
                        for each_file in ldesktop_for_exe:
                            ext = get_extention(each_file)
                            if ext == '.exe' or ext == '.EXE':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'EXE' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.lnk' in list_of_desktop_files or '.LNK' in list_of_desktop_files:
                        if check_if_desktop_lnk == False:
                            os.mkdir(desktop_path_lnk)
                        ldesktop_for_lnk = os.listdir(desktop_path)
                        for each_file in ldesktop_for_lnk:
                            ext = get_extention(each_file)
                            if ext == '.lnk' or ext == '.LNK':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'Shortcuts' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.TXT' in list_of_desktop_files or '.txt' in list_of_desktop_files:
                        if check_if_desktop_txt == False:
                            os.mkdir(desktop_path_txt)
                        ldesktop_for_txt = os.listdir(desktop_path)
                        for each_file in ldesktop_for_txt:
                            ext = get_extention(each_file)
                            if ext == '.TXT' or ext == '.txt':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'TXT' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.url' in list_of_desktop_files or '.URL' in list_of_desktop_files:
                        if check_if_desktop_url == False:
                            os.mkdir(desktop_path_url)
                        ldesktop_for_url = os.listdir(desktop_path)
                        for each_file in ldesktop_for_url:
                            ext = get_extention(each_file)
                            if ext == '.url' or ext == '.URL':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'Games' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.mp3' in list_of_desktop_files or '.MP4' in list_of_desktop_files:
                        if check_if_desktop_MP3 == False:
                            os.mkdir(desktop_path_MP3)
                        ldesktop_for_mp3 = os.listdir(desktop_path)
                        for each_file in ldesktop_for_mp3:
                            ext = get_extention(each_file)
                            if ext == '.mp3' or ext == '.MP3':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'MP3' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.mp4' in list_of_desktop_files or '.MP4' in list_of_desktop_files:
                        if check_if_desktop_MP4 == False:
                            os.mkdir(desktop_path_MP4)
                        ldesktop_for_mp4 = os.listdir(desktop_path)
                        for each_file in ldesktop_for_mp4:
                            ext = get_extention(each_file)
                            if ext == '.mp4' or ext == '.MP4':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'MP4' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.ico' in list_of_desktop_files or '.ICO' in list_of_desktop_files:
                        if check_if_desktop_ICO == False:
                            os.mkdir(desktop_path_ICO)
                        ldesktop_for_ico = os.listdir(desktop_path)
                        for each_file in ldesktop_for_ico:
                            ext = get_extention(each_file)
                            if ext == '.ico' or ext == '.ICO':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'ICO' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.PNG' in list_of_desktop_files or '.png' in list_of_desktop_files:
                        if check_if_desktop_PNG == False:
                            os.mkdir(desktop_path_PNG)
                        ldesktop_for_png = os.listdir(desktop_path)
                        for each_file in ldesktop_for_png:
                            ext = get_extention(each_file)
                            if ext == '.PNG' or ext == '.png':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'PNG' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    if '.py' in list_of_desktop_files or '.PY' in list_of_desktop_files:
                        if check_if_desktop_py == False:
                            os.mkdir(desktop_path_py)
                        ldesktop_for_py = os.listdir(desktop_path)
                        for each_file in ldesktop_for_py:
                            ext = get_extention(each_file)
                            if ext == '.py' or ext == '.PY':
                                og_exe_path = desktop_path + "\\" + each_file
                                desktop_path = desktop_path + "\\" + 'Python' + "\\" + each_file
                                shutil.move(og_exe_path, desktop_path)
                    # print(os.listdir(r'C:\Users\roni_\Desktop'))
                except Exception:
                    main_desktop()

            def main_downloads():
                try:
                    downloads_path = r'C:\Users\%s\Downloads' % username
                    # while True:
                    ########################################################
                    check_if_downloads_exe = os.path.isdir(downloads_path_exe)
                    check_if_downloads_lnk = os.path.isdir(downloads_path_lnk)
                    check_if_downloads_txt = os.path.isdir(downloads_path_txt)
                    check_if_downloads_url = os.path.isdir(downloads_path_url)
                    check_if_downloads_MP3 = os.path.isdir(downloads_path_MP3)
                    check_if_downloads_MP4 = os.path.isdir(downloads_path_MP4)
                    check_if_downloads_ICO = os.path.isdir(downloads_path_ICO)
                    check_if_downloads_PNG = os.path.isdir(downloads_path_PNG)
                    check_if_downloads_py = os.path.isdir(downloads_path_py)
                    ########################################################
                    time.sleep(.01)
                    list_of_downloads_files = []
                    for each_file in ldownloads:
                        # print(each_file)
                        extent = get_extention(each_file)
                        if extent != '-+':
                            list_of_downloads_files.append(extent)

                    if '.exe' in list_of_downloads_files or '.EXE' in list_of_downloads_files:
                        if check_if_downloads_exe == False:
                            os.mkdir(downloads_path_exe)
                        ldownloads_for_exe = os.listdir(downloads_path)
                        for each_file in ldownloads_for_exe:
                            ext = get_extention(each_file)
                            if ext == '.exe' or ext == '.EXE':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'EXE' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.lnk' in list_of_downloads_files or '.LNK' in list_of_downloads_files:
                        if check_if_downloads_lnk == False:
                            os.mkdir(downloads_path_lnk)
                        ldownloads_for_lnk = os.listdir(downloads_path)
                        for each_file in ldownloads_for_lnk:
                            ext = get_extention(each_file)
                            if ext == '.lnk' or ext == '.LNK':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'Shortcuts' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.TXT' in list_of_downloads_files or '.txt':
                        if check_if_downloads_txt == False:
                            os.mkdir(downloads_path_txt)
                        ldownloads_for_txt = os.listdir(downloads_path)
                        for each_file in ldownloads_for_txt:
                            ext = get_extention(each_file)
                            if ext == '.TXT' or ext == '.txt':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'TXT' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.url' in list_of_downloads_files or '.URL' in list_of_downloads_files:
                        if check_if_downloads_url == False:
                            os.mkdir(downloads_path_url)
                        ldownloads_for_url = os.listdir(downloads_path)
                        for each_file in ldownloads_for_url:
                            ext = get_extention(each_file)
                            if ext == '.url' or ext == '.URL':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'Games' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.mp3' in list_of_downloads_files or '.MP3' in list_of_downloads_files:
                        if check_if_downloads_MP3 == False:
                            os.mkdir(downloads_path_MP3)
                        ldownloads_for_mp3 = os.listdir(downloads_path)
                        for each_file in ldownloads_for_mp3:
                            ext = get_extention(each_file)
                            if ext == '.mp3' or ext == '.MP3':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'MP3' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.mp4' in list_of_downloads_files or '.MP4' in list_of_downloads_files:
                        if check_if_downloads_MP4 == False:
                            os.mkdir(downloads_path_MP4)
                        ldownloads_for_mp4 = os.listdir(downloads_path)
                        for each_file in ldownloads_for_mp4:
                            ext = get_extention(each_file)
                            if ext == '.mp4' or ext == '.MP4':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'MP4' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.ico' in list_of_downloads_files or '.ICO' in list_of_downloads_files:
                        if check_if_downloads_ICO == False:
                            os.mkdir(downloads_path_ICO)
                        ldownloads_for_ico = os.listdir(downloads_path)
                        for each_file in ldownloads_for_ico:
                            ext = get_extention(each_file)
                            if ext == '.ico' or ext == '.ICO':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'ICO' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.PNG' in list_of_downloads_files or '.png' in list_of_downloads_files:
                        if check_if_downloads_PNG == False:
                            os.mkdir(downloads_path_PNG)
                        ldownloads_for_png = os.listdir(downloads_path)
                        for each_file in ldownloads_for_png:
                            ext = get_extention(each_file)
                            if ext == '.PNG' or ext == '.png':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'PNG' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    if '.py' in list_of_downloads_files or '.PY' in list_of_downloads_files:
                        if check_if_downloads_py == False:
                            os.mkdir(downloads_path_py)
                        ldownloads_for_py = os.listdir(downloads_path)
                        for each_file in ldownloads_for_py:
                            ext = get_extention(each_file)
                            if ext == '.py' or ext == '.PY':
                                og_exe_path = downloads_path + "\\" + each_file
                                downloads_path = downloads_path + "\\" + 'Python' + "\\" + each_file
                                shutil.move(og_exe_path, downloads_path)
                    # print(os.listdir(r'C:\Users\roni_\Desktop'))
                except Exception:
                    main_desktop()

            main_desktop()
            main_downloads()
        except Exception as p:
            print(p)
            time.sleep(10)


    def listen_for_keys():
        while True:
            time.sleep(0.01)
            if keyboard.is_pressed('Control + Shift + Tab'):
                main_program()


    listen_for_keys_thread = threading.Thread(target=listen_for_keys)
    listen_for_keys_thread.start()
except Exception as e:
    print(e)
    time.sleep(100)