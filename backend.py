from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pycproject.readctree import CProject, CTree
import os
import os.path
import json
import pickle

import pdb

class Backend:


    def __init__(self):
        # first try and load saved network
        try:
            fileObject = open('neural_net.json','r')
        except FileNotFoundError:
            net = buildNetwork(n, 3, 1)
            fileObject = open('neural_net.json','w')
            pickle.dump(net, fileObject)


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


        # at this point, for each document in paper_list, run through the net with
        # boost_coeffcient = net.activate(paper_list[x])
        # use this boost coefficient to rank the results in the form
        # where alpha can be adjusted to give greater or lesser weight to the net boost

        #alpha = 0.3
        #rank = alpha * search_rank + 1-alpha * boost_coeffcient

        return paper_list


    def update_net(self, ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''
        net = self.get_net()

        # get features for id

        # convert strings to numerics

        # build the trainer
        # ds = SupervisedDataSet(n, 1) - where n is the number of features

        # make trainer
        # trainer = BackpropTrainer(net, ds)
        # trainer.trainUntilConvergence()

        # save net out to file




    def generate_test_data(self, inputfolder):
        pdb.set_trace()
        curdir = os.getcwd()
        testdata = CProject(curdir, inputfolder)
        for ctree in testdata.get_ctrees():
            yield ctree.get_classifier_features()


# b = Backend()
# print(b.get_table_data())
