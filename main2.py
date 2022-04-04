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

currents_valute = ["USD", "EUR", "GBP"]
# создаем словарь

# Размеры и положение появления окна Ширина * Высота 
root.geometry('550x1000')
# Меняем заголовок окна
root.title('Конвертер волют')
# Меняем иконку окна
root.iconbitmap(f'{Path.cwd()}/currency.ico')
root.resizable(False, False)

START_AMOUNT: int = 1000





try:
    html = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
    data = html.read()
    JSON_object = json.loads(data)
    currency = JSON_object['Valute']
    print(JSON_object)
except:
    messagebox.showerror("Error", "Ошибка получения курса валют")
    root.destroy()


# function
i = 0


def exchange():
    for cur_del in currents_valute:
        cur_d = f'e_{cur_del}'.lower()
        print(cur_del == f'e_{cur_del}')
        globals()[cur_d].delete(0, END)
        try:
            for cur_in in currency.items():
                if cur_del in cur_in[1]['CharCode']:
                    globals()[cur_d].insert(0, round(float(e_rur.get()) / float(cur_in[1]['Value']), 2))
        except:
            messagebox.showwarning('Warning', 'Проверьте введенную сумму')



# Header Frame
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Header
Label(header_frame, text="Дата изминения:", bg="#000", fg="#fff", font="Arial 12 bold").grid(row=0, column=0, sticky=EW)
Label(header_frame, text=JSON_object['Date'], bg="#ccc", font="Arial 12").grid(row=0, column=1, columnspan=2, sticky=EW)

h_currency = Label(header_frame, text="Валюта", bg="#ccc", font="Arial 12 bold")
h_currency.grid(row=1, column=0, sticky=EW)
h_buy = Label(header_frame, text="Покупка", bg="#ccc", font="Arial 12 bold")
h_buy.grid(row=1, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Arial 12 bold")
h_sale.grid(row=1, column=2, sticky=EW)

row: int = 2
column: int = 0
for cur in currency.items():
    if row % 2:
        bg_label = "#ccc"
    else:
        bg_label = "#fff"

    for current_cur in currents_valute:
        if current_cur in cur[1]['CharCode']:
            if column == 0:
                Label(header_frame, text=f"{cur[1]['Name']} | {cur[1]['CharCode']}", bg=bg_label, font="Arial 10",
                      anchor='w', padx=5).grid(row=row, column=column, sticky=EW)
                column += 1
            if column == 1:
                Label(header_frame, text="-", bg=bg_label, font="Arial 10").grid(row=row, column=column, sticky=EW)
                column += 1
            if column == 2:
                Label(header_frame, text=round(cur[1]['Value'], 2), bg=bg_label, font="Arial 10").grid(row=row, column=column, sticky=EW)
                column += 1
    if column == 3:
        column = 0
        row += 1

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
# Рузльтат
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

row_res = 2
column_res = 0
for cur in currency.items():
    for current_cur in currents_valute:
        if current_cur in cur[1]['CharCode']:
            str_cur_l = f'l_{current_cur}'.lower()
            str_cur =  f'e_{current_cur}'.lower()
            locals()[str_cur_l] = Label(res_frame, text=f"{cur[1]['CharCode']}:", font="Arial 10 bold")
            locals()[str_cur_l].grid(row=row_res, column=column_res)
            column_res += 1
            globals()[str_cur] = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
            globals()[str_cur].grid(row=row_res, column=column_res, columnspan=1, padx=10, sticky=EW)
            globals()[str_cur].insert(0, round((START_AMOUNT / cur[1]['Value']), 2))
            column_res += 1
    if column_res == 2:
        column_res = 0
        row_res += 1

root.mainloop()
