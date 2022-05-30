import random
sum_so_far=0
num_throws=0
def throw():
    return random.randint(1, 6)

all_sum_so_far = []
all_num_throws = []

for experiment in range(1000):
    sum_so_far = sum_so_far+throw()
    #print(sum_so_far)
    num_throws = num_throws+1

    while sum_so_far>=100:
        all_sum_so_far.append(sum_so_far)
        all_num_throws.append(num_throws)
        sum_so_far=0
        num_throws=0
#print(all_sum_so_far)
#print(all_num_throws)
print( sum(all_num_throws)/1000 )