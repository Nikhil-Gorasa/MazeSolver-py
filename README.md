++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                A-Maze: DFS Custom Map Solver 🎮                
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Welcome to **A-Maze**, a Python project that solves mazes using the **Depth-First Search (DFS)** algorithm! 🧠
This program visualizes the maze-solving process using agents, and it allows you to customize the maze's start 
and goal positions, speed, and more.

──────────────────────────────────────────────────────────────
                      📂 Directory Structure
──────────────────────────────────────────────────────────────
nikhil-gorasa-mazesolver-py/
    └── MazeSolver.py

──────────────────────────────────────────────────────────────
                          📝 Files Content
──────────────────────────────────────────────────────────────
### `MazeSolver.py` 🔧
This Python script is the heart of the maze solver, featuring:
- **DFS Algorithm**: Explores and solves the maze from start to goal.
- **Maze Creation**: Customize maze settings (rows, columns, start/goal positions).
- **Visualization**: Use agents to trace the paths visually. 🟨

──────────────────────────────────────────────────────────────
                           🛠️ How It Works
──────────────────────────────────────────────────────────────

1. **DFS Algorithm** 🧑‍💻
   The `DFS` function traverses the maze from the start position to the goal, 
   marking cells and creating paths. Once the goal is reached, it traces back the solution path.

2. **Maze Creation** 🏰
   The `executemaze` function allows you to create a maze with your preferred settings:
   - Rows and Columns 🎲
   - Start and Goal Positions 🚶‍♂️➡️🏁
   - Speed (from 1 being fastest) ⏱️
   - Enable Loops (Set to 100 to enable) 🔄

3. **Maze Visualization** 🌟
   The maze is visualized using the `pyamaze` library, where:
   - **Agent 1** traces the DFS search path.
   - **Agent 2** traces the found path.
   - **Agent 3** traces the forward path from start to goal.

4. **User Input** 🖊️
   You can choose between:
   - **Option 1**: Run with default settings.
   - **Option 2**: Enter custom settings like maze size, start, goal, speed, and loops.

──────────────────────────────────────────────────────────────
                          🎮 Features
──────────────────────────────────────────────────────────────
- **DFS Algorithm**: Solves the maze using depth-first search.
- **Customizable Maze**: Set the number of rows, columns, and positions.
- **Path Tracing**: Visualize the maze-solving process with agents.
- **Speed Control**: Adjust the speed of the tracing.

──────────────────────────────────────────────────────────────
                           🚀 Usage
──────────────────────────────────────────────────────────────

1. **Run the Program** 💻: Execute the script in your terminal or IDE.
2. **Input Options** 🗨️:
   - **Option 1**: Use default settings.
   - **Option 2**: Customize the maze settings:
     - Number of Rows and Columns 🧩
     - Start and Goal Positions 🚀
     - Speed Control ⏩
     - Enable Loops (100 to enable) 🔄
3. **Maze Visualization**: The program generates and displays the maze, solving it step-by-step.

──────────────────────────────────────────────────────────────
                        📦 Installation
──────────────────────────────────────────────────────────────
To run this program, install the required library:

```bash
pip install pyamaze
