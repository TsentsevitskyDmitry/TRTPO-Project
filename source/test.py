from dparser import Parser
from datetime import datetime
from TextNotofocationProcessor import NotificationsORM

TEST = "напомни завтра в 8 уьиться";

notifications = NotificationsORM()

def prepare_values():
	return {'tstart':0, 'tend': 0}

def main():
	current_context = prepare_values();

	parser = Parser()
	parser.parse_time(TEST, current_context)
	parser.parse_text_payload(TEST, current_context)

	if('error' in current_context):
		print (current_context['error'])

	# notifications.add(current_context, 430722754)
	# notification = create_notification(current_context)
	# print(notification['preview'])
	# print(current_context)

	remindings = notifications.get_all(datetime.now())
	for remind in remindings:
		print("%i what %s"%(remind.chat_id, remind.payload))

	print(notifications.show_all(430722754))

if __name__ == '__main__':
    main()