from TextNotofocationModel import TextNotification

class NotificationsORM:

	# def __init__(self):


	def add(self, context):
		TextNotification.create(payload=context['payload'], time=context['time'])