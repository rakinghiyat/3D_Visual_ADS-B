import csv
import json
import time
from urllib import request

def fetch_aircraft_data(url):
    try:
        response = request.urlopen(url)
        data = json.load(response)
        return data["acList"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def convert_to_csv_row(data):
    timestamp = int(time.time())
    return [
        "AITFC",
        data.get("Id", ""),
        data.get("Lat", ""),
        data.get("Long", ""),
        data.get("GAlt", ""),
        data.get("Vsi", ""),
        0 if data.get("Gnd", False) else 1,
        data.get("Trak", ""),
        data.get("Spd", ""),
        data.get("Call", ""),
        data.get("Type", ""),
        data.get("Reg", ""),
        data.get("From", "").split(" ")[0],
        data.get("To", "").split(" ")[0],
        timestamp,
    ]

def write_to_csv(filename, rows):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)

def main():
    json_url = "http://10.110.180.25/VirtualRadar/AircraftList.json?lat=-6.896348778173379&lng=107.57580757141115&fDstL=0&fDstU=185.20000000000002"
    csv_filename = r"D:\3D Visual\DataCSV.csv"
    id_queue = []
    interval = 1  # seconds

    while True:
        try:
            aircraft_data = fetch_aircraft_data(json_url)
            if not aircraft_data:
                time.sleep(interval)
                continue

            for data in aircraft_data:
                if data["Id"] not in id_queue:
                    id_queue.append(data["Id"])

            if id_queue:
                current_id = id_queue.pop(0)
                current_data = next(
                    (data for data in aircraft_data if data["Id"] == current_id), None
                )

                if current_data:
                    csv_row = convert_to_csv_row(current_data)
                    write_to_csv(csv_filename, [csv_row])

                print(f"Data update at {time.strftime('%d-%m-%Y %H:%M:%S')}")
                time.sleep(interval)

        except KeyboardInterrupt:
            print("Program terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    main()
