# from nsepy import get_history # get history for historical data
# from datetime import date, timedelta

# import requests
# import json
# import csv
# import sqlite3


# mydb = sqlite3.connect("test2.db")

# mycursor = mydb.cursor()

# list1 = ['RELIANCE', 'TCS', 'HINDUNILVR', 'HDFCBANK']
# # list1 = ['RELIANCE', 'TCS', 'HINDUNILVR', 'HDFCBANK', 'HDFC', 'INFY', 'KOTAKBANK', 'BHARTIARTL', 'ITC', 'ICICIBANK', 'SBIN', 'ASIANPAINT', 'DMART', 'BAJFINANCE', 'MARUTI', 'HCLTECH', 'LT', 'WIPRO', 'AXISBANK', 'ULTRACEMCO', 'HDFCLIFE', 'COALINDIA', 'ONGC', 'SUNPHARMA', 'NTPC', 'POWERGRID', 'TITAN', 'DABUR', 'IOC', 'BAJAJFINSV', 'PIDILITIND', 'BPCL', 'HINDZINC', 'BRITANNIA', 'SBILIFE', 'SHREECEM', 'BAJAJ-AUTO', 'SBICARD', 'TECHM', 'GODREJCP', 'DIVISLAB', 'DRREDDY', 'ICICIPRULI', 'ADANIPORTS', 'ICICIGI', 'BERGEPAINT', 'HDFCAMC', 'GSKCONS', 'INDIGO', 'SIEMENS', 'EICHERMOT', 'MARICO', 'M&M', 'JSWSTEEL', 'MCDOWELL-N', 'GAIL', 'CIPLA', 'COLPAL', 'DLF', 'TORNTPHARM', 'PGHH', 'BANDHANBNK', 'BIOCON', 'HEROMOTOCO', 'GRASIM', 'AMBUJACEM', 'TATASTEEL', 'HAVELLS', 'PETRONET', 'INFRATEL', 'HINDPETRO', 'YESBANK', 'ALKEM', 'BOSCHLTD', 'CADILAHC', 'IGL', 'LUPIN', 'UPL', 'NAUKRI', 'LTI', 'BANKBARODA', 'MRF', 'MUTHOOTFIN', 'NMDC', 'INDUSINDBK', 'UBL', 'PFC', 'AUROPHARMA', 'VEDL', 'ADANIGREEN', 'WHIRLPOOL', 'HONAUT', 'TATAMOTORS', 'PNB', 'HINDALCO', 'GLAXO', '3MINDIA', 'PEL', 'KANSAINER', 'ADANITRANS']


# file1 = open("list.csv", "r")
# reader = csv.reader(file1)
# num = 0
# for row in reader:
# 	# if num > 10:
# 	# 	break
# 	sym = row[0]
# 	num += 1
# 	print(num, sym)
#     # mycursor.execute(f"""CREATE TABLE IF NOT EXISTS {i} (
# 	# 	"Date"	TEXT,
# 	# 	"Series"	TEXT,
# 	# 	"Prev"	NUMERIC,
# 	# 	"Open"	NUMERIC,
# 	# 	"High"	NUMERIC,
# 	# 	"Low"	NUMERIC,
# 	# 	"Last"	NUMERIC,
# 	# 	"Close"	NUMERIC,
# 	# 	"VWAP"	NUMERIC,
# 	# 	"Volume"	NUMERIC,
# 	# 	"Turnover"	NUMERIC,
# 	# 	"Trades"	NUMERIC,
# 	# 	"Deliverable"	NUMERIC,
# 	# 	"%Deliverble"	NUMERIC
# 	# 	)""")
# 	start_date = date(2020,1,1)
# 	end_date = date(2020,1,2)

# 	while start_date < end_date:
# 		end1 = min(start_date + timedelta(days=29), end_date)
# 		data = get_history(symbol=sym, start=start_date, end=end1) # symbol, start, end
# 		start_date = start_date + timedelta(days=30)
# 		data.to_sql("2020", mydb, if_exists='append', index = True)

#     # mycursor.execute(f"SELECT * FROM {i}")

#     # for row in mycursor.fetchall():
#     #     print (row)


# mydb.commit()
# mydb.close()


























# # data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,3)) # symbol, start, end
# # data1 = data.to_dict()

# # print(data1)

# # df = data

# # data1 = [df.columns.values.tolist()] + df.values.tolist()

# # data[['Close']].plot()
# # for row in data1:
# #     print (row)