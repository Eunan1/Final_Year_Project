import json
import os

# Function to load configurations from the configs directory
def load_config():
    filename = 'configs/config.json'
    # This assumes 'filename' will be passed with respect to the 'fyp' package root.
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
    # The first os.path.dirname(__file__) navigates up to 'fyp/utils',
    # the second one navigates up to 'fyp', making 'config_path' relative to the project root.
    
    # Normalize the path to ensure it's correct for the current operating system
    normalized_path = os.path.normpath(config_path)
    
    # Load and return the configuration file
    with open(normalized_path, 'r') as file:
        return json.load(file)
