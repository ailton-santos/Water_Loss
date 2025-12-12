# Water Loss Reduction Simulation with Dashboard
By Ailton Dos Santos

## Overview
This project is a data visualization dashboard designed to simulate and analyze the impact of modernization technologies (such as IoT sensors) on water loss reduction in urban distribution networks. The application simulates weekly sensor data across four different city zones (North, South, East, West). It visualizes the "Pre-Modernization" vs. "Post-Modernization" phases, allowing stakeholders to view the projected efficiency gains over a 50-week period.

## Technologies Used
This project was built using **Python** with a focus on data analysis and interactive web visualization. The specific stack includes:

* **Dash:** Used for the web application framework (Backend + Frontend interface).
* **Plotly:** Used for generating interactive, dynamic graphs.
* **Pandas & NumPy:** Used for data manipulation and simulation algorithms.

*Note: Dash is built on top of Flask, Plotly.js, and React.js, allowing for the creation of complex frontend interfaces using pure Python.*

## Features
* **Multi-Zone Simulation:** Generates distinct data patterns for East, West, North, and South zones.
* **Dynamic Visualization:** Interactive line charts showing water loss percentages over time.
* **Impact Analysis:** Visual indicators (markers and reference lines) identifying exactly when modernization efforts were implemented.
* **Comparative View:** A summary view that overlays data from all zones to compare performance.

## Project Structure
* `main.py`: The entry point script that initializes and launches the server.
* `dashboard.py`: Contains the Dash app layout, callback logic, and UI definitions.
* `data_generator.py`: Logic for simulating sensor data and applying reduction factors.
* `[zone]_zone/`: (Implied) Modules containing specific configurations for each geographic zone.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/water-loss-dashboard.git](https://github.com/ailton-santos/Water_Loss.git)
    cd Water_Loss
    ```

2.  **Install dependencies:**
    Ensure you have Python installed, then install the required libraries:
    ```bash
    pip install dash pandas plotly numpy
    ```

3.  **Run the application:**
    Execute the main script to start the server:
    ```bash
    python main.py
    ```

4.  **Access the Dashboard:**
    Open your web browser and navigate to:
    `http://127.0.0.1:8050/`

## Future Improvements
* Integration with real-time sensor APIs.
* Advanced predictive modeling using Machine Learning.
* Export functionality for simulation reports.
