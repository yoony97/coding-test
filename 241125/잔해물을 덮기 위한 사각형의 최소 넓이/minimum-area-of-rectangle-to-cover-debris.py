# Input: Rectangle A and B coordinates
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

# Step 1: Calculate overlap region
cx1 = max(ax1, bx1)
cy1 = max(ay1, by1)
cx2 = min(ax2, bx2)
cy2 = min(ay2, by2)

# Check if overlap exists
if cx1 < cx2 and cy1 < cy2:
    # Step 2: Calculate remaining regions
    regions = []
    
    # Top region
    if cy2 < ay2:
        regions.append((ax1, cy2, ax2, ay2))
    # Bottom region
    if cy1 > ay1:
        regions.append((ax1, ay1, ax2, cy1))
    # Left region
    if cx1 > ax1:
        regions.append((ax1, ay1, cx1, ay2))
    # Right region
    if cx2 < ax2:
        regions.append((cx2, ay1, ax2, ay2))

    # Step 3: Calculate the smallest enclosing rectangle
    min_area = float('inf')
    for rx1, ry1, rx2, ry2 in regions:
        area = (rx2 - rx1) * (ry2 - ry1)
        min_area = min(min_area, area)

    print(min_area)
else:
    # No overlap: Entire area of A
    print((ax2 - ax1) * (ay2 - ay1))
