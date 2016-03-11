from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pycproject.readctree import CProject, CTree
import os

class Backend:

    def __init__(self):
        # first try and load saved network
        try:
            fileObject = open('neural_net.json','r')
        except FileNotFoundError:
            net = buildNetwork(2, 3, 1)
            fileObject = open('neural_net.json','w')
            pickle.dump(net, fileObject)

    def get_net(self):
        fileObject = open('neural_net.json', 'w')
        return pickle.load(fileObject)

    def get_table_data(self):
        '''
            get pre-boosted data for front-end display
        '''
        return ["Battling Zika in Brazil",
                       "A crucial time for public health preparedness: Zika virus and the 2016 Olympics, Umrah, and Hajj",
                       "Offline: Brazil-the unexpected opportunity that Zika presents",
                       "Zika Virus on the Move.",
                       "Zika, and rapid diagnostic tests for malaria",
                       "Research bodies vow to share data on Zika",
                       "Scientists probe Zika link to birth defects",
                       "Proving Zika link to birth defects poses huge challenge.",
                       "Severe eye damage in infants with microcephaly is presumed to be due to Zika virus",
                       "Healthcare staff encouraged to warn patients of the risks of the Zika virus"]

    def update_net(self, ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''
        net = get_net()
        


    def generate_test_data(inputfolder):
        testdata = CProject(os.getcwd(),"testdata")
        for ctree in testdata.get_ctrees():
            yield ctree.get_classifier_features()
