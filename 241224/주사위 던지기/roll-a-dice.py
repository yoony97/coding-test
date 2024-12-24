n, m, r, c  = map(int, input().split())
ops = input().split()

def roll_dice(n, m, r, c, ops):
    # Directions mapping: 'L', 'R', 'U', 'D' -> dx, dy
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    
    # Dice state [top, bottom, right, left, front, back]
    dice = [1, 6, 3, 4, 2, 5]
    
    # Initialize grid
    grid = [[0] * n for _ in range(n)]
    
    # Place initial position of dice on grid
    r -= 1  # Convert to 0-indexed
    c -= 1  # Convert to 0-indexed
    grid[r][c] = dice[1]  # Bottom of the dice

    # Define dice rolling functions
    def roll_left(dice):
        return [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]

    def roll_right(dice):
        return [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]

    def roll_up(dice):
        return [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]

    def roll_down(dice):
        return [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]

    # Process operations
    for op in ops:
        dx, dy = directions[op]
        nr, nc = r + dx, c + dy
        
        # If the move is within bounds
        if 0 <= nr < n and 0 <= nc < n:
            r, c = nr, nc
            if op == 'L':
                dice = roll_left(dice)
            elif op == 'R':
                dice = roll_right(dice)
            elif op == 'U':
                dice = roll_up(dice)
            elif op == 'D':
                dice = roll_down(dice)
            
            # Update the grid with the new bottom value
            grid[r][c] = dice[1]
    # Calculate the total sum of the grid
    return sum(sum(row) for row in grid)

answer = roll_dice(n, m, r, c, ops)
print(answer)