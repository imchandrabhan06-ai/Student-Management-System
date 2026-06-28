import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "student.json")

def load_data():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []
 
def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("Data Saved Successfully")