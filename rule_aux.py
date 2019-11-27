def get_preference_average(preferences):
	count = 0
	s = 0
	for key in preferences:
		count += 1
		s += preferences[key]

	return s / count
