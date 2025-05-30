# PA2 Skeleton Code
# DSA2, spring 2025


# YOUR CODE HERE



# checks if the shifts can be assigned based on the number of TAs
# such that no TA works more than the max and all shifts are covered
def can_assign(shifts, numTAs, max_weight):
    current_weight = 0
    required_TAs = 1

    for weight in shifts:
        if current_weight + weight > max_weight:
            # assign shifts to a new TA
            required_TAs += 1
            current_weight = weight
            # if more TAs are needed
            if required_TAs > numTAs:
                return False
        else:
            current_weight += weight
            #print("current_weight:", current_weight)
    return True

# binary search to find the minimum possible maximum total weight that
# a TA needs to handle
def find_min_max_weight(shifts, numTAs):
    low = max(shifts) # heaviest singular shift
    #print("low: " + str(low))
    high = sum(shifts)
    #print("high: " + str(high))

    while low < high:
        mid = (low + high) // 2
        #print("mid: " + str(mid))
        if can_assign(shifts, numTAs, mid):
            high = mid # try for a smaller max weight
            #print("high: " + str(high))
        else:
            low = mid + 1 # increase max weight
            #print("low: " + str(low))
    return low


# This reads in the input from stdin -- you can always assume that the input is valid
test_cases = int(input())
for _ in range(test_cases):
    #print(f"\nReading test case {_+1}/{test_cases}")
    [s, t] = [int(x) for x in input().split(" ")]
    #print(str(s) + " shifts, " + str(t) + " TAs")
    arr = [int(x) for x in input().strip().split(" ") if x]
    #print(arr)
    #print("length of array: " + str(len(arr)))
    #print("Sum of array: " + str(sum(arr)))

    # call your function here
    result = find_min_max_weight(arr,t)
    print(result)
