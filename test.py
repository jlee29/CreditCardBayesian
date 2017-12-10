from pomegranate import *
import json
import matplotlib.pyplot as plt


def main():
	a = BayesianNetwork()

	with open("exact0.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Exact DP Algorithm on 5 other states")
	plt.savefig("exact5.png")

	with open("exact1.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Exact DP Algorithm on 6 other states")
	plt.savefig("exact6.png")

	with open("exact2.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Exact DP Algorithm on 7 other states")
	plt.savefig("exact7.png")

	with open("exact3.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Exact DP Algorithm on 8 other states")
	plt.savefig("exact8.png")

	with open("greedy0.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Greedy Algorithm on 5 other states")
	plt.savefig("greedy5.png")

	with open("greedy1.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Greedy Algorithm on 6 other states")
	plt.savefig("greedy6.png")

	with open("greedy2.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Greedy Algorithm on 7 other states")
	plt.savefig("greedy7.png")

	with open("greedy3.json","r") as f:
	  d = json.load(f)
	graph = a.from_json(d)
	plt.figure(dpi=300)
	graph.plot()
	plt.title("Greedy Algorithm on 8 other states")
	plt.savefig("greedy8.png")


if __name__ == '__main__':
	main()