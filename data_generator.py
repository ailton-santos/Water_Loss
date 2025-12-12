import pandas as pd
import numpy as np
import random

def generate_sensor_data(weeks, initial_loss_percentage, reduction_factor=0.015):
    """
    Generates simulated water loss data over a number of weeks.
    
    Args:
        weeks (int): The number of weeks to simulate.
        initial_loss_percentage (float): Initial water loss percentage (e.g., 30.0).
        reduction_factor (float): Factor by which the loss reduces each week after modernization.
        
    Returns:
        pd.DataFrame: A DataFrame with 'week' and 'water_loss_percentage' columns.
    """
    data = []
    
    # Simulate initial period (before modernization)
    for week in range(1, weeks // 2 + 1):
        loss = initial_loss_percentage + np.random.uniform(-1, 1)
        data.append([week, max(0, loss)])
        
    # Simulate post-modernization period
    current_loss = initial_loss_percentage
    for week in range(weeks // 2 + 1, weeks + 1):
        # A gradual reduction, with some random fluctuation
        reduction = random.uniform(reduction_factor - 0.005, reduction_factor + 0.005)
        current_loss = current_loss * (1 - reduction)
        loss = current_loss + np.random.uniform(-0.5, 0.5)
        data.append([week, max(0, loss)])
        
    df = pd.DataFrame(data, columns=['week', 'water_loss_percentage'])
    return df
