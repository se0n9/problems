num_people = int(input())
demand_size = list(map(int, input().split()))
demand_size = [int(x) for x in input().split()]
#emand_size = [int(input()) for _ in range(6)]
t_set, p_set = map(int, input().split())
print(num_people)
print(demand_size)
print(t_set, p_set)