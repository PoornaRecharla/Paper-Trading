import requests
import json
import csv
import sqlite3
import time

file1 = open("dict.csv", "r")
csv = csv.reader(file1)
list1 = [row[0] for row in csv]

# list1 = ["A","AA","AAA","AAAU","AACG","AACQ","AACQU","AACQW","AADR","AAIC","AAIC-P-B","AAIC-P-C","AAL","AAMC","AAME","AAN","AAN-W","AAOI","AAON","AAP","AAPL"]

mydb = sqlite3.connect("test.db")
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM company_master")
print("deleted")
mydb.commit()
mydb.close()

print(len(list1))


while len(list1) != 0:
    print('aaa')
    for sym in list1:
        print(len(list1))
        print(sym)
        # NFIR6BEIRX2TZ0LO
        response = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={sym}&apikey=NFIR6BEIRX2TZ0LO").json()

        # a = [a for a in response]

        keys = str([keys for keys in response])[1:-1]

        # print(keys)

        values = str([values for keys, values in response.items()])[1:-1]

        mydb = sqlite3.connect("test.db")

        mycursor = mydb.cursor()

        execute1 = f"INSERT INTO company_master ({keys}) VALUES ({values})"
        

        if len(response) > 0:
            if list(response.keys())[0] == "Note":
                # print(list(response.values()))
                print(list(response.values())[0])
                print("waiting a minute")
                for i in range(60):
                    print(i, end=" ")
                    time.sleep(1)
                    time1 += 1
            else:
                mycursor.execute(execute1)

        list1.remove(sym)
        # mycursor.execute("CREATE TABLE companies (Symbol TEXT PRIMARY KEY)")

        # abc = """INSERT INTO company_master ("Symbol", "AssetType", "Name", "Description", "Exchange", "Currency", "Country", "Sector", "Industry", "Address", "FullTimeEmployees", "FiscalYearEnd", "LatestQuarter", "MarketCapitalization", "EBITDA", "PERatio", "PEGRatio", "BookValue", "DividendPerShare", "DividendYield", "EPS", "RevenuePerShareTTM", "ProfitMargin", "OperatingMarginTTM", "ReturnOnAssetsTTM", "ReturnOnEquityTTM", "RevenueTTM", "GrossProfitTTM", "DilutedEPSTTM", "QuarterlyEarningsGrowthYOY", "QuarterlyRevenueGrowthYOY", "AnalystTargetPrice", "TrailingPE", "ForwardPE", "PriceToSalesRatioTTM", "PriceToBookRatio", "EVToRevenue", "EVToEBITDA", "Beta", "52WeekHigh", "52WeekLow", "50DayMovingAverage", "200DayMovingAverage", "SharesOutstanding", "SharesFloat", "SharesShort", "SharesShortPriorMonth", "ShortRatio", "ShortPercentOutstanding", "ShortPercentFloat", "PercentInsiders", "PercentInstitutions", "ForwardAnnualDividendRate", "ForwardAnnualDividendYield", "PayoutRatio", "DividendDate", "ExDividendDate", "LastSplitFactor", "LastSplitDate") VALUES ("IBM", "Common Stock", "International Business Machines Corporation", "International Business Machines Corporation provides integrated solutions and services worldwide. Its Cloud & Cognitive Software segment offers software for vertical and domain-specific solutions in health, financial services, and Internet of Things (IoT), weather, and security software and services application areas; and customer information control system and storage, and analytics and integration software solutions to support client mission critical on-premise workloads in banking, airline, and retail industries. It also offers middleware and data platform software, including Red Hat that enables the operation of clients' hybrid multi-cloud environments; and Cloud Paks, WebSphere distributed, and analytics platform software, such as DB2 distributed, information integration, and enterprise content management, as well as IoT, Blockchain and AI/Watson platforms. The company's Global Business Services segment offers business consulting services; system integration, application management, maintenance, and support services for packaged software; finance, procurement, talent and engagement, and industry-specific business process outsourcing services; and IT infrastructure and platform services. Its Global Technology Services segment provides project, managed, outsourcing, and cloud-delivered services for enterprise IT infrastructure environments; and IT infrastructure support services. The company's Systems segment offers servers for businesses, cloud service providers, and scientific computing organizations; data storage products and solutions; and z/OS, an enterprise operating system, as well as Linux. Its Global Financing segment provides lease, installment payment, loan financing, short-term working capital financing, and remanufacturing and remarketing services. The company was formerly known as Computing-Tabulating-Recording Co. The company was founded in 1911 and is headquartered in Armonk, New York.", "NYSE", "USD", "USA", "Technology", "Information Technology Services", "One New Orchard Road, Armonk, NY, United States, 10504", "352600", "December", "2020-09-30", "110794031104", "15690000384", "14.0927", "9.2577", "23.801", "6.52", "0.0527", "8.823", "84.402", "0.1053", "0.1205", "0.0372", "0.401", "75030003712", "36489000000", "8.823", "0.011", "-0.026", "137.13", "14.0927", "10.6496", "1.4879", "5.2389", "2.2111", "10.8346", "1.2399", "150.8394", "86.9458", "122.5185", "121.8803", "891057024", "889453213", "22915875", "23255478", "4.53", "0.03", "0.0257", "0.132", "58.644", "6.52", "0.0527", "0.5756", "2020-12-10", "2020-11-09", "2:1", "1999-05-27")"""

        # print(abc)
        # mycursor.execute(abc)

        mydb.commit()
        mydb.close()