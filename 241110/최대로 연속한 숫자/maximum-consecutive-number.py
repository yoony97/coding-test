from sortedcontainers import SortedSet

def max_consecutive_length(n, m, removals):
    nums = SortedSet(range(n + 1))
    results = []
    
    # Use a dictionary to keep track of the start and end of each sequence
    segments = {0: (0, n)}
    
    for removal in removals:
        # Find the segment that contains the removal
        for start, (seg_start, seg_end) in segments.items():
            if seg_start <= removal <= seg_end:
                # Remove the segment and split it
                del segments[start]
                if seg_start <= removal - 1:
                    segments[seg_start] = (seg_start, removal - 1)
                if removal + 1 <= seg_end:
                    segments[removal + 1] = (removal + 1, seg_end)
                break

        # Calculate the max segment length
        max_length = 0
        for seg_start, seg_end in segments.values():
            max_length = max(max_length, seg_end - seg_start + 1)
        results.append(max_length)

    return results

# Input reading and execution
if __name__ == "__main__":
    n, m = map(int, input().split())
    removals = list(map(int, input().split()))
    results = max_consecutive_length(n, m, removals)
    
    for result in results:
        print(result)