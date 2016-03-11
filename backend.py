from pybrain.tools.shortcuts import buildNetwork
from pycproject.readctree import CProject, CTree
import os

class Backend:

    net = buildNetwork(2, 3, 1)

    def get_table_data():
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

    def update_net(ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''

    def generate_test_data(inputfolder):
        testdata = CProject(os.getcwd(),"testdata")
        for ctree in testdata.get_ctrees():
            yield ctree.get_classifier_features()