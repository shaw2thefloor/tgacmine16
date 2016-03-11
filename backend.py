from pybrain.tools.shortcuts import buildNetwork
from pycproject.readctree import CProject, CTree
import os
import os.path
import json

class Backend:

    typenet = buildNetwork(2, 3, 1)

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

    def generate_test_data(self, inputfolder):
        curdir = os.getcwd()
        testdata = CProject(curdir, "testdata")
        for ctree in testdata.get_ctrees():
            yield ctree.get_classifier_features()
            
# b = Backend()
# print(b.get_table_data())