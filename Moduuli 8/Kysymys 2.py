import mysql.connector

def get_airports_by_country(country_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='aleksandra',
        password='H6nckrxfRMz',
        autocommit=True
    )
    cursor = connection.cursor()
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    return result

def run_country_program():
    country_code_str = input("Enter the country code (e.g., FI for Finland): ").upper()
    results = get_airports_by_country(country_code_str)
    if not results:
        print(f"No airports found for country code '{country_code_str}'.")
        return
    print ("")
    print("")
    print(f"Airports in {country_code_str}:")
    for airport_type, count in results:
            print(f"{count} {airport_type} airports")

run_country_program()
