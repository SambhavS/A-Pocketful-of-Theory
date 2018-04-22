#DP Solutions to the Unbounded & 1/0 Knapsack problems

#Unbounded Variation
def knap(max_cap, items):
	max_cap += 1
	dp = [0]*max_cap
	for k in range(1, max_cap):
		dp[k] = max([i[1] + dp[k - i[0]] for i in items if i[0]<=k])
	return dp[-1]

#1/0 Variation
def knapsack(max_cap, items):
	#Length of lists include +1 because table goes from 0 -> Capacity, 0->Items
	capacity_width = max_cap + 1
	item_width = len(items) + 1
	dp = [[0]*item_width for i in range(capacity_width)]
	for Nth in range(1,item_width):
		for capacity in range(1, capacity_width):
			item_weight, item_value = items[Nth - 1]
			if(item_weight > capacity):
				dp[capacity][Nth] = dp[capacity][Nth - 1]
			else:
				dp[capacity][Nth] = max(dp[capacity][Nth - 1], dp[capacity-item_weight][Nth - 1] + item_value)
	return dp[-1][-1]

#A few examples
items = [(1,1),(20,21),(50,54),(70,77),(2,2),(50,52)] #format: (weight, value)
print(knap(500, items))
print(knapsack(500, items))
print(knap(100, items))
print(knapsack(100, items))