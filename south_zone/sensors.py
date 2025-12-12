import os
import subprocess

def run_dashboard():
    """
    Runs the Dash dashboard server.
    """
    print("Starting the Dash dashboard. This might take a few moments.")
    print("Open your browser and navigate to http://127.0.0.1:8050/")
    
    try:
        subprocess.run(["python", "dashboard.py"], check=True)
    except FileNotFoundError:
        print("Error: Could not find 'dashboard.py'. Make sure you are in the correct directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    run_dashboard()