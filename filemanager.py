import json

def upcoming_writer(upcoming_dict):
    with open("upcoming.json", 'w') as f:
        f.write(json.dumps(upcoming_dict, indent=4))

def get_upcoming():
    with open("upcoming.json", 'r') as f:
        upcoming_dict = json.loads(f.read())
    return upcoming_dict

def sol_writer(sol_dict):
    with open("solsea.json", 'w') as f:
        f.write(json.dumps(sol_dict, indent=4))

def get_sol():
    with open("solsea.json", 'r') as f:
        sol_dict = json.loads(f.read())
    return sol_dict

def get_verified_sol():
    with open("verified_solsea.json", 'r') as f:
        sol_dict = json.loads(f.read())
    return sol_dict

def sol_verified_writer(sol_dict):
    with open("verified_solsea.json", 'w') as f:
        f.write(json.dumps(sol_dict, indent=4))