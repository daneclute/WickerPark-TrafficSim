Wicker Park Traffic Simulation
A discrete-event traffic simulation modeling real-world vehicle flow in Chicago’s
Wicker Park neighborhood using live traffic data from the City of Chicago Data
Portal.
Overview
This project simulates traffic patterns on Chicago streets using real-time traffic
speed data. Built with SimPy (discrete event simulation framework), it models
individual vehicle movement through street segments, calculating realistic travel
times based on current traffic conditions.
Features
• Real-world data integration: Fetches live traffic data from Chicago’s
open data API
• Discrete event simulation: Models individual car movements through
street network
• Dynamic traffic conditions: Calculates travel times based on actual
reported speeds
• Scalable architecture: Designed to expand from single segments to full
neighborhood networks
Tech Stack
• Python 3.12 - Core language
• SimPy 4.1 - Discrete event simulation framework
• Pandas - Data processing and analysis
• Requests - API integration
• Matplotlib - Data visualization (planned)
• NumPy/SciPy - Numerical analysis
Project Structure
WickerPark-TrafficSim/
   Simulation/
    main.py # Entry point and simulation runner
    simulation.py # Street and Car classes, core sim logic
    load_data.py # Chicago DOT API integration
    events.py # Event handlers (in development)
   chicago_traffic_data.csv # Sample/cached traffic data
   requirements.txt # Python dependencies
   README.md
1
Installation
1. Clone the repository:
git clone https://github.com/daneclute/WickerPark-TrafficSim.git
cd WickerPark-TrafficSim
2. Install dependencies:
pip install -r requirements.txt
3. Set up API credentials (optional - sample data included):
# Create .env file with Chicago Data Portal credentials
echo "API_KEY=your_key_here" > .env
echo "API_SECRET=your_secret_here" >> .env
Usage
Run the simulation:
cd Simulation
python main.py
Sample output:
Simulating: Eastbound
Length: 0.25 miles, Speed: 15 mph
Car 1 starting at Damen Ave going Eastbound at 15mph
Car 1 arrived at Wood St at time 1.23 minutes
How It Works
1. Data Collection: Fetches real-time traffic speed data from Chicago’s
open data portal
2. Environment Setup: Creates a SimPy discrete event simulation envi-
ronment
3. Street Modeling: Initializes street segments with real attributes (length,
speed, direction)
4. Vehicle Generation: Spawns cars with randomized arrival times
5. Traffic Simulation: Calculates travel times based on time = distance
/ speed
6. Event Processing: Tracks vehicle movement through the network
Current Scope
Currently simulates North Avenue (segment 208) with the following parameters:
- Segment: North Ave, Eastbound - From: Damen Avenue - To: Wood Street
- Length: ~0.25 miles - Traffic Speed: Live data (typically 10-20 mph during
congestion)
2
Roadmap
□ Expand to full Wicker Park neighborhood network (10+ segments)
□ Add traffic light modeling and intersection delays
□ Implement route optimization algorithms
□ Build visualization dashboard (real-time traffic flow charts)
□ Statistical analysis: congestion patterns, bottleneck identification
□ Compare simulated vs. actual travel times for validation
Applications
This simulation framework can be used for: - Urban traffic pattern analysis -
Road infrastructure planning - Transit optimization studies - Predictive model-
ing for congestion management - Emergency vehicle routing optimization
Data Source
Traffic data sourced from the Chicago Data Portal - Traffic Tracker dataset,
updated continuously by the Chicago Department of Transportation.
License
MIT License - feel free to use and modify for research or educational purposes.
Author
Dane Clute
CS Graduate, University of Illinois Chicago
Interested in simulation modeling, AI systems, and urban data analysis
