def parser(file_input):
	try:
		file_input = file_input.decode('utf-8')
	except UnicodeDecodeError:
		file_input = file_input.decode('gbk')

	lines = []
	for line in file_input.split('\r'):
		if line.strip():
			lines.append(line.strip()+'\n')

	return lines

def append_item_to_file(item, file_name):
	if item[-1] != '\n':
		item = item+'\n'

	with open(file_name, 'a') as f:
		f.write(item)

def delete_item_from_file(item, file_name):
	with open(file_name, 'a+b') as f:
		f.seek(0)
		lines = parser(f.read())

	with open(file_name, 'w') as f:
		for line in lines:
			if item.strip() != line.strip():
				f.write(line)
