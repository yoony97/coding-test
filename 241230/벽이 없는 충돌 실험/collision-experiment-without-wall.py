from collections import defaultdict

def simulate_collisions(T, test_cases):
    results = []

    # 방향 정의
    directions = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for t in range(T):
        N, marbles = test_cases[t]
        positions = defaultdict(list)
        for idx, (x, y, w, d) in enumerate(marbles):
            positions[(x, y)].append((idx + 1, w, d))

        time = 0
        last_collision_time = -1
        
        while True:
            new_positions = defaultdict(list)
            collisions = []

            # Move marbles
            for (x, y), marbles_at_pos in positions.items():
                for num, w, d in marbles_at_pos:
                    dx, dy = directions[d]
                    new_x, new_y = x + dx, y + dy
                    new_positions[(new_x, new_y)].append((num, w, d))

            # Check for collisions
            for (x, y), marbles_at_pos in new_positions.items():
                if len(marbles_at_pos) > 1:
                    collisions.append((x, y, marbles_at_pos))

            # Resolve collisions
            for x, y, marbles_at_pos in collisions:
                marbles_at_pos.sort(key=lambda x: (-x[1], -x[0]))  # Sort by weight, then by number
                survivor = marbles_at_pos[0]
                new_positions[(x, y)] = [survivor]
                last_collision_time = time + 1

            # Remove empty positions
            positions = {pos: marbles for pos, marbles in new_positions.items() if len(marbles) == 1}

            if not collisions:
                break

            time += 1

        results.append(last_collision_time)

    return results

# 입력 처리
def main():
    T = int(input())
    test_cases = []

    for _ in range(T):
        N = int(input())
        marbles = []
        for _ in range(N):
            x, y, w, d = input().split()
            x, y, w = int(x), int(y), int(w)
            marbles.append((x, y, w, d))
        test_cases.append((N, marbles))

    results = simulate_collisions(T, test_cases)
    for res in results:
        print(res+1)

main()
