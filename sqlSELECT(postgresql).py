import psycopg2

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=*;DATABASE=*;UID=*;PWD=*')
cursor = conn.cursor()
query = """SELECT TOP 1200 [MessageID]
  FROM [EEC_MQ].[dbo].[MQMessages] where Action LIKE 'int://CP/P.TS.01/1.0.1/P.TS.01.PRC.001/P.TS.01.TRN.00%' 
and Direction = '0' order by ID desc"""


def iter_sql(result1):
    symbols = '(),'
    results = []
    for element in result1:
        temp = ""
        for ch in element:
            if ch not in symbols:
                temp += ch

        results.append(temp)
    return results


cursor.execute(query)
result1 = cursor.fetchall()
result1 = iter_sql(result1)
count = 0
for result in result1:
    exList1 = ''.join(result)
    query1 = f"SELECT count([ID]) FROM [EEC_MQ].[dbo].[MQMessages] where RelatesTo = '{exList1}'"
    cursor.execute(query1)
    result2 = cursor.fetchall()
    for result in result2:
        if result[0] == 2:
            count += 2
        else:
            count -= 2
if count == 2400:
    print(1)
else:
    print(0)
cursor.close()
conn.close()
