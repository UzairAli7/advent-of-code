from collections import Counter
def power_comsumption(filename):
	with open(filename , 'r') as f:
		list1=f.read().strip().split('\n')
	gamma=''
	epsilon=''
	for i in range(len(list1[0])):
		common=(Counter([x[i] for x in list1]))
		if common['1'] > common['0']:
			gamma += '1'
			epsilon += '0'
		else:
			gamma += '0'
			epsilon += '1'

	x=int(gamma,2)
	y=int(epsilon, 2)

	power = x * y

	return power

a=power_comsumption('advent3.txt')
with open('advent3aans.txt', 'w') as f:
	f.write(str(a))



