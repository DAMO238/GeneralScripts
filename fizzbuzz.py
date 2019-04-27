i = 1

while True:
	three = False
	five = False
	
	if i%3 == 0:
		three = True
		
	if i%5 == 0:
		five = True
		
	if three and five:
		print('FizzBuzz')
	elif three:
		print('Fizz')
	elif five:
		print('Buzz')
	else:
		print(str(i))
		
	#temp = raw_input()
	i = i +1