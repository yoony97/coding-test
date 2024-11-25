# Input: A and B rectangles
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

# Step 1: Calculate intersection coordinates
ix1 = max(ax1, bx1)
iy1 = max(ay1, by1)
ix2 = min(ax2, bx2)
iy2 = min(ay2, by2)

# Step 2: Check if there is an intersection
if ix1 < ix2 and iy1 < iy2:
    # Step 3: Remaining area after removing overlap
    # Remaining rectangles
    remaining_coords = [
        (ax1, ay1, ax2, iy1),  # Bottom part
        (ax1, iy2, ax2, ay2),  # Top part
        (ax1, iy1, ix1, iy2),  # Left part
        (ix2, iy1, ax2, iy2)   # Right part
    ]

    # Filter out invalid rectangles (zero or negative area)
    valid_coords = [
        (rx1, ry1, rx2, ry2)
        for rx1, ry1, rx2, ry2 in remaining_coords
        if rx1 < rx2 and ry1 < ry2
    ]

    # Step 4: Calculate the bounding rectangle of remaining parts
    min_x = min(rx1 for rx1, _, _, _ in valid_coords)
    min_y = min(ry1 for _, ry1, _, _ in valid_coords)
    max_x = max(rx2 for _, _, rx2, _ in valid_coords)
    max_y = max(ry2 for _, _, _, ry2 in valid_coords)

    # Step 5: Calculate the area of the bounding rectangle
    result = (max_x - min_x) * (max_y - min_y)
    print(result)
else:
    # No overlap, A is the remaining rectangle
    print((ax2 - ax1) * (ay2 - ay1))
