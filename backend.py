from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pycproject.readctree import CProject, CTree
import os
import os.path
import json
import jsonpickle as pickle
import input_classes

class Backend:


    def __init__(self, inputfolder):
        # first try and load saved network
        try:
            fileObject = open('neural_net.json','r')
        except FileNotFoundError:
            net = buildNetwork(2, 3, 1)
            fileObject = open('neural_net.json','w')
            pickle.dump(net, fileObject)
        # access data
        self.data = CProject(os.getcwd(), inputfolder)


    def get_net(self):
        fileObject = open('neural_net.json', 'w')
        return pickle.load(fileObject)


    def get_table_data(self):
        '''
            get pre-boosted data for front-end display
        '''

        paper_list = []
        for td in self.generate_test_data("testdata"):
            paper_list.append(td)

        return paper_list

    def update_net(self, ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''
        net = get_net()
        fc = input_classes.FeatureClassification()

        features = []
        for _id in ids:
            features.append(self.data.get_ctree(_id).get_classifier_features)
        


    def generate_test_data(self):
        for ctree in self.data.get_ctrees():
            yield ctree.get_classifier_features()


# b = Backend()
# print(b.get_table_data())
