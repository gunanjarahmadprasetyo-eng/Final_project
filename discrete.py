import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import folium
from streamlit_folium import st_folium
import random
from math import radians, sin, cos, sqrt, atan2
import pandas as pd
import requests

# =========================
# CONFIGURATION
# =========================
st.set_page_config(
    page_title="Discrete Mathematics Final Project",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS - PROFESSIONAL DESIGN
# =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Poppins:wght@300;400;500;600&display=swap');
    
    /* Main Background */
    .stApp {
        background-color: #FAF3E1;
        color: #222222;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Headers with Montserrat */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        color: #222222 !important;
    }
    
    .main-title {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800 !important;
        font-size: 3rem !important;
        color: #222222 !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
    }
    
    .section-title {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
        color: #222222 !important;
        border-bottom: 3px solid #FF6D1F;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem !important;
    }
    
    /* Sidebar Styling */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #F5E7C6 !important;
    }
    
    /* Professional Header */
    .main-header {
        background: linear-gradient(135deg, #FF6D1F, #FF8C42);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 25px rgba(255, 109, 31, 0.3);
    }
    
    /* Profile Cards */
    .profile-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 2px solid #F5E7C6;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }
    
    /* Role Badge */
    .role-badge {
        display: inline-block;
        background: #FF6D1F;
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 600;
        margin: 10px 0;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Contribution List */
    .contribution-list {
        text-align: left;
        margin: 20px 0;
        padding-left: 20px;
    }
    
    .contribution-list li {
        margin-bottom: 10px;
        line-height: 1.6;
    }
    
    /* Profile Photo */
    .profile-photo {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #FF6D1F;
        margin: 0 auto 20px;
        box-shadow: 0 8px 20px rgba(255, 109, 31, 0.3);
    }
    
    /* Graph Container */
    .graph-container {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        border: 1px solid #F5E7C6;
    }
    
    /* Map Container */
    .map-container {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        border: 1px solid #F5E7C6;
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #FF6D1F, #FF8C42);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 14px 28px;
        font-weight: 600;
        font-family: 'Montserrat', sans-serif;
        transition: all 0.3s ease;
        width: 100%;
        font-size: 1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 109, 31, 0.4);
        background: linear-gradient(135deg, #E55C1A, #FF6D1F);
    }
    
    /* Input Styling */
    .stSelectbox>div>div, .stTextInput>div>div>input, 
    .stNumberInput>div>div>input, .stMultiSelect>div>div {
        background: white;
        border: 2px solid #F5E7C6;
        color: #222222;
        border-radius: 8px;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Sidebar Navigation */
    .sidebar-nav {
        padding: 20px 0;
    }
    
    .nav-item {
        padding: 15px 20px;
        margin: 10px 0;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        border-left: 4px solid transparent;
        background: white;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    .nav-item:hover {
        background: #FF6D1F;
        color: white;
        border-left: 4px solid #222222;
        transform: translateX(5px);
    }
    
    .nav-item.active {
        background: #FF6D1F;
        color: white;
        border-left: 4px solid #222222;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        border-left: 5px solid #FF6D1F;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        border: 1px solid #F5E7C6;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    /* Route Option Cards */
    .route-option {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid #F5E7C6;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .route-option:hover {
        border-color: #FF6D1F;
        transform: translateY(-2px);
    }
    
    .route-option.selected {
        border-color: #FF6D1F;
        background: #FFF5EB;
    }
    
    .route-option.recommended {
        border-color: #FF6D1F;
        background: #FFF5EB;
        position: relative;
    }
    
    .route-option.recommended::before {
        content: "⭐ RECOMMENDED";
        position: absolute;
        top: -10px;
        right: 10px;
        background: #FF6D1F;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE INITIALIZATION
# =========================
if 'graph' not in st.session_state:
    st.session_state.graph = nx.Graph()
if 'node_positions' not in st.session_state:
    st.session_state.node_positions = {}
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Team Profiles"
if 'selected_route' not in st.session_state:
    st.session_state.selected_route = None
if 'available_routes' not in st.session_state:
    st.session_state.available_routes = None

# =========================
# GRAPH FUNCTIONS (From First Version)
# =========================
def create_random_graph(num_nodes, num_edges):
    """Create a random graph with specified nodes and edges"""
    G = nx.Graph()
    nodes = list(range(1, num_nodes + 1))
    G.add_nodes_from(nodes)
    
    all_possible_edges = [(i, j) for i in range(1, num_nodes + 1) for j in range(i + 1, num_nodes + 1)]
    
    if num_edges > len(all_possible_edges):
        num_edges = len(all_possible_edges)
    
    selected_edges = random.sample(all_possible_edges, num_edges)
    
    # Add weights to edges
    for edge in selected_edges:
        weight = random.randint(1, 20)
        G.add_edge(edge[0], edge[1], weight=weight)
    
    # Generate circular positions
    positions = {}
    center_x, center_y = 5, 5
    radius = 4
    
    for i, node in enumerate(nodes):
        angle = 2 * np.pi * i / len(nodes)
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        positions[node] = (x, y)
    
    return G, positions

def calculate_degree(G):
    """Calculate degree of each node"""
    return dict(G.degree())

def get_adjacency_matrix(G):
    """Get adjacency matrix as numpy array"""
    if len(G.nodes()) == 0:
        return np.array([])
    
    nodes = sorted(G.nodes())
    adj_matrix = np.zeros((len(nodes), len(nodes)))
    
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if G.has_edge(u, v):
                adj_matrix[i, j] = G[u][v].get('weight', 1)
    
    return adj_matrix

def visualize_graph(G, positions):
    """Visualize graph using matplotlib with high contrast colors"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    if len(G.nodes()) == 0:
        ax.text(0.5, 0.5, 'No graph to display', 
                horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=16, color='#222222', fontweight='bold')
        ax.set_facecolor('#FAF3E1')
        fig.patch.set_facecolor('#FAF3E1')
        return fig
    
    # High contrast colors
    node_colors = ['#FF6D1F' for _ in G.nodes()]
    edge_colors = ['#222222' for _ in G.edges()]
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(G, positions, ax=ax, 
                          node_color=node_colors, node_size=1000,
                          edgecolors='#222222', linewidths=2)
    
    nx.draw_networkx_edges(G, positions, ax=ax,
                          edge_color=edge_colors, width=2.5, alpha=0.8)
    
    # Draw labels
    nx.draw_networkx_labels(G, positions, ax=ax, 
                           font_size=14, font_weight='bold', font_color='white',
                           font_family='Montserrat')
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, 
                                   ax=ax, font_size=11, font_color='#222222',
                                   font_family='Montserrat')
    
    ax.set_facecolor('#FAF3E1')
    fig.patch.set_facecolor('#FAF3E1')
    ax.set_title("Graph Visualization", fontsize=20, pad=20, color='#222222', 
                fontweight='bold', fontfamily='Montserrat')
    ax.grid(True, alpha=0.3, color='#F5E7C6')
    ax.axis('on')
    
    return fig

# =========================
# JAVA ROUTE FINDER FUNCTIONS (From Second Version)
# =========================
# COMPREHENSIVE JAVA CITIES DATABASE
java_cities = {
    # Jakarta and Surroundings
    "Jakarta": [-6.2088, 106.8456],
    "Bogor": [-6.5971, 106.8060],
    "Depok": [-6.4025, 106.7942],
    "Tangerang": [-6.1783, 106.6319],
    "Bekasi": [-6.2383, 106.9756],
    
    # West Java
    "Bandung": [-6.9175, 107.6191],
    "Cimahi": [-6.8722, 107.5425],
    "Cirebon": [-6.7320, 108.5523],
    "Tasikmalaya": [-7.3274, 108.2207],
    "Sukabumi": [-6.9277, 106.9300],
    "Garut": [-7.2279, 107.9087],
    "Sumedang": [-6.8586, 107.9194],
    "Majalengka": [-6.8364, 108.2279],
    "Kuningan": [-6.9759, 108.4839],
    "Ciamis": [-7.3331, 108.3494],
    "Banjar": [-7.3708, 108.5346],
    "Purwakarta": [-6.5550, 107.4430],
    "Subang": [-6.5700, 107.7630],
    "Indramayu": [-6.3373, 108.3258],
    "Karawang": [-6.3227, 107.3376],
    
    # Central Java
    "Semarang": [-6.9667, 110.4167],
    "Surakarta (Solo)": [-7.5755, 110.8243],
    "Magelang": [-7.4706, 110.2177],
    "Salatiga": [-7.3307, 110.4922],
    "Pekalongan": [-6.8895, 109.6750],
    "Tegal": [-6.8694, 109.1400],
    "Cilacap": [-7.7255, 109.0244],
    "Purwokerto": [-7.4314, 109.2479],
    "Klaten": [-7.7050, 110.6060],
    "Demak": [-6.8903, 110.6392],
    "Kudus": [-6.8048, 110.8405],
    "Jepara": [-6.5944, 110.6711],
    "Pati": [-6.7550, 111.0380],
    "Blora": [-6.9698, 111.4185],
    "Rembang": [-6.8083, 111.6219],
    
    # Yogyakarta
    "Yogyakarta": [-7.7956, 110.3695],
    "Bantul": [-7.8833, 110.3333],
    "Sleman": [-7.7167, 110.3500],
    "Gunung Kidul": [-7.9833, 110.6167],
    "Kulon Progo": [-7.8667, 110.1500],
    
    # East Java
    "Surabaya": [-7.2575, 112.7521],
    "Malang": [-7.9666, 112.6326],
    "Kediri": [-7.8467, 112.0178],
    "Blitar": [-8.0986, 112.1683],
    "Madiun": [-7.6298, 111.5239],
    "Pasuruan": [-7.6453, 112.9075],
    "Probolinggo": [-7.7543, 113.2159],
    "Mojokerto": [-7.4664, 112.4338],
    "Jember": [-8.1845, 113.7032],
    "Banyuwangi": [-8.2191, 114.3691],
    "Lumajang": [-8.1335, 113.2242],
    "Bondowoso": [-7.9135, 113.8212],
    "Situbondo": [-7.7062, 114.0095],
    "Tulungagung": [-8.0643, 111.9023],
    "Trenggalek": [-8.0500, 111.7167],
    "Ponorogo": [-7.8667, 111.4667],
    "Pacitan": [-8.2067, 111.0933],
    "Ngawi": [-7.4044, 111.4464],
    "Magetan": [-7.6494, 111.3381],
    "Nganjuk": [-7.6050, 111.9036],
    "Bojonegoro": [-7.1500, 111.8833],
    "Tuban": [-6.8976, 112.0649],
    "Lamongan": [-7.1167, 112.4167],
    "Gresik": [-7.1556, 112.6542],
    "Sidoarjo": [-7.4481, 112.7183],
    "Jombang": [-7.5500, 112.2333]
}

# OSRM ROUTING FUNCTIONS
def get_osrm_route(start_coords, end_coords):
    """Get route from OSRM API with detailed geometry"""
    try:
        # OSRM expects format: lon,lat
        start_lon, start_lat = start_coords[1], start_coords[0]
        end_lon, end_lat = end_coords[1], end_coords[0]
        
        # Use public OSRM server
        url = f"http://router.project-osrm.org/route/v1/driving/{start_lon},{start_lat};{end_lon},{end_lat}?overview=full&geometries=geojson&alternatives=3"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['code'] == 'Ok':
            routes = []
            for i, route in enumerate(data['routes']):
                distance = route['distance'] / 1000  # Convert to km
                duration = route['duration'] / 60  # Convert to minutes
                
                # Extract geometry coordinates
                geometry = route['geometry']['coordinates']
                # Convert to [lat, lon] format for Folium
                coordinates = [[coord[1], coord[0]] for coord in geometry]
                
                # Extract steps for intermediate points
                steps = []
                if 'legs' in route:
                    for leg in route['legs']:
                        for step in leg['steps']:
                            if step['maneuver']['type'] == 'arrive':
                                continue
                            location = step['maneuver']['location']
                            steps.append([location[1], location[0]])  # Convert to [lat, lon]
                
                routes.append({
                    'distance': round(distance, 1),
                    'duration': round(duration, 1),
                    'coordinates': coordinates,
                    'steps': steps,
                    'name': f'Route {i+1}' if i > 0 else 'Recommended Route'
                })
            
            return routes
        else:
            return None
    except Exception as e:
        st.warning(f"OSRM API Error: {str(e)}. Using fallback routing.")
        return None

# FALLBACK ROUTING FUNCTIONS
def create_java_highway_graph():
    """Create a comprehensive highway graph for Java"""
    G = nx.Graph()
    
    # Add all cities as nodes
    for city, coord in java_cities.items():
        G.add_node(city, pos=coord)
    
    # Add major highway connections
    major_routes = [
        ("Jakarta", "Bandung", 150),
        ("Bandung", "Cirebon", 130),
        ("Cirebon", "Semarang", 200),
        ("Semarang", "Yogyakarta", 120),
        ("Yogyakarta", "Solo", 65),
        ("Solo", "Surabaya", 300),
        ("Bandung", "Tasikmalaya", 120),
        ("Tasikmalaya", "Ciamis", 30),
        ("Ciamis", "Banjar", 25),
        ("Semarang", "Pekalongan", 80),
        ("Pekalongan", "Tegal", 45),
        ("Tegal", "Cirebon", 150),
        ("Surabaya", "Malang", 90),
        ("Malang", "Blitar", 75),
        ("Blitar", "Kediri", 45),
        ("Kediri", "Jombang", 35),
        ("Jombang", "Mojokerto", 25),
        ("Mojokerto", "Surabaya", 50),
        ("Surabaya", "Sidoarjo", 25),
        ("Sidoarjo", "Pasuruan", 40),
        ("Pasuruan", "Probolinggo", 40),
        ("Probolinggo", "Jember", 85),
        ("Jember", "Banyuwangi", 95),
    ]
    
    for city1, city2, distance in major_routes:
        if city1 in java_cities and city2 in java_cities:
            G.add_edge(city1, city2, weight=distance)
    
    return G

def calculate_road_distance(coord1, coord2):
    """Calculate realistic road distance between two coordinates"""
    R = 6371
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    straight_distance = R * 2 * atan2(sqrt(a), sqrt(1-a))
    
    # Realistic road distance factor
    road_factor = 1.3 + (random.random() * 0.3)
    return straight_distance * road_factor

def find_fallback_routes(start_city, end_city, max_routes=3):
    """Find multiple possible routes using graph-based approach"""
    if start_city == end_city:
        return []
    
    G = create_java_highway_graph()
    
    try:
        routes = []
        
        # Shortest path
        shortest_path = nx.shortest_path(G, start_city, end_city, weight='weight')
        shortest_distance = calculate_path_distance(G, shortest_path)
        
        routes.append({
            'path': shortest_path,
            'distance': shortest_distance,
            'name': 'Shortest Route',
            'type': 'shortest'
        })
        
        # Alternative path 1 (avoiding some edges)
        try:
            G_temp = G.copy()
            # Remove one edge from shortest path to force alternative
            for i in range(min(2, len(shortest_path)-1)):
                if G_temp.has_edge(shortest_path[i], shortest_path[i+1]):
                    G_temp.remove_edge(shortest_path[i], shortest_path[i+1])
            
            alt_path = nx.shortest_path(G_temp, start_city, end_city, weight='weight')
            alt_distance = calculate_path_distance(G_temp, alt_path)
            
            if alt_path != shortest_path:
                routes.append({
                    'path': alt_path,
                    'distance': alt_distance,
                    'name': 'Alternative Route 1',
                    'type': 'alternative'
                })
        except:
            pass
        
        # Alternative path 2 (different weighting)
        try:
            G_alt = G.copy()
            # Adjust weights to prefer different routes
            for u, v, data in G_alt.edges(data=True):
                if random.random() > 0.5:
                    data['weight'] *= random.uniform(0.7, 1.3)
            
            alt_path2 = nx.shortest_path(G_alt, start_city, end_city, weight='weight')
            alt_distance2 = calculate_path_distance(G, alt_path2)
            
            if alt_path2 != shortest_path and not any(r['path'] == alt_path2 for r in routes):
                routes.append({
                    'path': alt_path2,
                    'distance': alt_distance2,
                    'name': 'Alternative Route 2',
                    'type': 'alternative'
                })
        except:
            pass
        
        return routes
        
    except nx.NetworkXNoPath:
        return []

def calculate_path_distance(G, path):
    """Calculate total distance for a path"""
    total_distance = 0
    for i in range(len(path) - 1):
        if G.has_edge(path[i], path[i+1]):
            total_distance += G[path[i]][path[i+1]]['weight']
    return round(total_distance, 1)

def find_closest_city(coords, exclude_cities=[]):
    """Find the closest city to given coordinates"""
    min_distance = float('inf')
    closest_city = None
    
    for city, city_coords in java_cities.items():
        if city in exclude_cities:
            continue
        
        distance = calculate_road_distance(coords, city_coords)
        if distance < min_distance:
            min_distance = distance
            closest_city = city
    
    return closest_city if min_distance < 50 else None  # Only if within 50km

def find_all_routes(start_city, end_city, use_osrm=True):
    """Find all available routes between cities"""
    routes = []
    
    if use_osrm:
        # Try OSRM first
        start_coords = java_cities[start_city]
        end_coords = java_cities[end_city]
        
        osrm_routes = get_osrm_route(start_coords, end_coords)
        
        if osrm_routes:
            for i, osrm_route in enumerate(osrm_routes):
                # Get intermediate cities from OSRM steps
                intermediate_cities = []
                if 'steps' in osrm_route and osrm_route['steps']:
                    # Find closest cities to OSRM steps
                    for step in osrm_route['steps']:
                        closest_city = find_closest_city(step, [start_city, end_city] + intermediate_cities)
                        if closest_city and closest_city not in [start_city, end_city]:
                            intermediate_cities.append(closest_city)
                
                route_path = [start_city] + intermediate_cities + [end_city]
                
                routes.append({
                    'path': route_path,
                    'distance': osrm_route['distance'],
                    'duration': osrm_route['duration'],
                    'coordinates': osrm_route['coordinates'],
                    'name': osrm_route['name'],
                    'type': 'osrm' if i == 0 else 'alternative',
                    'source': 'OSRM'
                })
    
    # Add fallback routes if OSRM failed or we need more options
    if len(routes) == 0 or not use_osrm:
        fallback_routes = find_fallback_routes(start_city, end_city)
        for fb_route in fallback_routes:
            # Generate coordinates for fallback routes
            coordinates = []
            for city in fb_route['path']:
                if city in java_cities:
                    coordinates.append(java_cities[city])
            
            routes.append({
                'path': fb_route['path'],
                'distance': fb_route['distance'],
                'duration': fb_route['distance'] / 60,  # Estimated duration (60 km/h average)
                'coordinates': coordinates,
                'name': fb_route['name'],
                'type': fb_route['type'],
                'source': 'Graph Algorithm'
            })
    
    # Sort routes by distance
    routes.sort(key=lambda x: x['distance'])
    
    # Mark the shortest as recommended
    if routes:
        routes[0]['name'] = '⭐ ' + routes[0]['name']
    
    return routes

# =========================
# SIDEBAR NAVIGATION
# =========================
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #222222; margin-bottom: 10px; font-family: "Montserrat", sans-serif; font-weight: 800;'>🌐 DISCRETE MATHEMATICS FINAL PROJECT</h1>
        <p style='color: #666; font-size: 14px; font-family: "Poppins", sans-serif;'>Advanced Graph Analysis Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation buttons
    nav_options = {
        "👥 TEAM PROFILES": "Team Profiles",
        "📊 GRAPH MATRIX APP": "Graph Matrix App", 
        "🗺️ JAVA ROUTE FINDER": "Java Route Finder"
    }
    
    for nav_text, page_id in nav_options.items():
        if st.button(nav_text, key=page_id, use_container_width=True):
            st.session_state.current_page = page_id
            st.rerun()
    
    st.markdown("---")
    
    # Quick stats in sidebar
    if len(st.session_state.graph.nodes()) > 0 and st.session_state.current_page == "Graph Matrix App":
        st.markdown("### 📈 CURRENT GRAPH")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Nodes", len(st.session_state.graph.nodes()))
        with col2:
            st.metric("Edges", len(st.session_state.graph.edges()))
    
    st.markdown("---")
    
    # Team information
    st.markdown("### 👥 DEVELOPMENT TEAM")
    st.markdown("""
    <div style='font-family: "Poppins", sans-serif;'>
    - Jasmiana C. A. (021202500026)
    - Angel Margaretha (021202500007)  
    - Gunanjar A. P. (021202500020)
    </div>
    """, unsafe_allow_html=True)

# =========================
# PAGE 1: TEAM MEMBER PROFILES
# =========================

st.markdown("""
<style>
/* CARD */
.profile-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    max-width: 320px;
    margin: auto;
}

/* CONTRIBUTIONS */
.contribution-list {
    margin-top: 14px;
}

.contribution-list ul {
    padding-left: 18px;
    margin: 0;
}

.contribution-list li {
    margin-bottom: 10px;
    line-height: 1.6;
    word-wrap: break-word;
    white-space: normal;
}
/* IMAGE */
img {
    display: block;
    margin: auto;
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.current_page == "Team Profiles":
    # Header Section
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">TEAM MEMBER PROFILES</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family: Montserrat, sans-serif; font-weight: 600; color: white; margin-bottom: 0;">Meet the talented team behind Graph Matrix Pro</h3>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Team Member 1: Jasmine
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("Jasmi.jpg", width=180)

        st.markdown("""
        <div class="profile-card">
            <h3 style='color: #FF6D1F; font-family: Montserrat, sans-serif;'>
                JASMIANA CELSMIN ARAUJO
            </h3>
            <p style='font-family: Poppins, sans-serif; font-weight: 600;'>
                NIM: 021202500026
            </p>
            <div class="role-badge">
                ⚙️ DevOps & Project Manager / Team Leader
            </div>
            <div class="contribution-list">
                <strong>Contributions:</strong>
                <ul>
                    <li>Led the team by coordinating tasks and managing timelines.</li>
                    <li>Oversaw the entire development workflow.</li>
                    <li>Handled deployment using GitHub and Streamlit Community Cloud.</li>
                    <li>Managed version control and repository structure.</li>
                    <li>Ensured final deployment met project requirements.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("Angel.jpg", width=180)

        st.markdown("""
        <div class="profile-card">
            <h3 style='color: #FF6D1F; font-family: Montserrat, sans-serif;'>
                ANGEL MARGARETHA
            </h3>
            <p style='font-family: Poppins, sans-serif; font-weight: 600;'>
                NIM: 021202500026
            </p>
            <div class="role-badge">
                🧪 Quality Assurance (QA) & Finalizer
            </div>
            <div class="contribution-list">
                <strong>Contributions:</strong>
                <ul>
                    <li>Conducted thorough testing of all features to detect bugs, UI inconsistencies, and functionality issues.</li>
                    <li>Reported issues to the developers and verified fixes to ensure the system operated smoothly.</li>
                    <li>Reviewed the entire web application for quality, completeness, and user experience before final submission.</li>
                    <li>Finalized all project components, including documentation, formatting, and the submission file.</li>
                    <li>Ensured that the deployed website and project report met academic standards and were error-free.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.image("gunanjar.jpg", width=180)

        st.markdown("""
        <div class="profile-card">
            <h3 style='color: #FF6D1F; font-family: Montserrat, sans-serif;'>
                GUNANJAR AHMAD PRASETYO
            </h3>
            <p style='font-family: Poppins, sans-serif; font-weight: 600;'>
                NIM: 021202500026
            </p>
            <div class="role-badge">
                💻 Back-End Developer & Full-Stack Developer
            </div>
            <div class="contribution-list">
                <strong>Contributions:</strong>
                <ul>
                    <li>Developed the server-side logic and built the core functionalities required for the web application.</li>
                    <li>Designed and managed the data flow between the front-end and back-end components.</li>
                    <li>Implemented APIs and ensured proper communication between the user interface and the database.</li>
                    <li>Provided full-stack support by assisting with front-end integration and troubleshooting issues during development.</li>
                    <li>Ensured the overall performance, stability, and functionality of the system.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("---")
    st.markdown('<h2 class="section-title">📋 PROJECT OVERVIEW</h2>', unsafe_allow_html=True)
    
    overview_col1, overview_col2 = st.columns(2)
    
    with overview_col1:
        st.markdown("""
        <div style='background: white; padding: 25px; border-radius: 15px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);'>
            <h3 style='color: #FF6D1F; font-family: Montserrat, sans-serif;'>🎯 Project Objectives</h3>
            <ul style='font-family: Poppins, sans-serif;'>
                <li>Develop a comprehensive graph theory visualization and analysis tool</li>
                <li>Create an interactive matrix application with adjacency matrix features</li>
                <li>Build a Java city routing system with Dijkstra's algorithm</li>
                <li>Deploy a fully functional web application using Streamlit</li>
                <li>Document the entire development process and results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with overview_col2:
        st.markdown("""
        <div style='background: white; padding: 25px; border-radius: 15px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);'>
            <h3 style='color: #FF6D1F; font-family: Montserrat, sans-serif;'>🛠️ Technologies Used</h3>
            <ul style='font-family: Poppins, sans-serif;'>
                <li><strong>Frontend:</strong> Streamlit, Folium, Matplotlib</li>
                <li><strong>Backend:</strong> Python, NetworkX, NumPy, Pandas</li>
                <li><strong>Algorithms:</strong> Dijkstra's Algorithm, Graph Theory</li>
                <li><strong>Deployment:</strong> GitHub, Streamlit Community Cloud</li>
                <li><strong>Design:</strong> Custom CSS, Google Fonts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# =========================
# PAGE 2: GRAPH MATRIX APP (Progress Report 1)
# =========================
elif st.session_state.current_page == "Graph Matrix App":
    st.markdown('<h1 class="section-title">📊 GRAPH MATRIX APPLICATION</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-family: Poppins, sans-serif; font-size: 18px; color: #444;">This application demonstrates graph theory concepts including graph visualization, node degree calculation, and adjacency matrix representation.</p>', unsafe_allow_html=True)
    
    # Feature Tabs
    tab1, tab2, tab3 = st.tabs(["🎲 GRAPH VISUALIZATION", "📈 NODE DEGREES", "🔢 ADJACENCY MATRIX"])
    
    with tab1:
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown('<div class="graph-container">', unsafe_allow_html=True)
            st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">⚙️ GRAPH CONFIGURATION</h3>', unsafe_allow_html=True)
            
            st.write("**Create a Random Graph**")
            num_nodes = st.slider("Number of Nodes", 2, 15, 6, key="viz_nodes")
            max_edges = num_nodes * (num_nodes - 1) // 2
            num_edges = st.slider("Number of Edges", 1, max_edges, min(8, max_edges), key="viz_edges")
            
            if st.button("🎲 GENERATE RANDOM GRAPH", key="generate_viz", use_container_width=True):
                G, positions = create_random_graph(num_nodes, num_edges)
                st.session_state.graph = G
                st.session_state.node_positions = positions
                st.success(f"✅ Generated graph with {num_nodes} nodes and {num_edges} edges!")
            
            st.markdown("---")
            
            # Graph Information
            if len(st.session_state.graph.nodes()) > 0:
                st.markdown('<h4 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📊 GRAPH INFORMATION</h4>', unsafe_allow_html=True)
                
                G = st.session_state.graph
                info_col1, info_col2 = st.columns(2)
                
                with info_col1:
                    st.metric("Nodes", len(G.nodes()))
                    st.metric("Density", f"{nx.density(G):.3f}")
                
                with info_col2:
                    st.metric("Edges", len(G.edges()))
                    connected = "Yes" if nx.is_connected(G) else "No"
                    st.metric("Connected", connected)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="graph-container">', unsafe_allow_html=True)
            st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">👁️ GRAPH VISUALIZATION</h3>', unsafe_allow_html=True)
            
            if len(st.session_state.graph.nodes()) > 0:
                fig = visualize_graph(st.session_state.graph, st.session_state.node_positions)
                st.pyplot(fig)
            else:
                st.info("👆 Please generate a random graph using the controls on the left to see the visualization here.")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        if len(st.session_state.graph.nodes()) == 0:
            st.warning("⚠️ Please generate a graph first in the Graph Visualization tab.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="graph-container">', unsafe_allow_html=True)
                st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📊 NODE DEGREES CALCULATION</h3>', unsafe_allow_html=True)
                
                degrees = calculate_degree(st.session_state.graph)
                
                # Create degree distribution visualization
                fig, ax = plt.subplots(figsize=(10, 6))
                
                nodes = list(degrees.keys())
                degree_values = list(degrees.values())
                
                colors = ['#FF6D1F' if d == max(degree_values) else 
                         '#222222' if d == min(degree_values) else 
                         '#F5E7C6' for d in degree_values]
                
                bars = ax.bar(nodes, degree_values, color=colors, edgecolor='#222222', linewidth=1.5)
                ax.set_facecolor('#FAF3E1')
                ax.set_xlabel('Nodes', color='#222222', fontsize=12, fontweight='bold', fontfamily='Montserrat')
                ax.set_ylabel('Degree', color='#222222', fontsize=12, fontweight='bold', fontfamily='Montserrat')
                ax.set_title('Node Degrees Distribution', color='#222222', fontsize=16, fontweight='bold', fontfamily='Montserrat')
                ax.tick_params(colors='#222222')
                ax.grid(True, alpha=0.3, color='#F5E7C6')
                
                # Add value labels on bars
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height)}', ha='center', va='bottom',
                            color='#222222', fontweight='bold', fontsize=10, fontfamily='Montserrat')
                
                fig.patch.set_facecolor('#FAF3E1')
                st.pyplot(fig)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="graph-container">', unsafe_allow_html=True)
                st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📈 DEGREE STATISTICS</h3>', unsafe_allow_html=True)
                
                # Display degree values
                st.write("**Degree of Each Node:**")
                for node, degree in degrees.items():
                    st.write(f"Node {node}: {degree} connection(s)")
                
                st.markdown("---")
                
                # Degree statistics
                stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
                
                with stats_col1:
                    st.metric("Maximum Degree", max(degrees.values()))
                with stats_col2:
                    st.metric("Minimum Degree", min(degrees.values()))
                with stats_col3:
                    st.metric("Average Degree", f"{sum(degrees.values()) / len(degrees):.2f}")
                with stats_col4:
                    st.metric("Total Degree", sum(degrees.values()))
                
                # Additional graph properties
                st.markdown("---")
                st.markdown('<h4 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📋 GRAPH PROPERTIES</h4>', unsafe_allow_html=True)
                
                G = st.session_state.graph
                prop_col1, prop_col2 = st.columns(2)
                
                with prop_col1:
                    st.write(f"**Is Connected:** {'Yes' if nx.is_connected(G) else 'No'}")
                    if nx.is_connected(G):
                        st.write(f"**Diameter:** {nx.diameter(G)}")
                    st.write(f"**Average Clustering:** {nx.average_clustering(G):.3f}")
                
                with prop_col2:
                    st.write(f"**Number of Components:** {nx.number_connected_components(G)}")
                    st.write(f"**Graph Density:** {nx.density(G):.3f}")
                    st.write(f"**Is Eulerian:** {'Yes' if nx.is_eulerian(G) else 'No'}")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        if len(st.session_state.graph.nodes()) == 0:
            st.warning("⚠️ Please generate a graph first in the Graph Visualization tab.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="graph-container">', unsafe_allow_html=True)
                st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">🔢 ADJACENCY MATRIX</h3>', unsafe_allow_html=True)
                
                adj_matrix = get_adjacency_matrix(st.session_state.graph)
                
                if adj_matrix.size > 0:
                    # Display matrix as styled table
                    nodes = sorted(st.session_state.graph.nodes())
                    adj_df = pd.DataFrame(adj_matrix, index=nodes, columns=nodes)
                    
                    st.dataframe(adj_df, use_container_width=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="graph-container">', unsafe_allow_html=True)
                st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📊 MATRIX PROPERTIES</h3>', unsafe_allow_html=True)
                
                if adj_matrix.size > 0:
                    # Matrix statistics
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Shape:** {adj_matrix.shape}")
                        st.write(f"**Total Elements:** {adj_matrix.size}")
                        st.write(f"**Non-zero Elements:** {np.count_nonzero(adj_matrix)}")
                    
                    with col2:
                        st.write(f"**Matrix Density:** {np.count_nonzero(adj_matrix) / adj_matrix.size:.3f}")
                        st.write(f"**Symmetric:** {np.array_equal(adj_matrix, adj_matrix.T)}")
                        st.write(f"**Trace:** {np.trace(adj_matrix)}")
                    
                    # Matrix heatmap
                    st.markdown("---")
                    st.markdown('<h4 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">🎨 MATRIX HEATMAP</h4>', unsafe_allow_html=True)
                    
                    fig, ax = plt.subplots(figsize=(8, 6))
                    
                    im = ax.imshow(adj_matrix, cmap='Oranges', interpolation='nearest')
                    
                    # Set ticks and labels
                    ax.set_xticks(range(len(nodes)))
                    ax.set_yticks(range(len(nodes)))
                    ax.set_xticklabels(nodes, color='#222222', fontweight='bold', fontfamily='Montserrat')
                    ax.set_yticklabels(nodes, color='#222222', fontweight='bold', fontfamily='Montserrat')
                    
                    ax.set_title('Adjacency Matrix Heatmap', color='#222222', fontsize=16, fontweight='bold', fontfamily='Montserrat', pad=20)
                    ax.set_facecolor('#FAF3E1')
                    fig.patch.set_facecolor('#FAF3E1')
                    
                    # Add colorbar
                    cbar = plt.colorbar(im, ax=ax)
                    cbar.ax.tick_params(colors='#222222')
                    cbar.set_label('Edge Weight', color='#222222', fontfamily='Montserrat')
                    
                    st.pyplot(fig)
                
                st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PAGE 3: JAVA ROUTE FINDER (From Second Version)
# =========================
elif st.session_state.current_page == "Java Route Finder":
    st.markdown('<h1 class="section-title">🗺️ JAVA ISLAND ROUTE PLANNER</h1>', unsafe_allow_html=True)
    
    # Main layout
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📍 SELECT YOUR ROUTE</h3>', unsafe_allow_html=True)
        
        # City selection
        city_list = sorted(java_cities.keys())
        
        start_city = st.selectbox(
            "🚗 Start City:",
            city_list,
            index=city_list.index("Jakarta") if "Jakarta" in city_list else 0
        )
        
        end_city = st.selectbox(
            "🎯 Destination City:",
            [city for city in city_list if city != start_city],
            index=city_list.index("Surabaya") if "Surabaya" in city_list and "Surabaya" != start_city else 0
        )
        
        # Routing options
        st.markdown("### 🔧 Routing Options")
        use_osrm = st.checkbox("Use OSRM for accurate routing (recommended)", value=True)
        show_alternatives = st.checkbox("Show alternative routes", value=True)
        
        if st.button("🔍 FIND ROUTES", use_container_width=True):
            with st.spinner("Finding optimal routes..."):
                routes = find_all_routes(start_city, end_city, use_osrm=use_osrm)
                
                if routes:
                    # Limit to 3 routes if not showing alternatives
                    if not show_alternatives:
                        routes = [routes[0]]
                    
                    st.session_state.available_routes = routes
                    st.session_state.selected_route = routes[0]  # Default to shortest route
                    st.success(f"✅ Found {len(routes)} route options!")
                else:
                    st.error("❌ No routes found between selected cities. Please try different cities.")
                    st.session_state.available_routes = None
                    st.session_state.selected_route = None
        
        # Display route options if available
        if 'available_routes' in st.session_state and st.session_state.available_routes:
            st.markdown("---")
            st.markdown('<h4 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">🛣️ AVAILABLE ROUTES</h4>', unsafe_allow_html=True)
            
            for i, route in enumerate(st.session_state.available_routes):
                is_selected = st.session_state.selected_route and st.session_state.selected_route['path'] == route['path']
                is_recommended = i == 0
                
                route_class = "route-option"
                if is_selected:
                    route_class += " selected"
                if is_recommended:
                    route_class += " recommended"
                
                st.markdown(f'<div class="{route_class}">', unsafe_allow_html=True)
                
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.write(f"**{route['name']}**")
                    st.write(f"📍 {' → '.join(route['path'])}")
                    if 'source' in route:
                        st.caption(f"Source: {route['source']}")
                with col_b:
                    st.write(f"**{route['distance']} km**")
                    if 'duration' in route:
                        hours = int(route['duration'] // 60)
                        minutes = int(route['duration'] % 60)
                        st.write(f"⏱️ {hours}h {minutes}m")
                
                if st.button(f"Select This Route", key=f"select_route_{i}", use_container_width=True):
                    st.session_state.selected_route = route
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Route details for selected route
        if st.session_state.selected_route:
            st.markdown("---")
            st.markdown('<h4 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">📋 ROUTE DETAILS</h4>', unsafe_allow_html=True)
            
            route = st.session_state.selected_route
            st.write(f"**Total Distance:** {route['distance']} km")
            
            if 'duration' in route:
                hours = int(route['duration'] // 60)
                minutes = int(route['duration'] % 60)
                st.write(f"**Estimated Duration:** {hours} hours {minutes} minutes")
            
            st.write(f"**Number of Stops:** {len(route['path'])}")
            st.write("**Route Breakdown:**")
            
            for i, city in enumerate(route['path']):
                col_a, col_b = st.columns([1, 4])
                with col_a:
                    if i == 0:
                        st.markdown("🚩")
                    elif i == len(route['path']) - 1:
                        st.markdown("🏁")
                    else:
                        st.markdown(f"**{i}.**")
                with col_b:
                    if i == 0:
                        st.markdown(f"**START:** {city}")
                    elif i == len(route['path']) - 1:
                        st.markdown(f"**DESTINATION:** {city}")
                    else:
                        st.markdown(f"**Stop {i}:** {city}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #FF6D1F; font-family: Montserrat, sans-serif;">🗺️ INTERACTIVE JAVA MAP</h3>', unsafe_allow_html=True)
        
        # Create base map centered on Java
        java_center = [-7.5, 110.0]
        m = folium.Map(
            location=java_center,
            zoom_start=7,
            tiles='OpenStreetMap'
        )
        
        # Add all city markers
        for city, coord in java_cities.items():
            # Determine marker color based on selection
            if st.session_state.selected_route and city in st.session_state.selected_route['path']:
                if city == st.session_state.selected_route['path'][0]:
                    icon_color = 'green'
                    icon_type = 'play'
                    popup_text = f"<b>START: {city}</b>"
                elif city == st.session_state.selected_route['path'][-1]:
                    icon_color = 'red'
                    icon_type = 'stop'
                    popup_text = f"<b>END: {city}</b>"
                else:
                    icon_color = 'blue'
                    icon_type = 'info-sign'
                    popup_text = f"<b>{city}</b> (Route Stop)"
            else:
                icon_color = 'gray'
                icon_type = 'info-sign'
                popup_text = f"<b>{city}</b>"
            
            folium.Marker(
                coord,
                popup=popup_text,
                tooltip=city,
                icon=folium.Icon(color=icon_color, icon=icon_type, prefix='fa')
            ).add_to(m)
        
        # Draw selected route if available
        if st.session_state.selected_route:
            route = st.session_state.selected_route
            
            # Use detailed coordinates if available (from OSRM)
            if 'coordinates' in route and route['coordinates']:
                route_coords = route['coordinates']
            else:
                # Fallback: use city coordinates
                route_coords = [java_cities[city] for city in route['path']]
            
            # Add the main route line
            folium.PolyLine(
                route_coords,
                color='#FF6D1F',
                weight=6,
                opacity=0.9,
                popup=f"<b>{route['name']}</b><br>Distance: {route['distance']} km<br>{' → '.join(route['path'])}",
                tooltip="Click for route details"
            ).add_to(m)
        
        # Display the map
        st_folium(m, width=700, height=600)
        
        # Map legend and info
        st.markdown("""
        <div style='background: #FAF3E1; padding: 15px; border-radius: 5px; margin-top: 10px;'>
        <strong>Map Legend:</strong><br>
        🟢 <span style='color: green;'>Start City</span> | 
        🔴 <span style='color: red;'>Destination</span> | 
        🔵 <span style='color: blue;'>Route Stops</span> | 
        ⚫ <span style='color: gray;'>Other Cities</span><br><br>
        <strong>Routing Info:</strong><br>
        • <span style='color: #FF6D1F;'>Orange Line</span> = Selected Route<br>
        • Click on markers for city info<br>
        • Click on route line for route details
        </div>
        """, unsafe_allow_html=True)
        
        # OSRM status
        if st.session_state.selected_route and 'source' in st.session_state.selected_route:
            source = st.session_state.selected_route['source']
            if source == 'OSRM':
                st.success("✅ Using OSRM for accurate road routing")
            else:
                st.info("ℹ️ Using graph algorithm for route calculation")
        
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #222222; padding: 30px; font-family: Poppins, sans-serif;'>"
    "🌐 <b>GRAPH MATRIX PRO</b> - FINAL PROJECT © 2024 | "
    "COMPREHENSIVE GRAPH ANALYSIS & JAVA ROUTE PLANNING | "
    "DEVELOPED WITH STREAMLIT & NETWORKX"
    "</div>",
    unsafe_allow_html=True
)