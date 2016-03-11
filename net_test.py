from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# make dataset
ds = SupervisedDataSet(2, 2)

# add samples
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((0,0), (0,0))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))
ds.addSample((1,1), (1,1))

# build network
net = buildNetwork(2,3,2)

# make trainer
trainer = BackpropTrainer(net, ds)

#train
print('Training....')
trainer.trainUntilConvergence()


#tests
print('testing (0,0) -> should give (0,0)')
print(net.activate([0,0]))

print(' ')
print('testing (1,1) -> should give (1,1)')
print(net.activate([1,1]))
