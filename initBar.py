import numpy as np

# Define constants
AMBIENT = 0
HOT = 1
COLD = -1

def initBar(m, n, hotSites, coldSites):
    # Initialize the ambient bar with AMBIENT values
    ambientBar = np.full((m, n), AMBIENT, dtype=int)
    return applyHotCold(ambientBar, hotSites, coldSites)

def applyHotCold(bar, hotSites, coldSites):
    newBar = bar
    for i in range(hotSites.shape[0]):
        for j in range(hotSites.shape[1]):
            if hotSites[i, j] == 1:  # Assign HOT only if the value is 1
                newBar[i, j] = HOT

    for i in range(coldSites.shape[0]):
        for j in range(coldSites.shape[1]):
            if coldSites[i, j] == 1:  # Assign COLD only if the value is 1
                newBar[i, j] = COLD

    return newBar

def convertToLabels(grid):
    # Convert numerical values to their string representations
    labelGrid = np.empty(grid.shape, dtype=object)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == HOT:
                labelGrid[i, j] = "HOT"
            elif grid[i, j] == COLD:
                labelGrid[i, j] = "COLD"
            else:
                labelGrid[i, j] = "AMBIENT"
    return labelGrid

if __name__ == "__main__":
    x = 2  # Number of rows
    y = 4  # Number of columns

    # Initialize hotSites
    hotSites = np.zeros((x, y), dtype=int)
    for i in range(x):
        for j in range(y):
            hotSites[i, j] = np.random.randint(0, 2)  # Randomly assign 0 or 1

    # Initialize coldSites
    coldSites = np.zeros((x, y), dtype=int)
    for i in range(x):
        for j in range(y):
            coldSites[i, j] = np.random.randint(0, 2)

    print("Hot Sites:")
    print(hotSites)
    print("Cold Sites:")
    print(coldSites)

    # Generate the ambient bar with hot and cold sites applied
    resultGrid = initBar(x, y, hotSites, coldSites)
    labeledGrid = convertToLabels(resultGrid)
    print("Resulting Grid:")
    print(labeledGrid)
