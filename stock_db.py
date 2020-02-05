import sqlite3
import os

def create_db(df):
    for i in range(len(df['ID'])):
        path = 'C:/Users/user/Documents/stocks/{}.db'.format(df['ID'][i])
        if os.path.exists(path):
            pass
        else:
            conn = sqlite3.connect('C:/Users/user/Documents/stocks/{}.db'.format(df['ID'][i]))
            c = conn.cursor()
            c.execute("""CREATE TABLE price (
                        Date text,
                        Volume real,
                        Open real,
                        High real,
                        Low real,
                        Close real
                        )""")
            conn.commit()
            conn.close()


def insert_price(df):
    for i in range(len(df['ID'])):
        conn = sqlite3.connect('C:/Users/user/Documents/stocks/{}.db'.format(df['ID'][i]))
        c = conn.cursor()
        c.execute("INSERT INTO price VALUES (:Date, :Volume, :Open, :High, :Low, :Close)",
                  {'Date': df['Date'][i], 'Volume': df['Volume'][i], 'Open': df['Open'][i],
                   'High': df['High'][i], 'Low': df['Low'][i], 'Close': df['Close'][i]})
        conn.commit()
        conn.close()
