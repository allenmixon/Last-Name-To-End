import csv

print("This program moves the last name from the beggining of a cell the end of a cell.\nThis is for CSV files only.")
fn = input("What is the name of the file you would like to open: ")

#try:
with open(fn, 'r') as csv_file:

	csv_reader = csv.reader(csv_file)
	column_names = next(csv_reader)

	print(column_names, '\n')
	cname = input("What is the name of the column you want to apply this to: ")	
	loc = column_names.index(cname)

	while cname not in column_names:
		cname = input("Column name does not exist try again: ")

	for line in csv_reader:

		#Skip companies by checking for 'LLC'
		if 'LLC' in line[loc]:
			print(line[loc])
			continue

		names = line[loc].split(' ')
		suffix = ''
		

		#remove stray '&'
		if names[-1] == '&':
			names.pop()

		#handle suffix
		if ('JR' or 'JUNIOR') in names:
			suffix = (' ' + names.pop(names.index('JR'))) 
		elif 'SR' in names:
			suffix = (' ' + names.pop(names.index('SR')))
		elif 'II' in names:
			suffix = (' ' + names.pop(names.index('II')))
		elif 'III' in names:
			suffix = (' ' + names.pop(names.index('III')))

		#remove other info
		if 'ET' in names: names.remove('ET')
		if 'AL' in names: names.remove('AL')
		if 'UX' in names: names.remove('UX')
		if 'ETAL' in names: names.remove('ETAL')
		if 'ETUX' in names: names.remove('ETUX')	
		if 'R/S' in names: names.remove('R/S')
		if 'L/E' in names: names.remove('L/E')
		if '(LIFE EST)' in names: names.remove('(LIFE EST)')
		if '(L/E)' in names: names.remove('(L/E)')
		if '(LE)' in names: names.remove('(LE)')		

		last = names.pop(0)

		for i in names:
			print(i + ' ', end='')

		print(last + suffix)
	
	print( "\nThe preceding changes will be made to the column \'{}\' in {} continue [y/n]?".format(cname, csv_file.name))

	if input() == ('y'):
		with open(('new_' + fn), 'w') as new_file:
			csv_writer = csv.writer(new_file)

			print('Creating {} ...'.format(new_file.name))
			csv_writer.writerow(column_names)

			csv_file.seek(0)	
			next(csv_reader)

			for line in csv_reader:

				#Skip companies by checking for 'LLC'
				if 'LLC' in line[loc]:
					csv_writer.writerow(line)
					continue

				names = line[loc].split(' ')
				suffix = ''

				#remove stray '&
				if names[-1] == '&':
					names.pop()
				
				#handle suffix
				if ('JR' or 'JUNIOR') in names:
					suffix = (' ' + names.pop(names.index('JR'))) 
				elif 'SR' in names:
					suffix = (' ' + names.pop(names.index('SR')))
				elif 'II' in names:
					suffix = (' ' + names.pop(names.index('II')))
				elif 'III' in names:
					suffix = (' ' + names.pop(names.index('III')))

				#remove other info
				if 'ET' in names: names.remove('ET')
				if 'AL' in names: names.remove('AL')
				if 'UX' in names: names.remove('UX')
				if 'ETAL' in names: names.remove('ETAL')
				if 'ETUX' in names: names.remove('ETUX')	
				if 'R/S' in names: names.remove('R/S')
				if 'L/E' in names: names.remove('L/E')
				if '(LIFE EST)' in names: names.remove('(LIFE EST)')
				if '(L/E)' in names: names.remove('(L/E)')
				if '(LE)' in names: names.remove('(LE)')		

				last = names.pop(0)
				
				#set to empy string
				line[loc] = ""

				for i in names:
					line[loc] += (i + ' ')
	
				line[loc] += last
				line[loc] += (suffix)

				csv_writer.writerow(line)
# except:
# 	print("Error: program terminated")

