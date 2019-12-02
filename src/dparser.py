from datetime import datetime, time

class Parser:

	def __init__(self):
		self.__relative_keys = ['через', 'спустя']
		self.__absolute_keys = ['сегодня', 'завтра', 'послезавтра']
		self.__keyword = 'напомни'
		self.__err_usage = "Usage: Напомни *что* *когда*"
		self.__digits_worlds = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10}
		self.__dimention_worlds = {'час': 'hour', 'мин': 'min', 'ден': 'day', 'нед': 'week'}

	def parse_time(self, instring, context):
		if (self.__keyword in instring):
			# check if instring contains any elements of relative_keys
			if (any(elem in instring for elem in self.__relative_keys)):
				self.parse_relative(instring, context)
			elif (any(elem in instring for elem in self.__absolute_keys)):
				self.parse_absolute(instring, context)
			elif (self.contain_native(instring)):
				self.parse_native(instring, context)
			else:
				context['error'] = self.__err_usage
		else:
			context['error'] = self.__err_usage

	def parse_regular_digit(self, data, structure):
		try:
			structure['digit'] = int(data)
			return True
		except ValueError:
			if (data in self.__digits_worlds):
				structure['digit'] =  self.__digits_worlds[data]
				return True
			else:
				return False 

	def parse_dimention(self, data, structure):
		if (data[:3] in self.__dimention_worlds):
			structure['dimention'] = self.__dimention_worlds[data[:3]]

	def ismin(self, structure):
		if (structure['dimention'] == 'min'):
			return True;
		return False;

	def ishour(self, structure):
		if (structure['dimention'] == 'hour'):
			return True;
		return False;

	def isday(self, structure):
		if (structure['dimention'] == 'day'):
			return True;
		return False;	

	def isweek(self, structure):
		if (structure['dimention'] == 'week'):
			return True;
		return False;				

	def parse_relative(self, instring, context):
		# ex: напоини через [3] часа
		indata = instring.split(' ')
		structure = {'digit': 1, 'dimention': 'nope'}

		parse_index = indata.index(self.__keyword) + 2
		isdigit = self.parse_regular_digit(indata[parse_index], structure)
		if(isdigit):
			parse_index = parse_index + 1

		self.parse_dimention(indata[parse_index], structure)

		if ('nope' in structure.values()):
			context['error'] = "Не указано когда!"
		else:
			context['mins'] = self.ismin(structure) * structure['digit'];
			context['hours'] = self.ishour(structure) * structure['digit'];
			context['days'] = self.isday(structure) * structure['digit'];
			context['days'] = self.isweek(structure) * structure['digit'] * 7;
			context['tend'] = instring.find(indata[parse_index]) + len(indata[parse_index]) + 1


	def parse_day(self, data, structure):
		if (data in self.__absolute_keys):
			structure['tday'] = self.__absolute_keys.index(data)
			return True
		else:
			return False

	def parse_complex_time(self, data, structure):
		if (not self.contain_native(data) and data in self.__digits_worlds):
			data =  str(self.__digits_worlds[data])

		if (':' not in data):
			data = data + ':00'
		time = 	datetime.strptime(data, '%H:%M').time()
		structure['ttime'] = time



	def parse_absolute(self, instring, context):
		# ex: напонги завтра в 8
		indata = instring.split(' ')
		structure = {'tday': 0, 'ttime': time()}
		parse_index = indata.index(self.__keyword) + 1

		isday = self.parse_day(indata[parse_index], structure);
		if(isday and ((parse_index + 1) < len(indata)) and ('в' == indata[parse_index + 1])):
			parse_index = parse_index + 2
			self.parse_complex_time(indata[parse_index], structure)

		context['tend'] = instring.find(indata[parse_index]) + len(indata[parse_index]) + 1
		print(structure)
		context['time'] = datetime.now() + structure['ttime'] 

		if ('error' in structure):
			context['error'] = "Непонятное чет время"

	def contain_native(self, instring):
		return any(char.isdigit() for char in instring)

	def parse_native(self, instring, context):
		context['error'] = "Not implemented native"

	def parse_payload(self, instring, context):
		dstart = context['tend']	
		res = instring[dstart:]

		if (len(res) == 0 and 'payload' not in context or context['tend'] == 0):
			context['error'] = self.__err_usage
		else:
			context['payload'] = res;