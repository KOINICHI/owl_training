import random
import time

Menu = []
for item in open('menu'):
	item = item.strip()
	idx = len(Menu) + 1
	Menu.append({'id': str(idx), 'name': item})

def test():
	results = {}
	for menu in random.sample(Menu, len(Menu)):
		name = menu['name']
		start_time = time.time()
		print (name + '?')
		ans = input()
		time_diff = time.time() - start_time
		results[name] = []
		if time_diff > 2:
			results[name].append('took too long')
		if ans != menu['id']:
			results[name].append('wrong answer')
	return list(filter(lambda x: len(results[x]) > 0, results))
		
		

while True:
	menu = random.choice(Menu)
	print (menu['name'] + '?')

	mode = False

	tries = 3
	while tries > 0:
		ans = input()
		if ans == '!t':
			results = test()
			for res in results:
				print ("{0} - {1}".format(res, ', '.join(results[res])))
			print ("{0}/{1} correct".format(len(Menu) - len(results), len(Menu)))
			if len(results) == 0:
				print ("You got everything!!")
			mode = True
			break
		if ans == menu['id']:
			print ("correct!")
			break
		tries -= 1

	if mode:
		continue

	if tries == 0:
		print ("wrong!: {0} - {1}".format(menu['id'], menu['name']))
		
