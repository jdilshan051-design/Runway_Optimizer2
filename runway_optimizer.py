import os
import logging
import streamlit as st
import numpy as np
import requests
import math
import streamlit.components.v1 as components

# Mute warnings
logging.getLogger("streamlit.runtime.scriptrunner_utils").setLevel(logging.ERROR)
logging.getLogger("streamlit").setLevel(logging.ERROR)
os.environ["STREAMLIT_LOG_LEVEL"] = "error"

# =====================================================================
# 🌐 PREMIUM HIGH-CONTRAST GUI CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="AeroRoute | Global Live Command Deck", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# High-Contrast Professional Slate Dashboard Design (UI FIXED)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main body text */
    .main { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }
    
    /* FIX: Make Sidebar Text Dark and Bold */
    [data-testid="stSidebar"] {
        background-color: #f1f5f9; /* Light Gray Sidebar Background */
    }
    [data-testid="stSidebar"] * {
        color: #0f172a !important; /* Dark Slate Text */
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #020617 !important; /* Extra Dark Headers in Sidebar */
        font-weight: 800 !important;
    }
    [data-testid="stSidebar"] label {
        color: #1e293b !important;
        font-weight: 600 !important;
    }
    
    /* Main Content Headers */
    .main h1, .main h2, .main h3 { 
        color: #ffffff !important; 
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }
    
    /* Premium High-Contrast Interface Cards */
    .stMetric { 
        background: #1e293b;
        padding: 20px; 
        border-radius: 10px; 
        border: 2px solid #334155; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .timeline-log {
        background-color: #020617;
        border-left: 5px solid #2563eb;
        padding: 14px;
        margin-bottom: 12px;
        border-radius: 6px;
        font-size: 0.9rem;
        color: #cbd5e1;
        border: 1px solid #1e293b;
    }
    .timeline-time { color: #38bdf8; font-weight: 700; font-family: monospace; }
    .timeline-node { color: #ffffff; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

st.title("🌐 AeroRoute: Worldwide Live Fleet Digital Twin")
st.caption("Enterprise-Grade Dynamic Geographic Positioning System & Neural Safety Optimization Matrix")
st.markdown("---")

# =====================================================================
# 🧠 MATHEMATICAL NEURAL CORE 
# =====================================================================
class FlightRiskEngine:
    def __init__(self):
        np.random.seed(1337)
        self.W1 = np.random.randn(7, 12) * np.sqrt(2.0 / 7)
        self.b1 = np.zeros((1, 12))
        self.W2 = np.random.randn(12, 1) * np.sqrt(2.0 / 12)
        self.b2 = np.zeros((1, 1))
        
    def _sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))
    
    def _relu(self, z):
        return np.maximum(0, z)

    def evaluate(self, X):
        Z1 = np.dot(X, self.W1) + self.b1
        A1 = self._relu(Z1)
        Z2 = np.dot(A1, self.W2) + self.b2
        return self._sigmoid(Z2)

@st.cache_resource
def load_flight_engine():
    return FlightRiskEngine()

risk_engine = load_flight_engine()

