import mysql.connector
from geopy.distance import geodesic
def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='aleksandra',
        password='H6nckrxfRMz',
        autocommit=True
    )
    cursor = connection.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    return result

def run_airport_distance():
    icao_code_1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code_2 = input("Enter the ICAO code of the second airport: ").upper()

    coords1 = get_airport_coordinates(icao_code_1)
    coords2 = get_airport_coordinates(icao_code_2)

    if not coords1:
        print(f"Airport with ICAO code {icao_code_1} not found in the database.")
        return
    if not coords2:
        print(f"Airport with ICAO code {icao_code_2} not found in the database.")
        return
    distance = geodesic(coords1, coords2).kilometers
    print(f"\n\nDistance between {icao_code_1} and {icao_code_2}: {distance:.2f} kilometers")
run_airport_distance()
