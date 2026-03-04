from collections import deque
import heapq


jug1 = 4
jug2 = 3
goal = 2

start = (0,0)

def get_next_states(state):
    x,y = state

    states = []

   
    states.append((jug1,y))

  
    states.append((x,jug2))

   
    states.append((0,y))

    
    states.append((x,0))

   
    transfer = min(x, jug2-y)
    states.append((x-transfer, y+transfer))

    
    transfer = min(y, jug1-x)
    states.append((x+transfer, y-transfer))

    return states


def goal_test(state):
    return state[0] == goal or state[1] == goal



def bfs():

    queue = deque([(start, [])])
    visited = set()

    while queue:

        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if goal_test(state):
            return path

        for next_state in get_next_states(state):
            queue.append((next_state, path))



def dfs():

    stack = [(start, [])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if goal_test(state):
            return path

        for next_state in get_next_states(state):
            stack.append((next_state, path))



def iterative_dfs():

    stack = [(start, [])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if goal_test(state):
            return path

        for next_state in reversed(get_next_states(state)):
            stack.append((next_state, path))



def dls(state, path, depth_limit):

    if goal_test(state):
        return path + [state]

    if depth_limit <= 0:
        return None

    for next_state in get_next_states(state):

        result = dls(next_state, path + [state], depth_limit-1)

        if result:
            return result

    return None



def ucs():

    pq = []
    heapq.heappush(pq,(0,start,[]))

    visited = set()

    while pq:

        cost, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if goal_test(state):
            return path

        for next_state in get_next_states(state):
            heapq.heappush(pq,(cost+1,next_state,path))




print("BFS Solution")
print(bfs())

print("\nDFS Solution")
print(dfs())

print("\nIterative DFS Solution")
print(iterative_dfs())

print("\nDepth Limited Search Solution")
print(dls(start, [], 10))

print("\nUniform Cost Search Solution")
print(ucs())
