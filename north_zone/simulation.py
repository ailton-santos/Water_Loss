import pandas as pd
import os
import sys

# Add parent directory to path to import data_generator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_generator import generate_sensor_data

def run_simulation(weeks):
    """
    Runs the water loss simulation for the  North Zone.
    """
    print("North Zone: Starting ...")
    # Simulating data with an initial higher loss percentage
    initial_loss = 35.0  
    simulated_data = generate_sensor_data(weeks, initial_loss)
    print("North Zone: Complete.")
    return simulated_data