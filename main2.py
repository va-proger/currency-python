from locale import currency
from textwrap import fill
from tkinter import *
from pathlib import Path
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox
from PIL import Image as i
# рекомендуется называть переменную "root"
root = Tk()

# создаем словарь

# Размеры и положение появления окна Ширина * Высота 
root.geometry('500x1000')
# Меняем заголовок окна
root.title('Конвертер волют')
# Меняем иконку окна
root.iconbitmap(f'{Path.cwd()}/currency.ico')
root.resizable(False, False)

START_AMOUNT = 1


# function
def exchange():
    pass

try:
    html = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
    data = html.read()
    JSON_object = json.loads(data)
    currency = JSON_object['Valute']
    print(JSON_object)
except:
    messagebox.showerror("Error", "Ошибка получения курса валют")
    root.destroy()


# Header Frame
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)
header_frame.grid_columnconfigure(3, weight=1)

# Header
h_currency_date = Label(header_frame, text="Дата изминения:", bg="#000", fg="#fff", font="Arial 12 bold").grid(row=0, column=0,  sticky=EW)
h_currency_date_text = Label(header_frame, text=JSON_object['Date'], bg="#ccc", font="Arial 12").grid(row=0, column=1, columnspan=2, sticky=EW)


h_currency = Label(header_frame, text="Валюта", bg="#ccc", font="Arial 12 bold")
h_currency.grid(row=1, column=0, sticky=EW)
h_buy = Label(header_frame, text="Покупка", bg="#ccc", font="Arial 12 bold")
h_buy.grid(row=1, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Arial 12 bold")
h_sale.grid(row=1, column=2, sticky=EW)


row = 2
column = 0
for cur in currency.items():
    if column == 0:
        Label(header_frame, text=cur[1]['CharCode'], font="Arial 10").grid(row=row, column=column, sticky=EW)
        column += 1
    if column == 1:
        Label(header_frame, text=cur[1]['Value'], font="Arial 10").grid(row=row, column=column, sticky=EW)
        column += 1
    if column == 2:
        Label(header_frame, text="-", font="Arial 10").grid(row=row, column=column, sticky=EW)
        column += 1
    if column == 3:
        python_image = PhotoImage(file=f'{Path.cwd()}/flag/NOT.png')
        Label(header_frame, image=python_image).grid(row=row, column=column, sticky=EW)
        column += 1

    if column == 4:
        column = 0
        row += 1
   # Label(header_frame, text="USD", font="Arial 10").grid(row=1, column=0, sticky=EW)


# calc frame
calc_frame = Frame(root, bg="#fff")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)
#
# RUR
l_rur = Label(calc_frame, text="Рубль:", bg="#fff", font="Arial 10 bold")
l_rur.grid(row=0, column=0, padx=10)
e_rur = ttk.Entry(calc_frame, justify=CENTER, font="Arial 10")
e_rur.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_rur.insert(0, START_AMOUNT)

# button
btn_calc = ttk.Button(calc_frame, text="Обмен", command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)
#
# # Рузльтат
# res_frame = Frame(root)
# res_frame.pack(expand=1, fill=BOTH, pady=5)
# res_frame.grid_columnconfigure(1, weight=1)
#
# # USD
# l_usd = Label(res_frame, text="USD:", font="Arial 10 bold")
# l_usd.grid(row=2, column=0)
# e_usd = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
# e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
# e_usd.insert(0, "25000")
#
# # USD
# l_eur = Label(res_frame, text="EUR:", font="Arial 10 bold")
# l_eur.grid(row=3, column=0)
# e_eur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
# e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
# e_eur.insert(0, "25000")
#
# # GBR
# l_gbr = Label(res_frame, text="GBR:", font="Arial 10 bold")
# l_gbr.grid(row=4, column=0)
# e_gbr = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
# e_gbr.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)
# e_gbr.insert(0, "10000")

root.mainloop()
