import json
import os

MEMORY_FILE = "jarvis_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
         return json.load(file)
    return {}

memory = load_memory()

def remember(key, value):
    memory[key] = value

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def recall(key):
    return memory.get(key)

def forget(key):
    if key in memory:
        del memory[key]
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=4)

            return True
        
        return False    

print("Memory is ready to use.")
