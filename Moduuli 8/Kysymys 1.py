import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksandra',
         password='H6nckrxfRMz',
         autocommit=True
         )

icao_code_str = input("Enter the ICAO code of an airport: ").upper()

cursor = connection.cursor()
sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao_code_str,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}\nLocation: {result[1]}")
else:
    print(f"No airport found with ICAO code {icao_code_str}")

