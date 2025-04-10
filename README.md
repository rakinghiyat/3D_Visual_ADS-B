# 3D_Visual_ADS-B ✈️🛰️

This project enables real-time 3D visualization of ADS-B flight data using the X-Plane flight simulator. By parsing aircraft data from a CSV file, the system transmits the traffic to X-Plane, allowing you to view and analyze real-world flight movements in a 3D simulated environment.

---

## 🌍 Use Case

- Simulate real aircraft positions inside X-Plane based on ADS-B receiver data
- Visualize and analyze air traffic in 3D for research or training
- Extend realism of simulation environments with live or recorded flight data

---

## 🛠️ Requirements

- Python 3.x
- X-Plane 11 or later
- X-Plane plugin that allows dataref injection (e.g., X-Plane SDK or XUIPC)
- Python libraries:
  - `pandas`
  - `socket`
  - `json`
  - `time`

---

## 🚀 How It Works

1. **Collect ADS-B flight data** (e.g., from FlightAware or local receiver).
2. **Format it as a CSV** like the provided `DataCSV.csv` sample.
3. **Run `SendTraffic.py`** to send aircraft position data to X-Plane via UDP.
4. **Observe in X-Plane** as virtual aircraft appear and follow their real-world paths.

---

## 📊 CSV Format Example

Each row in `DataCSV.csv` should contain:

- ICAO address
- Latitude
- Longitude
- Altitude
- Track
- Speed

_(Adjust your parser if using a different format.)_

---

## 🔧 Configuration

Ensure that X-Plane is listening on the correct UDP port and accepts external data. You may need to adjust IP address and port settings in `SendTraffic.py`.

---

## 📄 RTdev2.0.pdf

This document contains design concepts, flowcharts, and additional notes on the development process of this 3D visualization system.

---

## 📌 Future Improvements

- Real-time connection to Virtual Radar Server (VRS) JSON feed
- Enhanced visualization via aircraft models
- Flight history recording and replay
- Web-based control or dashboard

---

## 🧠 Author

Created by [rakinghiyat](https://github.com/rakinghiyat), an enthusiast in aircraft systems, telemetry, and simulation-based innovation.

---

## 📄 License

MIT License - Feel free to use or adapt for educational and research purposes.
