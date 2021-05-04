
import numpy as np
import copy
# THIS CODE IS OPTIMAL FOR LARGER CASES BUT LESS OPTIMAL FOR SMALLER CASES
initial = [1,3,0,4,2,5,6,7] # solution = 8 steps
desired = [3,1,4,2,0,6,5,7]

i2 = [3,4,0,1] # 3 steps
d2 = [1,3,4,0]

initial_edge = [0,3] # solution = 1 step
desired_edge = [3,0]

initial_e1 = [0] # solution = 0
desired_e1 = [0]

initial_e2 = [4] # solution = 0
desired_e2 = [4]

def compute_cost(curr, targ): # this returns current cost of a dictionary after a move
    # keys are car numbers, pair is current index and cost to be updated
    cost = 0
    for key, value in curr.items():
        if value[1] != 0: # if current cost is not zero
        # cost is abs value of the difference in current index and desired index
            num_out_of_place = abs(value[0] - targ[key])
            value[1] = num_out_of_place # update cost
            cost += num_out_of_place
        else:
            cost += 0
    return cost, curr

def swap(curr, swap_car): # takes in the current dict and the id of the car to swap
    zero_id = curr[0][0] # get the zeroes id
    swap_id = curr[swap_car][0]
    temp = swap_id
    curr[swap_car][0] = zero_id
    curr[0][0] = temp

def min_moves_to_desired(initial, desired):

    current_dict = {} # keys are the car numbers, values are a pair (current index, cost)
    target_dict = {}

    # initialize dicts
    for i in range(0, len(initial)):
        if initial[i] != 0:
            current_dict[initial[i]] = [i,np.Inf] # store indices
        else:
            current_dict[initial[i]] = [i,0] # store index for 0 space has no cost

        target_dict[desired[i]] = i # store indices

    cost, current_dict = compute_cost(current_dict,target_dict) # inital cost of the initial state
    min_dict = current_dict # current lowest cost is initial, current lowest cost dict is current_dict
    num_steps = 0
    state_cost = np.Inf
    c = []
    prev_swap_key = -1
    c.append(cost)
    state_dict = copy.deepcopy(min_dict) ## initalize as state
    while cost > 0: #stop when we find a zero cost solution or break when reached local min
         # local min for expansion is current cost of overall loop
        asdfds = 1
        for key, value in state_dict.items():
            temp = copy.deepcopy(state_dict)
            if key != 0 and value[1] != 0 and key != prev_swap_key: # can't swap on the empty space or zero cost spaces
                swap(temp,key) # move the car to the empty space
                curr_cost, temp = compute_cost(temp,target_dict)
                if curr_cost == 0:
                    cost = 0
                    break
                if curr_cost < state_cost: # if we find a next state with less cost than current
                    cost = curr_cost
                    state_cost = curr_cost
                    min_dict = copy.deepcopy(temp)
                    prev_swap_key = key
        state_dict = copy.deepcopy(min_dict)
        state_cost = np.Inf
        num_steps += 1
        c.append(cost)
        if c[num_steps] <= c[num_steps - 1]: # if we have a result that increases the cost we dont want to repeat that move
            prev_swap_key = -1
    return num_steps

print(min_moves_to_desired(initial,desired))
print(min_moves_to_desired(initial_edge,desired_edge))
print(min_moves_to_desired(initial_e1,desired_e1))
print(min_moves_to_desired(initial_e2,desired_e2))
print(min_moves_to_desired(i2,d2))


