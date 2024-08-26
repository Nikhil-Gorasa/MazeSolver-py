#DFS CUSTOM MAP SOLVER
from pyamaze import maze, agent, COLOR, textLabel

def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)
        if currCell == m._goal:
            break
        poss = 0
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                if child in explored:
                    continue
                poss += 1
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell
        if poss > 1:
            m.markCells.append(currCell)
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return dSearch, dfsPath, fwdPath

def executemaze(ro, co, speed, start_pos, goal_pos, loop):
    print("Executing...")
    m = maze(ro, co)  # ROWS & COLUMNS OF THE MAZE
    m.CreateMaze(*goal_pos,loopPercent=loop)  # GOAL CELL
    l1=textLabel(m,'TOTAL CELLS ',m.rows*m.cols)
    dSearch, dfsPath, fwdPath = DFS(m, start_pos)  # START CELL
    a = agent(m, *start_pos, goal=goal_pos, footprints=True, shape='square', color=COLOR.yellow)
    b = agent(m, *goal_pos, goal=start_pos, footprints=True, filled=True)
    c = agent(m, *start_pos, footprints=True, color=COLOR.dark, filled=True, shape='arrow')
    m.tracePath({a: dSearch}, showMarked=True, delay=speed // 2)
    m.tracePath({b: dfsPath}, delay=speed)
    m.tracePath({c: fwdPath}, delay=speed)
    m.run()
    return

if __name__ == '__main__':
    print("Welcome to A-Maze !")
    opt = int(input("Enter your choice : \n1.Go with The Default Settings\n2.Custom Settings\n-> "))
    if opt == 1:
        ro = co = 10
        goal_pos = (2, 4)
        start_pos = (5, 1)
        executemaze(ro, co, 100, start_pos, goal_pos, 0)

    elif opt == 2:
        print("-------------INPUT MAZE DATA--------------")
        ro = int(input("Enter the Number of Rows : "))
        co = int(input("Enter the Number of Columns : "))
        goal_pos = tuple(map(int, input("Enter Goal Position (row, col) separated by space: ").split()))
        start_pos = tuple(map(int, input("Enter Start Position (row, col) separated by space: ").split()))
        sp = int(input("Enter Speed [1 being fastest] : "))
        loop= int(input("Enter 100 to Enable Loops : "))
        executemaze(ro, co, sp, start_pos, goal_pos, loop)

    else:
        print("Enter the Right Option : ")
