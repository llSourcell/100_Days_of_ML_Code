import sys
from string import ascii_uppercase
pegs = ascii_uppercase[:NUM_PEGS]

NUM_PEGS = 3
NUM_DISCS = 4

def main():
    # Build graph
    G = build()

    #Validation
    checkDisksOrder("data-files/source.txt")
    checkDisksOrder("data-files/destination.txt")

    # Sample
    initial_state = readInitialState("data-files/source.txt")
    final_state = readFinalState()

    # Solution
    path = bfs(G, get_state_id(initial_state), get_state_id(final_state))[::-1]

    print "\nSolution:"
    for i in range(len(path)-1):
        print(move(get_state(path[i]), get_state(path[i+1])))

def openFile(filename):
    lines = open(filename, 'r')
    file.close
    return lines

def checkDisksOrder(filename):
    state_map = {}
    # Save state in map
    for line in openFile(filename):
        peg_pair = line.strip().split('-')
        peg_pair = line.strip().split('-')
        state_map[peg_pair[0]] = peg_pair[1].split(':')

    # Check for wrong cases in map
    for peg in state_map:
        array_size = len(state_map[peg])
        if(array_size) > 1:
            for disk, valor in enumerate(state_map[peg]):
                if(disk < array_size - 1):
                    next_disk = state_map[peg][(disk + 1)]
                if(next_disk > valor):
                    print("Disk '" + str(valor) + "' is on top of disk: '" + str(next_disk) + "'\n")
                    raise ValueError('Invalid State Map')
    return True

def readInitialState(filename):
    state_map = [None] * NUM_DISCS

    for line in openFile(filename):
        peg_pair = line.strip().split('-')
        # if there is a disk on peg
        if peg_pair[1] is not '':
            disks_in_peg = enumerate(peg_pair[1].split(':'))
            for disk, value in disks_in_peg :
                state_map[int(value)-1] = peg_pair[0]
    return state_map

def readFinalState():
    final_state_map = [None] * NUM_DISCS
    for peg in range(NUM_PEGS):
        final_state_configuration = raw_input("Estado final da haste " + str(pegs[peg]) + ':\n')
        peg_pair = final_state_configuration.strip().split('-')
        # if there is a disk on peg
        if peg_pair[1] is not '':
            disks_in_peg = enumerate(peg_pair[1].split(':'))
            for disk, value in disks_in_peg :
                final_state_map[int(value)-1] = peg_pair[0]
    return final_state_map

def get_state(state_id):
    state = []
    for i in range(NUM_DISCS):
        state += [pegs[state_id % NUM_PEGS]]
        state_id /= NUM_PEGS
    return state

def get_state_id(state):
    state_id = 0
    for disk in range(NUM_DISCS):
        state_id += NUM_PEGS**disk * pegs.index(state[disk])
    return state_id

def get_peg(state_id, disk):
    state = get_state(state_id)
    return pegs.index(state[disk])

def fits_on_top(state_id, disk, peg):
    state = get_state(state_id)
    for i in range(disk):
        if state[i] == pegs[peg]:
            return False
    return True

def get_valid_moves(state_id):
    valid_moves = []
    for disk in range(NUM_DISCS):
        disk_peg = get_peg(state_id,disk)
        if not fits_on_top(state_id, disk, disk_peg):
            continue
        for peg in range(NUM_PEGS):
            if peg == disk_peg:
                continue
            if not fits_on_top(state_id, disk, peg):
                continue
            state = get_state(state_id)
            state[disk] = pegs[peg]
            valid_moves += [get_state_id(state)]
    return valid_moves

def build():
    G = []
    for state_id in range(NUM_PEGS**NUM_DISCS):
        G += [ get_valid_moves(state_id) ]
    return G

def bfs(G, src, dst):
    visited = [False] * NUM_PEGS**NUM_DISCS
    queue = [ (0, src) ]
    last_of_layer = src

    i = 0
    while i < len(queue):
        pos, state_id = queue[i]
        if state_id == dst:
            break
        visited[state_id] = True
        for next_state in G[state_id]:
            if not visited[next_state]:
                queue += [ (i, next_state) ]
        if state_id == last_of_layer:
            pos, last_of_layer = queue[-1]
        i += 1

    path = []
    while i:
        i, state_id = queue[i]
        path += [state_id]

    path += [src]
    return path

def move(src, dst):
    for disk in range(NUM_DISCS):
        if src[disk] != dst[disk]:
            return '%d-%c' % (disk+1, dst[disk])

if __name__ == "__main__":
   main()