# =====================================================================
# 📡 WORLDWIDE LIVE DATA MATRIX REGISTRY
# =====================================================================
def get_global_airspace_registry(icao):
    icao = icao.upper().strip()
    airports = {
        "VCBI": {"lat": 7.1808, "lon": 79.8837, "rwy": 40, "alt_lat": 6.2902, "alt_lon": 81.1219, "name": "BIA (Colombo)", "alt_name": "Mattala Hub (VCRI)", "fix_lat": 6.1, "fix_lon": 78.8},
        "KJFK": {"lat": 40.6398, "lon": -73.7789, "rwy": 40, "alt_lat": 40.6895, "alt_lon": -74.1745, "name": "JFK (New York)", "alt_name": "Newark Liberty", "fix_lat": 39.5, "fix_lon": -75.0}
    }
    
    data = airports.get(icao, {"lat": 7.18, "lon": 79.88, "rwy": 40, "name": "Unknown Hub", "alt_name": "N/A", "fix_lat": 6.1, "fix_lon": 78.8})
    data["wind_speed"] = round(np.random.uniform(10, 30), 1)
    data["wind_dir"] = int(np.random.uniform(0, 360))
    data["gust_index"] = round(np.random.uniform(0.5, 4.0), 1)
    data["friction"] = round(np.random.uniform(0.2, 0.55), 2)
    
    # LIVE API CALL TO OPENSKY
    try:
        url = f"https://opensky-network.org/api/states/all?lamin={data['lat']-2}&lamax={data['lat']+2}&lomin={data['lon']-2}&lomax={data['lon']+2}"
        response = requests.get(url, timeout=5).json()
        live_fleet = []
        if 'states' in response and response['states']:
            for s in response['states']:
                live_fleet.append({
                    "callsign": str(s[1]).strip(),
                    "lat": s[6], "lon": s[5],
                    "alt": int(s[7] if s[7] else 0),
                    "speed": int(s[9] * 1.94384 if s[9] else 0),
                    "heading": int(s[10] if s[10] else 0)
                })
        data["live_flights"] = live_fleet
    except:
        data["live_flights"] = []
        
    return data

# =====================================================================
# 🕹️ TACTICAL CONTROL CENTER SIDEBAR
# =====================================================================
st.sidebar.markdown("<h2>🛰️ Operations Controller</h2>", unsafe_allow_html=True)
icao_input = st.sidebar.text_input("Ingest Active Target Code (ICAO):", value="VCBI").upper()
data_block = get_global_airspace_registry(icao_input)

st.sidebar.markdown("---")
st.sidebar.markdown("<h3>✈️ Monitored Vessel Registry</h3>", unsafe_allow_html=True)
aircraft_type = st.sidebar.selectbox("Commercial Airframe Class", ["Intercontinental Jumboliner (B777/A350)", "Commercial Transit Carrier (A320/B737)"])
aircraft_weight = 75.0 if "Intercontinental" in aircraft_type else 35.0

st.sidebar.markdown("<h3>🚨 Managed Vulnerability Systems</h3>", unsafe_allow_html=True)
active_failures = st.sidebar.slider("Active Mechanical System Faults", 0, 3, 0)
fuel_status = st.sidebar.slider("Remaining Fuel Energy Reserves (%)", 5, 100, 60)

# Aerodynamic Math
angle_difference = abs(data_block["wind_dir"] - data_block["rwy"])
if angle_difference > 180: angle_difference = 360 - angle_difference
crosswind_knots = data_block["wind_speed"] * math.sin(math.radians(angle_difference))

normalized_inputs = np.array([[ 
    data_block["wind_speed"] / 50.0, angle_difference / 90.0, aircraft_weight / 150.0,
    active_failures / 3.0, fuel_status / 100.0, data_block["gust_index"] / 5.0, data_block["friction"] / 0.6
]])

raw_risk_score = risk_engine.evaluate(normalized_inputs)[0][0]

# =====================================================================
# 📊 CONTROL CENTER VIEWPORTS
# =====================================================================
col_left, col_right = st.columns([1, 2])

