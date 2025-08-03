import os
import subprocess
import pandas as pd
import shutil

def setup_kaggle_api(api_path="kaggle.json"):
    """
    Moves kaggle.json to the location: ~/.kaggle/kaggle.json
    and sets the appropriate permissions.
    
    Parameters:
    - api_path: str, path to the kaggle.json file in the project root.
    """
    target_dir = os.path.expanduser("~/.kaggle")
    target_file = os.path.join(target_dir, "kaggle.json")

    if not os.path.exists(api_path):
        raise FileNotFoundError("kaggle.json not found in project root.")
    
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy(api_path, target_file)
    os.chmod(target_file, 0o600)
    print("kaggle.json moved to ~/.kaggle and permissions set.")

def download_kaggle_dataset(dataset, dest_dir="datasets"):
    """
    Downloads a Kaggle dataset using the Kaggle API.
    
    Parameters:
    - dataset: str, the Kaggle dataset identifier (e.g., 'zillow/zecon').   
    - dest_dir: str, directory where the dataset will be downloaded and unzipped.
    """
    os.makedirs(dest_dir, exist_ok=True)
    print("Downloading dataset...")
    subprocess.run([
        "kaggle", "datasets", "download", "-d", dataset, 
        "-p", dest_dir, "--unzip"
    ])

def load_events_csv(path):
    """
    Loads the main events CSV into a pandas DataFrame.
    Parameters:
    - path: str, path to the events CSV file.
    """
    df = pd.read_csv(path)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', errors='coerce')
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    return df