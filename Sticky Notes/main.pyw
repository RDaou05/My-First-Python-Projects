import time


try:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import Frame
    from tkinter import Text
    from tkinter import Label
    from tkinter import Scrollbar
    from tkinter.constants import RIGHT, X
    from functools import partial
    import tkinter.font as font
    from tkinter import Canvas
    from tkinter import ttk
    import os
    import re
    import sys
    import subprocess
    import getpass
    import shutil

    def main():
        def setup():
            global username
            global path_of_notes_folder
            global path_of_dolm_file
            username = getpass.getuser()
            path_of_notes_folder = fr'C:\Users\{username}\Notes'
            path_of_dolm_folder = fr'C:\Users\{username}\DOLM'
            path_of_dolm_file = path_of_dolm_folder + "\\dol.txt"
            if os.path.isdir(path_of_notes_folder) == False:
                os.mkdir(path_of_notes_folder)
            else:
                pass
            if os.path.isdir(path_of_dolm_folder) == False:
                os.mkdir(path_of_dolm_folder)
            else:
                pass
            if os.path.isfile(path_of_dolm_file) == False:
                with open(path_of_dolm_file, 'w') as temp:
                    temp.write('l')
                    temp.close()
            else:
                pass

        def set_color_reg():
            global yellow_color
            global gray_color
            global black_color
            global light_mode_on

            with open(path_of_dolm_file, 'r') as dol_check:
                dol_check_content = str(dol_check.read())
                dol_check.close()
                if 'l' in dol_check_content:
                    light_mode_on = True
                    yellow_color = '#fff7d1'
                    gray_color = '#eeeeee'
                    black_color = '#000000'
                elif 'd' in dol_check_content:
                    light_mode_on = False
                    yellow_color = '#333333'
                    gray_color = '#e6b905'
                    black_color = '#000000'

        def new_note():
            def register_new_note():
                global new_note_name

                current_amount_of_notes = len(os.listdir(path_of_notes_folder))
                new_note_name = f'Note {current_amount_of_notes + 1}.txt'
                with open(f'{path_of_notes_folder}\\{new_note_name}', 'w') as new_note_txt:
                    new_note_txt.close()
            register_new_note()
            frame = tk.Tk()
            frame.title("TextBox Input")
            frame.geometry('400x210')
            frame.config(bg=yellow_color)
            frame.resizable(False, False)

            def save_note():
                inp = inputtxt.get(1.0, "end-1c")
                # print(inp)
                with open(f'{path_of_notes_folder}\\{new_note_name}', 'w') as new_note_txt:
                    new_note_txt.write(inp)
                    new_note_txt.close()
                frame.destroy()
                root.destroy()
                main()

            if light_mode_on == False:
                inputtxt = tk.Text(frame,
                                   height=11,
                                   width=49, bg=yellow_color, fg=gray_color)
            else:
                inputtxt = tk.Text(frame,
                                   height=11,
                                   width=49, bg=yellow_color)
            inputtxt.pack()
            if light_mode_on == False:
                saveButton = tk.Button(frame,
                                       text="Save",
                                       command=save_note, bg=gray_color, fg=yellow_color)
            elif light_mode_on == True:
                saveButton = tk.Button(frame,
                                       text="Save",
                                       command=save_note, bg=gray_color, fg=black_color)
            saveButton.pack(side=tk.BOTTOM)
            frame.mainloop()

        def view_notes_func(note_number_to_rewrite):
            reframe = tk.Tk()
            reframe.title("TextBox Input")
            reframe.geometry('400x210')
            reframe.config(bg=yellow_color)
            reframe.resizable(False, False)

            def resave_note():
                inp = inputtxt.get(1.0, "end-1c")
                # print(inp)
                # print(note_number_to_rewrite)
                with open(f'{path_of_notes_folder}\\Note {note_number_to_rewrite}.txt', 'w') as new_note_txt:
                    new_note_txt.write(inp)
                    new_note_txt.close()
                reframe.destroy()
                root.destroy()
                main()

            if light_mode_on == False:
                inputtxt = tk.Text(reframe,
                                   height=11,
                                   width=49, bg=yellow_color, fg=gray_color)
            else:
                inputtxt = tk.Text(reframe,
                                   height=11,
                                   width=49, bg=yellow_color)

            def get_note_content():
                global note_content_to_display
                with open(f'{path_of_notes_folder}\\Note {note_number_to_rewrite}.txt', 'r') as note_reading:
                    note_content_to_display = str(note_reading.read())
                    note_reading.close()
            get_note_content()
            inputtxt.insert(1.0, note_content_to_display)
            inputtxt.pack()
            if light_mode_on == False:
                saveButton = tk.Button(reframe,
                                       text="Save",
                                       command=resave_note, bg=gray_color, fg=yellow_color)
            elif light_mode_on == True:
                saveButton = tk.Button(reframe,
                                       text="Save",
                                       command=resave_note, bg=gray_color, fg=black_color)
            saveButton.pack(side=tk.BOTTOM)
            saveButton.pack(side=tk.BOTTOM)
            reframe.mainloop()

        def update_note_names():
            global path_of_notes_folder

            username = getpass.getuser()
            path_of_notes_folder = fr'C:\Users\{username}\Notes'
            dir_list_of_notes = []
            for note_name in os.listdir(path_of_notes_folder):
                dir_list_of_notes.append(
                    path_of_notes_folder + "\\" + note_name)
            temp_note_num = 0
            for note_dir in dir_list_of_notes:
                temp_note_num += 1
                os.rename(note_dir, path_of_notes_folder +
                          f"\\Note {temp_note_num}.txt")

        def delete_note(note_num):
            path_of_note_to_delete = f'{path_of_notes_folder}\\Note {note_num}.txt'
            os.remove(path_of_note_to_delete)
            update_note_names()
            root.destroy()
            main()

        def refresh_root():
            root.destroy()
            main()

        def color_mode():
            global yellow_color
            global gray_color
            global black_color
            global light_mode_on
            #
            # username = getpass.getuser()
            # path_of_notes_folder = fr'C:\Users\{username}\Notes'
            # path_of_dolm_folder = fr'C:\Users\{username}\DOLM'
            # path_of_dolm_file = path_of_dolm_folder + "\\dol.txt"
            #

            with open(path_of_dolm_file, 'r') as dol_check:
                dol_check_content = str(dol_check.read())
                dol_check.close()
                if 'l' in dol_check_content:
                    dol_check.close()
                    light_mode_on = True
                    with open(path_of_dolm_file, 'w') as dol_write:
                        dol_write.write('d')
                        dol_write.close()
                    yellow_color = '#fff7d1'
                    gray_color = '#eeeeee'
                    black_color = '#000000'
                elif 'd' in dol_check_content:
                    light_mode_on = False
                    dol_check.close()
                    with open(path_of_dolm_file, 'w') as dol_write:
                        dol_write.write('l')
                        dol_write.close()
                    yellow_color = '#333333'
                    gray_color = '#e6b905'
                    black_color = '#000000'
                else:
                    pass
            try:
                refresh_root()
            except:
                pass

        def main_window():
            global root

            class VerticalScrolledFrame(tk.Frame):
                def __init__(self, parent, *args, **kw):
                    tk.Frame.__init__(self, parent, *args, **kw)

                    # create a canvas object and a vertical scrollbar for scrolling it
                    vscrollbar = tk.Scrollbar(
                        self, orient=tk.VERTICAL, bg=yellow_color)
                    vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
                    canvas = tk.Canvas(self, bd=30, highlightthickness=0,
                                       yscrollcommand=vscrollbar.set, bg=yellow_color, height=2100000000)
                    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
                    vscrollbar.config(command=canvas.yview)

                    # reset the view
                    canvas.xview_moveto(0)
                    canvas.yview_moveto(0)

                    # create a frame inside the canvas which will be scrolled with it
                    self.interior = interior = tk.Frame(
                        canvas, bg=yellow_color)
                    interior_id = canvas.create_window(0, 0, window=interior,
                                                       anchor=tk.NW)

                    # track changes to the canvas and frame width and sync them,
                    # also updating the scrollbar
                    def _configure_interior(event):
                        # update the scrollbars to match the size of the inner frame
                        size = (interior.winfo_reqwidth(),
                                interior.winfo_reqheight())
                        canvas.config(scrollregion="0 0 %s %s" %
                                      size, bg=yellow_color)
                        if interior.winfo_reqwidth() != canvas.winfo_width():
                            # update the canvas's width to fit the inner frame
                            canvas.config(width=interior.winfo_reqwidth())

                    interior.bind('<Configure>', _configure_interior)

                    def _configure_canvas(event):
                        if interior.winfo_reqwidth() != canvas.winfo_width():
                            # update the inner frame's width to fill the canvas
                            canvas.itemconfigure(
                                interior_id, width=canvas.winfo_width())
                    canvas.bind('<Configure>', _configure_canvas)

            root = tk.Tk()
            root.title('Notes')
            #root.iconbitmap('notes_picture.ico')
            root.config(bg=yellow_color)
            root.geometry("371x410")
            root.resizable(False, False)
            scframe = VerticalScrolledFrame(root)
            scframe.pack()
            empty_line2 = tk.Label(scframe.interior, text="", width=7, height=20,
                                   bg=yellow_color)
            empty_line2.pack(side=tk.RIGHT, anchor=tk.NE)
            # sb = Scrollbar(
            #     root, orient=tk.VERTICAL)

            # sb.grid(row=0, column=1, sticky=tk.NS)

            # root.config(yscrollcommand=sb.set)
            # sb.config(command=root.yview)

            new_note_button_font = font.Font(size=13, weight='bold')
            new_note_button = tk.Button(scframe.interior, text="+", command=new_note,
                                        width=5, height=2, bg=gray_color, font=new_note_button_font)
            # fr = Frame(width=200, height=51, border=0,
            #            highlightthickness=0)
            title_on_right = font.Font(size=12, weight='bold')
            fill_button = tk.Button(scframe.interior, text="Sticky Notes",
                                    font=title_on_right, height=2, width=23, command=color_mode, bg=gray_color)

            # test_button = tk.Button(text="testing", width=4, height=2,
            #                         fg='#0e12f1')
            # test_button1 = tk.Button(text="testing", width=4, height=2,
            #                          fg='#0e12f1')

            new_note_button.place(x=0, y=0)
            fill_button.pack(side=tk.TOP, anchor=tk.NE)
            amount_of_notes = len(os.listdir(path_of_notes_folder))
            note_number_for_loop = 0
            y_coord_for_delete_buttton = 0
            for note in os.listdir(path_of_notes_folder):
                y_coord_for_delete_buttton += 96
                note_number_for_loop += 1
                with open(path_of_notes_folder + '\\' + note, 'r') as note_read:
                    note_content = str(note_read.read())
                    if len(list(note_content)) <= 20:
                        first_characters = note_content
                    else:
                        first_characters = ''.join(
                            list(note_content)[i] for i in range(20))
                    note_read.close()
                    if '\n' in first_characters:
                        first_characters = first_characters.replace('\n', ' ')

                def pack_show_note_buttons(button_num_for_notes):
                    note_box_font = font.Font(size=13)
                    # print(button_num_for_notes)

                    button_num_for_notes = tk.Button(scframe.interior, text=f'         {first_characters}', width=30, height=2,
                                                     fg=black_color, bg=gray_color, font=note_box_font, command=partial(view_notes_func, note_number_for_loop))
                    delete_button_font = font.Font(size=12)
                    delete_button = tk.Button(
                        scframe.interior, text="-", width=5, height=2, font=delete_button_font, bg=gray_color, command=partial(delete_note, note_number_for_loop))
                    empty_line = tk.Label(scframe.interior, text="", width=30, height=2,
                                          bg=yellow_color, font=note_box_font)
                    empty_line.pack()
                    button_num_for_notes.pack()
                    delete_button.place(x=10, y=y_coord_for_delete_buttton)
                pack_show_note_buttons(str(note_number_for_loop) + 'button')

            root.mainloop()

        setup()
        set_color_reg()
        main_window()

    main()
except Exception as e:
    print(e)
