from dparser import Parser

def prepare_values():
	return {'tstart':0, 'tent': 0}

def main():
	current_context = prepare_values();

	parser = Parser()
	parser.parse_time(current_context)
	# parse_payload(current_context)

	if('error' in current_context):
		print (current_context['error'])

	# notification = create_notification(current_context)
	# print(notification['preview'])
	print(current_context)


if __name__ == '__main__':
    process()