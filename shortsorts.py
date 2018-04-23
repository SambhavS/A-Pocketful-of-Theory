#MergeSort (keeps duplicates)
def merge(l1,l2):
	final = []
	while l1 and l2:
		final.append(min([l1,l2], key = lambda x: x[0]).pop(0))
	return final + max([l1,l2], key = lambda x: len(x))
sorter = lambda lst: (lst if len(lst) < 2 else merge(sorter(lst[len(lst)//2:]), sorter(lst[:len(lst)//2])))
#QuickSort (removes duplicates)
quicky = lambda lst: (lst if len(lst) < 2 else quicky([x for x in lst if x<lst[0]]) + lst[:1] + quicky([x for x in lst if x > lst[0]]))