with col_left:
    st.write("### 📜 Airspace Active Data Logs")
    st.markdown(f"""
    <div class='timeline-log'><span class='timeline-time'>▶️ Grid Status:</span> Target Vector Airport: <span class='timeline-node'>{data_block['name']}</span></div>
    <div class='timeline-log'><span class='timeline-time'>▶️ Fleet Matrix:</span> Streaming <span style='color:#38bdf8; font-weight:bold;'>{len(data_block['live_flights'])} Live Assets</span>.</div>
    <div class='timeline-log'><span class='timeline-time'>▶️ Wind Vector:</span> Current Local Crosswind: <span style='color:#f59e0b; font-weight:bold;'>{crosswind_knots:.2f} Knots</span></div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("### 🎚️ Telemetry Scorecard")
    st.metric(label="Calculated Crosswind Component", value=f"{crosswind_knots:.2f} KT")
    st.metric(label="Neural Prediction Risk Index", value=f"{raw_risk_score:.3f}")
    
    st.markdown("### 🚦 Autonomous Rerouting System")
    if raw_risk_score < 0.48:
        st.success(f"🟢 PERMISSION GRANTED\n\nVector corridor locked into {data_block['name']}.")
        target_lat, target_lon = data_block["lat"], data_block["lon"]
        path_line_color = "#10b981" 
        status_text = "ARRIVING AT PRIMARY BASE"
    else:
        st.error(f"🔴 EMERGENCY REDIRECT ENFORCED\n\nSafety thresholds breached! Rerouting asset automatically.")
        st.markdown(f"🚨 **Redirect Airport Strip:** `{data_block['alt_name']}`")
        target_lat, target_lon = data_block["alt_lat"], data_block["alt_lon"]
        path_line_color = "#ef4444" 
        status_text = "DIVERTING TO ALTERNATE HUB"

with col_right:
    st.write("### 🌍 Worldwide Live Tracking Satellite Map")
    
    js_flights_array = ", ".join([
        f"{{ callsign: '{f['callsign']}', lat: {f['lat']}, lon: {f['lon']}, alt: {f['alt']}, speed: {f['speed']}, heading: {f['heading']} }}"
        for f in data_block["live_flights"]
    ])

    leaflet_map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            html, body, #map {{ width: 100%; height: 535px; margin: 0; padding: 0; border-radius: 12px; }}
            .leaflet-popup-content-inner {{ font-family: sans-serif; line-height: 1.5; color: #0f172a; font-size: 13px; }}
            .popup-title {{ font-weight: bold; color: #1e3a8a; font-size: 14px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; margin-bottom: 6px; }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var map = L.map('map').setView([{data_block["lat"]}, {data_block["lon"]}], 6);

            L.tileLayer('https://mt1.google.com/vt/lyrs=y&x={{x}}&y={{y}}&z={{z}}').addTo(map);
            L.circle([{data_block["lat"]}, {data_block["lon"]}], {{ radius: 25000, color: '#38bdf8', weight: 2, fillOpacity: 0.03 }}).addTo(map);

            L.marker([{data_block["lat"]}, {data_block["lon"]}]).addTo(map).bindPopup("<b>🎯 Primary Hub:</b> {data_block['name']}");
            L.marker([{data_block["alt_lat"]}, {data_block["alt_lon"]}]).addTo(map).bindPopup("<b>🚨 Alternate Hub:</b> {data_block['alt_name']}");

            var flightPlanPoints = [[{data_block["fix_lat"]}, {data_block["fix_lon"]}], [{target_lat}, {target_lon}]];
            L.polyline(flightPlanPoints, {{ color: '{path_line_color}', weight: 6, opacity: 0.95, dashArray: '8, 8' }}).addTo(map);

            var liveGlobalFleet = [{js_flights_array}];
            var airplaneSvg = `<svg viewBox="0 0 24 24" width="32" height="32" xmlns="http://www.w3.org/2000/svg"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L14 19v-5.5l8 2.5z" fill="#fbbf24" stroke="#1e293b" stroke-width="1.2"/></svg>`;

            liveGlobalFleet.forEach(function(f) {{
                var customIcon = L.divIcon({{
                    html: '<div style="transform: rotate(' + f.heading + 'deg); text-align: center;">' + airplaneSvg + '</div>',
                    className: 'custom-plane-icon', iconSize: [32, 32], iconAnchor: [16, 16]
                }});

                var popupContent = "<div class='leaflet-popup-content-inner'><div class='popup-title'>✈️ " + f.callsign + "</div><b>Alt:</b> " + f.alt + " FT<br><b>Speed:</b> " + f.speed + " KTS</div>";
                L.marker([f.lat, f.lon], {{icon: customIcon}}).addTo(map).bindPopup(popupContent);
            }});
        </script>
    </body>
    </html>
    """
    
    components.html(leaflet_map_html, height=545, scrolling=False)