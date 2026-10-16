# Set up the environment 
rooms = { 
"A": input("Enter the initial state of Room A (dirty/clean): ").lower(), 
"B": input("Enter the initial state of Room B (dirty/clean): ").lower() 
} 
 
# Validate room states 
for room in rooms: 
    while rooms[room] not in ["dirty", "clean"]: 
        rooms[room] = input( 
            f"Invalid input. Enter the state of Room {room} (dirty/clean):" 
        ).lower() 
 
 
# Function to check if a room is dirty 
def is_dirty(room): 
    return rooms[room] == "dirty" 
 
 
# Function to clean a room 
def clean_room(room): 
    rooms[room] = "clean" 
 
 
# Rule-based agent class 
class VacuumAgent: 
    def __init__(self): 
        self.location = "A" 
 
    # Move between Room A and Room B 
    def move(self): 
        if self.location == "A": 
            self.location = "B" 
        else: 
            self.location = "A" 
 
    # Perceive the room and perform an action 
    def perceive_and_act(self):  
        current_room = self.location 
 
        # Rule 1: If the room is dirty, clean it 
        if is_dirty(current_room): 
            clean_room(current_room) 
            action = f"Cleaned Room {current_room}" 
 
        # Rule 2: If the room is clean, move to the other room 
        else: 
            self.move() 
            action = f"Moved to Room {self.location}" 
 
        return action 
 
 
# Create  agent 
agent = VacuumAgent() 
 
# Ask the user how many steps to run 
steps = int(input("Enter the number of simulation steps: ")) 
 
print("\nInitial Environment:") 
print(rooms) 
print(f"Initial Agent Location: Room {agent.location}") 
 
# Run  simulation 
for step in range(1, steps + 1): 
    action = agent.perceive_and_act() 
 
    print(f"\nStep {step}") 
    print(f"Agent Location: Room {agent.location}") 
    print(f"Action Taken: {action}") 
    print(f"Environment: {rooms}") 
 
print("\nSimulation complete.")