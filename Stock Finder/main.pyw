from tkinter import font
from tkinter.constants import NO
from bs4 import BeautifulSoup
import requests
import time
from requests.api import request
import tkinter as tk
from tkinter import *


def find_stock(ticker_to_search):
    if len(str(ticker_to_search).strip()) != 0:
        def get_ticker():
            global ticker

            ticker = ticker_to_search.upper()

        def navigation_setup():
            global soup
            global dom

            url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

        def get_stock_info():
            global final_info
            global no_val

            final_chart_info_list = []

            stock_price = soup.find_all(
                class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')[0].getText()
            print(stock_price)
            try:
                valued = soup.find(
                    class_='Fw(b) Fl(end)--m Fz(s) C($primaryColor').getText()
                no_val = False
            except AttributeError:
                no_val = True

            def get_up_down():
                global up_today

                try:
                    how_much_up_down = soup.find(
                        class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)').getText()
                    up_today = True
                except AttributeError:
                    how_much_up_down = soup.find(
                        class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)').getText()
                    up_today = False
                return how_much_up_down

            def get_elements_in_chart():
                chart_info = []
                chart_piece_titles_list = ['Previous Close', 'Open', 'Bid', 'Ask', "Day's Range", '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap',
                                           'Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est']
                for num in range(16):
                    chart_element = soup.find_all(
                        class_='Ta(end) Fw(600) Lh(14px)')[num].getText()
                    chart_info.append(chart_element)
                for chart_piece_num, chart_piece in enumerate(chart_info):
                    final_chart_info_list.append(
                        f'{chart_piece_titles_list[chart_piece_num]}: {chart_piece}')

            get_elements_in_chart()
            final_chart_info = '\n'.join(final_chart_info_list)
            if no_val:
                final_info = f'Stock Price: {stock_price}\n{get_up_down()}\n\n{final_chart_info}'
            else:
                final_info = f'Stock Price: {stock_price}\n{get_up_down()}\n\n{valued}\n{final_chart_info}'
        get_ticker()
        navigation_setup()
        get_stock_info()
        return final_info
    else:
        global up_today

        up_today = None
        return ''


def tkinter_settings():
    root = tk.Tk()
    root.resizable(False, False)

    # Search
    canvas1 = tk.Canvas(root, width=400, height=100,  relief='raised')
    canvas1.pack()

    # canvas1.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Enter stock ticker:')
    label2.config(font=('helvetica', 15))
    canvas1.create_window(200, 20, window=label2)

    entry1 = tk.Entry(root)
    canvas1.create_window(200, 50, window=entry1)

    def show_stock_res():
        global ticker_label
        global stock_info_label
        ticker_label_font = font.Font(size=30)
        ticker_label = tk.Label(root, text=entry1.get().upper(),
                                font=ticker_label_font)
        stock_info_label_font = font.Font(weight='bold')
        stock_info_label = tk.Label(
            root, text=f'{find_stock(entry1.get().upper())}', width=35, height=20, font=stock_info_label_font)

        ticker_label.pack()
        root.title(entry1.get().upper())
        stock_info_label.pack()
        entry1.delete(0, END)

        if up_today:
            color_bg = '#00c805'
        elif up_today == False:
            color_bg = '#ff5000'
        else:
            color_bg = '#f0f0f0'

        root.config(bg=color_bg)
        canvas1.config(bg=color_bg)
        stock_info_label.config(bg=color_bg)
        ticker_label.config(bg=color_bg)
        label2.config(bg=color_bg)

    def clear_func():
        try:
            ticker_label.pack_forget()
            stock_info_label.pack_forget()
        except NameError:
            pass

    def clear_and_show(event=None):
        clear_func()
        show_stock_res()
    root.bind('<Return>', clear_and_show)
    button1 = tk.Button(root, text='Search',
                        bg='brown', fg='white', font=('helvetica', 9, 'bold'), command=clear_and_show)
    canvas1.create_window(200, 80, window=button1)
    # Search

    root.mainloop()


tkinter_settings()
