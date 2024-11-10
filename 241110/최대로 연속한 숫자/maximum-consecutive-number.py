def max_consecutive_length(n, m, removals):
    left = {i: i - 1 for i in range(n + 1)}
    right = {i: i + 1 for i in range(n + 1)}
    results = []
    
    # Initial maximum length is the whole sequence
    max_length = n + 1
    segment_lengths = {0: max_length}

    for removal in removals:
        l, r = left[removal], right[removal]
        left[r] = l
        right[l] = r

        # Update segment lengths
        current_length = r - l - 1
        if l in segment_lengths:
            del segment_lengths[l]
        if current_length > 0:
            segment_lengths[l] = current_length

        max_length = max(segment_lengths.values())
        results.append(max_length)

    return results

# Input reading and execution
if __name__ == "__main__":
    n, m = map(int, input().split())
    removals = list(map(int, input().split()))
    results = max_consecutive_length(n, m, removals)
    
    for result in results:
        print(result)