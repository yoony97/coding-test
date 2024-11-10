from sortedcontainers import SortedSet

def max_consecutive_length(n, m, removals):
    nums = SortedSet(range(n + 1))
    results = []

    for removal in removals:
        nums.remove(removal)

        max_length = 0
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        max_length = max(max_length, current_length)
        results.append(max_length)

    return results

# Input reading and execution
if __name__ == "__main__":
    n, m = map(int, input().split())
    removals = list(map(int, input().split()))
    results = max_consecutive_length(n, m, removals)
    
    for result in results:
        print(result)