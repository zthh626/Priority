class Priority_Event_List():
	def __init__(self, calendar):
		temp = calendar.get_events()
		self.events = temp.get('items', [])

	def convert_to_priority_list(self):


	def get_summaries(self):
		x = []
		for event in events:
			x += event['summary']

		return x
