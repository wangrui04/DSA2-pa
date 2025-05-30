# Rui Wang
# bxe5fd
# PA4: Exam Grading Optimisation

# T = number of teams
# Q = number of questions
def grading_optimisation(d, x): #d for duration to grade question and x for transfer time between teams
    T = len(d) # no of teams
    Q = len(d[0]) # no of qns

    # dp table
    f = [[0]*Q for _ in range(T)]

    #base case is grading qn 0
    for t in range(T):
        f[t][0] = d[t][0]

    #filling in of dp table
    for q in range(1, Q):
        for t in range(T):
            same_team = f[t][q-1] + d[t][q]
            transfer = min(f[tp][q-1] + x[tp][q-1] for tp in range(T) if tp != t) + d[t][q]
            f[t][q] = min(same_team, transfer)
    return min(f[t][Q-1] for t in range(T))

test_cases = int(input())
for case in range(test_cases):
    num_tas, num_qns = map(int, input().split())
    team_count = num_tas//num_qns

    #d array
    d_flat = list(map(int, input().split()))
    d = [d_flat[i * num_qns:(i + 1)*num_qns] for i in range(team_count)]

    #x array
    x_flat = list(map(int, input().split()))
    x = [x_flat[i * (num_qns-1):(i+1)*(num_qns-1)] for i in range(team_count)]

    result = grading_optimisation(d, x)
    print(result)