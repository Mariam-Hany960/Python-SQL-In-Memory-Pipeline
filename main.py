import sqlite3

import pandas as pd

import tkinter as tk

from tkinter import filedialog



root = tk.Tk()

root.withdraw()

root.attributes('-topmost', True)

file_path = filedialog.askopenfilename(

    title="Select Your Excel File",

    filetypes=[("Excel files", "*.xlsx *.xls")]

)



df = pd.read_excel(file_path)



conn = sqlite3.connect(':memory:')



df.to_sql('SalesTable', conn, index=False, if_exists='replace')



def run_query(query_title, query):

    print(f"\n==================================================")

    print(f"📊 {query_title}")

    print(f"==================================================")

    result = pd.read_sql_query(query, conn)

    print(result.to_string(index=False))



run_query("Data Extraction (SELECT)", """

SELECT OrderID, CustomerID, Product, Quantity, TotalPrice 

FROM SalesTable 

LIMIT 10;

""")



run_query("WHERE Clause - Equality (Desk Only)", """

SELECT OrderID, Product, Quantity, TotalPrice 

FROM SalesTable 

WHERE Product = 'Desk'

LIMIT 10;

""")



run_query("WHERE Clause - Comparison (TotalPrice > 1500)", """

SELECT OrderID, Product, Quantity, TotalPrice 

FROM SalesTable 

WHERE TotalPrice > 1500.00

LIMIT 10;

""")



run_query("Pattern Matching (ReferralSource LIKE 'In%')", """

SELECT OrderID, Product, ReferralSource, TotalPrice 

FROM SalesTable 

WHERE ReferralSource LIKE 'In%'

LIMIT 10;

""")



run_query("GROUP BY & SUM (Total Revenue per Product)", """

SELECT Product, SUM(TotalPrice) AS TotalRevenue 

FROM SalesTable 

GROUP BY Product;

""")



run_query("COUNT & AVG Aggregations per Payment Method", """

SELECT PaymentMethod, COUNT(OrderID) AS TotalOrders, AVG(TotalPrice) AS AverageOrderValue 

FROM SalesTable 

GROUP BY PaymentMethod;

""")



run_query("ORDER BY (Products Ranked by Revenue DESC)", """

SELECT Product, SUM(Quantity) AS TotalUnitsSold, SUM(TotalPrice) AS TotalRevenue 

FROM SalesTable 

GROUP BY Product 

ORDER BY TotalRevenue DESC;

""")



conn.close() 

