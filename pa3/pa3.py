#Rui Wang
#bxe5fd
#PA3: Office Hours Redux

def find_overlap(shifts):
    if not shifts:
        return []

    shifts.sort() #sort shifts based on start time

    final_start, final_end = shifts[0] # set the start and end times to those of the first ta in sorted shift

    overlap = []

    for start_time, end_time in shifts[1:]:
        if start_time <= final_end: # yes there is an overlap
            final_end = max(final_end, end_time)
        else: # no overlap
            overlap.append(f"{final_start}-{final_end}")
            final_start, final_end = start_time, end_time # do comparison again to find the next set of overlap\

    overlap.append(f"{final_start}-{final_end}")
    return overlap

# read from stdin
test_cases = int(input())
for _ in range(test_cases):
    #print(f"\nReading test case {_+1}/{test_cases}")
    number_of_shifts = int(input())
    shifts = []

    for _ in range(number_of_shifts):
        start, end = map(int, input().split())
        shifts.append([start, end])

    # call your function here
    result = find_overlap(shifts)
    #for start, end in result:
    #print(str(start) + "-" + str(end))
    print(", ".join(result))