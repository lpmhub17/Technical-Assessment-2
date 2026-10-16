Rule-Based Vacuum Agent
This Python program demonstrates a simple rule-based intelligent agent. The agent acts as a vacuum cleaner that moves between two rooms, Room A and Room B.
The agent checks the condition of its current room and follows predefined rules:
- If the current room is dirty, the agent cleans it.
- If the current room is clean, the agent moves to the other room.
Requirements
- Python 3.x
No external Python libraries are required.
How to Run
1. Save the code in a Python file, such as:
vacuum_agent.py
2. Open the folder in VS Code.
3. Open the VS Code terminal.
4. Run the program:
py vacuum_agent.py
If the py command does not work, use:
python vacuum_agent.py
User Inputs
The program asks the user to provide:
1. The initial state of Room A: dirty or clean
2. The initial state of Room B: dirty or clean
3. The number of simulation steps
The program accepts uppercase or lowercase room states because the input is converted to lowercase.
Example Input
Enter the initial state of Room A (dirty/clean): dirty
Enter the initial state of Room B (dirty/clean): clean
Enter the number of simulation steps: 4
Example Output
Initial Environment:
{'A': 'dirty', 'B': 'clean'}
Initial Agent Location: Room A

Step 1
Agent Location: Room A
Action Taken: Cleaned Room A
Environment: {'A': 'clean', 'B': 'clean'}

Step 2
Agent Location: Room B
Action Taken: Moved to Room B
Environment: {'A': 'clean', 'B': 'clean'}

Simulation complete.
The exact output depends on the starting room conditions and the number of steps entered.
How the Agent Works
The agent starts in Room A. During every simulation step, it observes its current room and chooses an action based on the room's condition.
Rule 1: Clean a Dirty Room
If the current room is dirty, the agent changes the room's state to clean.
Rule 2: Move from a Clean Room
If the current room is clean, the agent moves to the other room.
Main Parts of the Program
- rooms stores the condition of Room A and Room B.
- is_dirty() checks whether a room is dirty.
- clean_room() changes a room's state to clean.
- VacuumAgent represents the intelligent agent.
- move() switches the agent between the two rooms.
- perceive_and_act() applies the agent's rules.
- The for loop runs the simulation for the number of steps entered by the user.
Purpose of the Simulation
This program demonstrates how a rule-based agent:
- Perceives its environment
- Uses predefined rules
- Performs an action
- Changes the state of its environment
It is a simple example of how intelligent systems can make decisions based on conditions.
Limitations
- The environment contains only two rooms.
- The agent can only clean rooms and move between rooms.
- The agent does not remember previous actions.
- The number of simulation steps must be entered as a whole number.
