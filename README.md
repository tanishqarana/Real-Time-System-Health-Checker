## Real-Time-System-Health-Checker
A real-time web app that monitors your system’s CPU, RAM, Disk, and Network usage, and updates live using WebSockets.

# Overview
The Real-Time System Health Dashboard is a Python-based web application that monitors and visualizes your system’s performance metrics — including CPU usage, Memory utilization, Disk space, and Network activity — in real time.
Built using Flask, Socket.IO, and Chart.js, the project continuously collects system data using the psutil library and streams updates to the frontend without page refreshes.

# Features : 
- Live System Monitoring — View CPU, RAM, Disk, and Network stats updating every second.
- WebSocket-Powered Updates — No manual refresh; metrics update instantly via Flask-SocketIO.
- Backend Efficiency — Optimized data polling with lightweight threads and async emissions.
- Dynamic Visualization — Interactive charts rendered using Chart.js with smooth animations.
- Multi-Client Sync — All connected dashboards receive updates simultaneously.

# Tech Stack :
- Backend -> Flask, FlaskSocketIO
- Data Collection -> psutil
- Fronted -> HTML, CSS, JS, Chart.js
- Version Control -> Git and GitHub

# Folder Structure : 
real-time-system-dashboard/
│
├── app.py                  # Main Flask + SocketIO app
├── system_metrics.py        # Collects live system data via psutil
├── templates/
│   └── index.html           # Dashboard frontend
├── static/
│   ├── style.css            # Styling and layout
│   └── scripts.js           # Chart.js logic and SocketIO events
├── requirements.txt         # Dependencies
├── .gitignore               # Ignore files and folders
└── README.md                # Project documentation

# Architecture : 
 ┌──────────────────────────────┐
 │          Frontend            │
 │  (HTML + JS + Chart.js)      │
 │  ↓ Receives live data        │
 └────────────┬─────────────────┘
              │ WebSocket (Socket.IO)
 ┌────────────┴─────────────────┐
 │           Backend            │
 │  Flask + Flask-SocketIO      │
 │  → Gathers system stats via  │
 │    psutil                    │
 │  → Emits JSON every second   │
 └────────────┬─────────────────┘
              │
 ┌────────────┴─────────────────┐
 │           System             │
 │  CPU, Memory, Disk, Network  │
 └──────────────────────────────┘
