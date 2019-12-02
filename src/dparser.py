
class Parser:

	def __init__(self):
		self.__relative_keys = ['через', 'спустя']
		self.__absolute_keys = ['завтра', 'сегодня']


	def parse_time(context):
		# check if context contains any elements of relative_keys
		if (any(elem in context for elem in self.__relative_keys)):
			parse_relative(context)
		elif (any(elem in context for elem in self.__absolute_keys)):
			parse_absolute(context)
		elif (contain_native(context)):
			parse_native(context)
		else:
			context['error'] = "From list rand answer like 'ok, but when??'"


	def parse_relative(context):
		context['error'] = "Not implemented"

	def parse_absolute(context):
		context['error'] = "Not implemented"

	def contain_native(context):
		return any(char.isdigit() for char in context)

	def parse_native(context):
		context['error'] = "Not implemented"