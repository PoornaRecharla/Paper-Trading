from datetime import date
import sqlite3

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

from dateutil import parser

style.use('fivethirtyeight')

conn = sqlite3.connect('test.db')
c = conn.cursor()


list1 = ['RELIANCE', 'TCS', 'HINDUNILVR', 'HDFCBANK', 'HDFC', 'INFY', 'KOTAKBANK', 'BHARTIARTL', 'ITC', 'ICICIBANK', 'SBIN', 'ASIANPAINT', 'DMART', 'BAJFINANCE', 'MARUTI', 'HCLTECH', 'LT', 'WIPRO', 'AXISBANK']
list1 = ['ITC']

for row in list1[0:1]:
    query = f"""SELECT * FROM '2020' WHERE Symbol='{row}'""" 

    c.execute(query)
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[3])

    plt.plot_date(dates,values,'-')
    plt.show()





# TM = pd.read_sql(query, conn)

# plt.scatter(TM['Date'], TM['Close'])
# plt.xlabel("Date", fontsize = 16)
# plt.ylabel("Close", fontsize = 16)
# plt.title("SBIN", fontsize = 25)
# plt.show()





# def graph_data():
#     c.execute('SELECT ')



































# mydb = sqlite3.connect("test.db")
# mycursor = mydb.cursor()



# mycursor.execute("""SELECT * FROM '2020' WHERE Symbol='SBIN' AND Date<'2020-02-01' AND Date>'2019-01-01'""")

# asd = mycursor.fetchall()

# print(asd)


# # for row in mycursor.fetchall():
# #     print (row)




# mydb.commit()
# mydb.close()