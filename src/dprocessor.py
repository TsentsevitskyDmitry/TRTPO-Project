from dparser import Parser 

class DialogProcessor:
	def __init__(self):
		self.__open_dialogs = {};
		self.__database = NotiDatabase();

    def prepare_values():
    	return {'tstart':0, 'tent': 0}

	def process(self, content, chat_id):
		current_context = prepare_values();
		if(chat_id in self.__open_dialogs):
			current_context = self.__open_dialogs[chat_id];

		parser = Parser();
		parser.parse_time(current_context)
		parser.parse_payload(current_context)

		if('error' in current_context):
			return current_context['error']

		notification = create_notification(current_context)
		self.__database.add(notification)
		current_context.pop(chat_id, None)
		return notification['preview']



	# def process(self, content, chat_id):
	# 	time_context = contetn_context = False

	# 	if (chat_id in self.__open_dialogs):
	# 		context = self.__open_dialogs[chat_id]
	# 		if ('time' in context):
	# 			time_context = True;
	# 		elif ('content' in context):
	# 			contetn_context = True;

	# 	data = Parser.parse(content)
	# 	if (('content' in data and 'time' in data) or ('time' in data and contetn_context) or ('content' in data and time_context)):
	# 		self.__open_dialogs.clear();
	# 		print ("Adding new task: content %s, time %s" % (data['content'], data['time']))
	# 		return ("Task ok, content %s, time %s" % (data['content'], data['time']))

	# 	elif ('time' in data):
	# 		return "Select text from db: Ok, but what?"

	# 	elif ('content' in data):
	# 		return "Select text from db: Ok, but when?"

	# 	self.__open_dialogs[caht_id] = data;
