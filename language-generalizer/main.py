import csv
from random import randint

class Main:

	def __init__(self):
		self.frequency = dict()
		self.adjacency = dict()


	def collect_data(self, locations: list) -> None:
		total = 0
		sum_all = 0

		for location in locations:
			print(f"New Location: {location}")
			total += 1
			sum_all += len(location)
			for index, character in enumerate(location):
				print(f"{index}, {character}")

				if character in self.frequency:
					self.frequency[character] += 1
				else:
					self.frequency[character] = 1

				if index > 0:
					pair = f'{location[index-1]}{character}'
					if pair in self.adjacency:
						self.adjacency[pair] += 1
					else:
						self.adjacency[pair] = 1
		mean_length = sum_all / total
		test_out = ''
		while len(test_out) < mean_length:
			test_out += self.choose_pair()
		print(f"Frequency: {self.frequency}\nAdjacency: {self.adjacency}\nTest Out: {test_out}")

	def choose_pair(self) -> str:
		chance_total = 0
		for pair in self.adjacency:
			chance_total += self.adjacency[pair]
		print(f"Chance Total: {chance_total}")
		while True:
			for pair in self.adjacency:
				if randint(0, chance_total) < self.adjacency[pair]:
					return pair


	def process_data(self) -> None:
		pass


	def generate_data(self) -> list:
		pass


process = Main()
data = list()
with open('uk-towns-sample.csv', encoding='utf-8') as file:
	reader = csv.reader(file)
	for row in reader:
		data.append(row[1].lower())

process.collect_data(data)