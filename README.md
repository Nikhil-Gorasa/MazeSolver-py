Here's the updated README with emojis:

```markdown
# 🧩 DFS Custom Map Solver

A maze-solving application that uses a Depth-First Search (DFS) algorithm to navigate through a maze and find the path from the start to the goal position. The program allows the user to either use default settings or provide custom maze data.

## 📂 Directory Structure

```
nikhil-gorasa-mazesolver-py/
    └── MazeSolver.py
```

## 📜 Files Content

### `MazeSolver.py`

This file contains the code that implements the maze solver using the DFS algorithm. It also creates the maze and visualizes the solution using agents in a graphical interface.

## 🔑 Key Functions

- `DFS(m, start=None)`: Implements the Depth-First Search algorithm to solve the maze.
- `executemaze(ro, co, speed, start_pos, goal_pos, loop)`: Executes the maze creation, solving, and visualization based on user input or default settings.

## 🔍 Key Variables

- `m`: The maze object.
- `start_pos`: The starting position of the agent.
- `goal_pos`: The goal position of the agent.
- `dSearch`: A list of the path taken during DFS.
- `dfsPath`: A dictionary containing the DFS path for backtracking.
- `fwdPath`: The final path from the start to the goal.

## ⚙️ Execution Flow

1. The program either starts with default settings or asks the user to input custom maze data, including rows, columns, start position, goal position, and speed.
2. The maze is created and solved using the DFS algorithm.
3. The program visualizes the path taken by agents and marks cells where multiple paths are possible.

## 📥 Installation

Clone this repository:

```bash
git clone https://github.com/nikhil-gorasa/mazesolver-py.git
```

Install the required Python libraries:

```bash
pip install pyamaze
```

## 🚀 Usage

Run the script:

```bash
python MazeSolver.py
```

Choose one of the following options:

- **Option 1**: Use default settings.
  - Rows and columns are set to 10.
  - Start position is (5, 1) and goal position is (2, 4).
  - Speed is set to 100.

- **Option 2**: Provide custom maze settings.
  - Enter the number of rows and columns.
  - Specify the start and goal positions.
  - Adjust the speed (1 is fastest).
  - Enable loops by entering 100.

## 🤝 Contributing

Feel free to fork this repository and contribute by opening issues or submitting pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- The maze-solving algorithm is based on Depth-First Search (DFS).
- The visualization of the maze is implemented using the pyamaze Python library.
```
