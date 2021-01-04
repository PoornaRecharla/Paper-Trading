from nsepy import get_history # get history for historical data
from datetime import date


data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31)) # symbol, start, end
data.to_csv('SBIN.csv', index = True) # to write to CSV

# data[['Close']].plot()

# Stock futures price history
# Set futures=True and provide expiry_date of the contract (Refer Fetching Expiry Dates)
# Stock futures (Similarly for index futures, set index = True)

stock_fut = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        futures=True,
                        expiry_date=date(2015,1,29))
stock_fut.to_csv('futures.csv', index = True)


# For stock options, specify-
# option_type as “CE” for call and as “PE” for put option
# strike_price - the strike price of the contract
# expiry_date - expiry date of the contract, refer:ref:get_expiry_date
# Stock options (Similarly for index options, set index = True)
stock_opt = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))

# Index price history
# symbol - Name of the index in capital (Refer this page for list of indices)
# NIFTY Next 50 index
nifty_next50 = get_history(symbol="NIFTY NEXT 50",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True)
# NIFTY50 Equal wight index (random index from the list)
nifty_eq_wt = get_history(symbol="NIFTY50 EQUAL WEIGHT",
                            start=date(2017,6,1),
                            end=date(2017,6,10),
                            index=True)

