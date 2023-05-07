# Color
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BLUE = '\033[34m'
RESET = '\033[0m'

# Set up the initial environment
NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)] # Down, Left, Up, Right
NUM_ROW = 4
NUM_COL = 3
utilityMatrix = [[0, 1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Arguments - Given in the problem
REWARD = -0.04 # constant reward for non-terminal states
DISCOUNT = 0.95
MAX_ERROR = 10**(-3)

# Visualization
def printEnvironment(utilityMatrix, policy=False):
    displayGrid = ""
    for r in range(NUM_ROW):
        displayGrid += "|"
        for c in range(NUM_COL):
            if c == 1 and r == 2:
                val = "WALL"
            elif r == 0 and c >= 1:
                val = "+1" if c == 1 else "-1"
            else:
                if policy:
                     val = ["↓", "←", "↑", "→"][utilityMatrix[r][c]]
                else:
                    val = str(utilityMatrix[r][c])
            if(policy):
                if val == "→":
                    displayGrid += BLUE + val[:5].ljust(5) + RESET + " |"
                elif val == "←":
                    displayGrid += YELLOW + val[:5].ljust(5) + RESET + " |"
                elif val == "↓" or val == "+1":
                    displayGrid += RED + val[:5].ljust(5) + RESET + " |"
                elif val == "↑" or val == "-1":
                    displayGrid += GREEN + val[:5].ljust(5) + RESET + " |"
                elif val == "WALL":
                    displayGrid += MAGENTA + val[:5].ljust(5) + RESET + " |"
                else:
                    displayGrid += val[:5].ljust(5) + " |"
            else:
                if(val == "WALL"):
                    displayGrid += MAGENTA + val[:5].ljust(5) + RESET + " |"
                elif(val == "+1"):
                    displayGrid += GREEN + val[:5].ljust(5) + RESET + " |"
                elif(val == "-1"):
                    displayGrid += RED + val[:5].ljust(5) + RESET + " |"
                else:
                    displayGrid += val[:5].ljust(5) + " |"
        displayGrid += "\n"
    print(displayGrid)

# Get the utility of the state reached by performing the given action from the given state
def getUtilityByAction(utilityMatrix, row, col, action):
    rowChange, colChange = ACTIONS[action]
    newRow, newCol = row+rowChange, col+colChange
    if newRow < 0 or newCol < 0 or newRow >= NUM_ROW or newCol >= NUM_COL or (newRow == 2 and newCol == 1): # Boundry-Wall collision condition
        return utilityMatrix[row][col]
    else:
        return utilityMatrix[newRow][newCol]

# Calculate the utility of a state given an action
def calculateStateActionUtility(U, row, col, action):
    stateUtility = REWARD
    stateUtility += 0.15 * DISCOUNT * getUtilityByAction(U, row, col, (action-1)%4) # then (action-1)%4 = Right, perpendicular action
    stateUtility += 0.7 * DISCOUNT * getUtilityByAction(U, row, col, action) #  if action = Down, intended action
    stateUtility += 0.15 * DISCOUNT * getUtilityByAction(U, row, col, (action+1)%4) # then (action-1)%4 = Left, perpendicular action
    return stateUtility

def valueIteration(utilityMatrix):
    print("During the value iteration:\n")
    while True:
        nextUtilityMatrix = [[0, 1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        error = 0
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if  (r == 0 and c >= 1) or (c == 1 and r == 2):
                    continue
                nextUtilityMatrix[r][c] = max([calculateStateActionUtility(utilityMatrix, r, c, action) for action in range(NUM_ACTIONS)]) # Bellman update
                error = max(error, abs(nextUtilityMatrix[r][c]-utilityMatrix[r][c]))
        utilityMatrix = nextUtilityMatrix
        printEnvironment(utilityMatrix)
        if error < MAX_ERROR * (1-DISCOUNT) / DISCOUNT:
            break
    return utilityMatrix

# Get the optimal policy from utility matrix
def getOptimalPolicy(utilityMatrix):
    policy = [[-1, -1, -1, -1] for _ in range(NUM_ROW)]
    for row in range(NUM_ROW):
        for col in range(NUM_COL):
            if (row == 0 and col >= 1) or (col == 1 and row == 2): # ignore the wall and the terminal state
                continue
            # Choose the action that maximizes the utility
            maxAction, maxUtility = None, -float("inf")
            for action in range(NUM_ACTIONS):
                utility = calculateStateActionUtility(utilityMatrix, row, col, action)
                if utility > maxUtility:
                    maxAction, maxUtility = action, utility
            policy[row][col] = maxAction
    return policy

if __name__ == "__main__":
    # Print the initial environment
    print("The initial U is:\n")
    printEnvironment(utilityMatrix)

    # Value iteration
    utilityMatrix = valueIteration(utilityMatrix)

    # Get the optimal policy from utility matrix and print it
    policy = getOptimalPolicy(utilityMatrix)
    print("The optimal policy is:\n")
    printEnvironment(policy, True)

# Reference - https://github.com/SparkShen02/MDP-with-Value-Iteration-and-Policy-Iteration