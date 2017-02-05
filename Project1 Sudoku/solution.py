assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    # Find all instances of naked twins
    for unit in units():
        twins = [(b1, b2, values[b1]) for b1 in sorted(unit) for b2 in sorted(unit)
                            if b2 > b1
                            and len(values[b1]) == 2
                            and values[b1] == values[b2]]
                            
        # Eliminate the naked twins as possibilities for the other boxes in the unit
        for b1, b2, v in twins:
            for box in unit:
                if box == b1 or box == b2:
                    continue
                assign_value(values, box, values[box].replace(v[0], ""))
                assign_value(values, box, values[box].replace(v[1], ""))
    return values

def cross(A, B):
    return [a+b for a in A for b in B]

def grid_values(grid):
    rows = 'ABCDEFGHI'
    cols = '123456789'
    boxes = cross(rows, cols)
    
    return {b: v if v != '.' else '123456789' for b, v in zip(boxes, grid)}

def display(values):
    if values == False:
        print("No solution exist")
        return
    
    rows = 'ABCDEFGHI'
    cols = '123456789'
    for i, r in enumerate(rows):
        if (i%3 == 0 and i != 0):
            print("+".join(['-'*(2*3)]*3))
        line = ""
        for j, c in enumerate(cols):
            if (j%3 == 0 and j != 0):
                line += "|"
            box = r+c
            line += "{} ".format(values[box])
        print(line)
    return
    
def peers(box):
    rows = 'ABCDEFGHI'
    cols = '123456789'
    
    ret = []
    ret += cross(box[0], cols) # peers along the same row
    ret += cross(rows, box[1]) # peers along the same col
    
    rs = next(v for v in ["ABC", "DEF", "GHI"] if box[0] in v)
    cs = next(v for v in ["123", "456", "789"] if box[1] in v)
    ret += cross(rs, cs) # peers in the same 3x3
    
    # get peers in diagonal (if it is a box in the diagonal)
    diag1 = [r+c for r, c in zip(rows, cols)]
    diag2 = [r+c for r, c in zip(rows, cols[::-1])]
    if box in diag1:
        ret += diag1
    if box in diag2:
        ret += diag2
    
    ret = list(set(ret)) # remove duplicate
    ret.remove(box) # remove the box itself
    
    return sorted(ret)

def eliminate(values):
    solved_boxes = [box for box, v in values.items() if len(v) == 1]
    for box in solved_boxes:
        for peer in peers(box):
            # remove the value of each box from its peers
            assign_value(values, peer, values[peer].replace(values[box], ""))
            
            # if a new solved box is created, add it to the solved boxes list
            if len(values[peer]) == 1 and not (peer in solved_boxes):
                solved_boxes.append(peer)
    return values

    
def units():
    rows = 'ABCDEFGHI'
    cols = '123456789'
    
    ret = []
    ret += [cross(r, cols) for r in rows] # row units
    ret += [cross(rows, c) for c in cols] # column units
    ret += [cross(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]] # 3x3 units
    ret += [[r+c for r, c in zip(rows, cols)], [r+c for r, c in zip(rows, cols[::-1])]] # diagonals
    
    return ret
    
def only_choice(values):
    for unit in units():
        for v in "123456789":
            possible_boxes = [box for box in unit if v in values[box]]
            if len(possible_boxes) == 1:
                only_box = possible_boxes[0]
                assign_value(values, only_box, v)
    return values

def reduce_puzzle(values):
    done = False
    while not done:
        n_pre_solved = len([box for box in values if len(values[box]) == 1])
        
        # Apply constraints
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        
        n_solved = len([box for box in values if len(values[box]) == 1])
        
        done = n_pre_solved == n_solved
    return values

def search(values):
    # solve puzzle as much as possible
    values = reduce_puzzle(values)
    
    unsolved_boxes = [box for box in values if len(values[box]) != 1]
    impossible_boxes = [box for box in values if len(values[box]) == 0]
    
    # base cases:
    if len(impossible_boxes) > 0: # one box has no possible values based on the current setup
        return False
    if len(unsolved_boxes) == 0: # all boxes were solved
        return values
    
    # DFS algorithm:
    # 1. choose box with the fewest 
    min_len = min([len(values[box]) for box in unsolved_boxes])
    choosen_box = next(box for box in unsolved_boxes if len(values[box]) == min_len)
    
    # 2. loop over possible values for the choosen box and recursively check each possible solution
    for v in values[choosen_box]:
        temp_values = values.copy()
        assign_value(temp_values, choosen_box, v)
        ret = search(temp_values)
        if ret != False:
            return ret
    
    # 3. if no option worked for the choosen box, it means there is no solution for the board given
    return False

def solve(grid):
    values = grid_values(grid)
    return search(values)
    

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
