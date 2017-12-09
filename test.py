from pebl import data
from pebl.learner import greedy

print('HELl0')
dataset = data.fromfile("data.csv")
dataset.discretize()
print(dataset)
dataset.discretize()
learner = greedy.GreedyLearner(dataset, max_iterations=10000)
ex1result = learner.run()
ex1result.tohtml("example1-result")