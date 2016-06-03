from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

import os
import os.path
import json
import jsonpickle as pickle
import input_classes
import pdb


class Backend:
    def __init__(self):
        pass



    def get_net(self):
        fileObject = open('neural_net.json', 'w')
        return pickle.load(fileObject)



    def get_table_data(self):

        data = [{'keywords': ['regulatory T-cells', 'human regulatory T-cells', 'infection', 'vaccination', 'pathogens',
                              'tuberculosis', 'leprosy', 'BCG'],
                 'authors': ['Mardi C. Boer', 'Simone A. Joosten', 'Tom H. M. Ottenhoff'],
                 'journal': 'Frontiers in Immunology',
                 'title': 'Regulatory T-Cells at the Interface between Human Host and Pathogens in Infectious Diseases and Vaccination'},
                {'keywords': [],
                 'authors': ['Jolanta Kolodziejek', 'Bernhard Seidel', 'Christof Jungbauer', 'Katharina Dimmel',
                             'Michael Kolodziejek', 'Ivo Rudolf', 'Zdenek Hubálek', 'Franz Allerberger',
                             'Norbert Nowotny'],
                 'journal': 'PLoS ONE',
                 'title': 'West Nile Virus Positive Blood Donation and Subsequent Entomological Investigation, Austria, 2014'},
                {'keywords': [],
                 'authors': ['Gloria Omosa-Manyonyi', 'Juliet Mpendo', 'Eugene Ruzagira', 'William Kilembe',
                             'Elwyn Chomba',
                             'François Roman', 'Patricia Bourguignon', 'Marguerite Koutsoukos', 'Alix Collard',
                             'Gerald Voss',
                             'Dagna Laufer', 'Gwynn Stevens', 'Peter Hayes', 'Lorna Clark', 'Emmanuel Cormier',
                             'Len Dally',
                             'Burc Barin', 'Jim Ackland', 'Kristen Syvertsen', 'Devika Zachariah', 'Kamaal Anas',
                             'Eddy Sayeed', 'Angela Lombardo', 'Jill Gilmour', 'Josephine Cox', 'Patricia Fast',
                             'Frances Priddy'], 'journal': 'PLoS ONE',
                 'title': 'A Phase I Double Blind, Placebo-Controlled, Randomized Study of the Safety and Immunogenicity of an Adjuvanted HIV-1 Gag-Pol-Nef Fusion Protein and Adenovirus 35 Gag-RT-Int-Nef Vaccine in Healthy HIV-Uninfected African Adults'},
                {'keywords': [],
                 'authors': ['Kraisak Kesorn', 'Phatsavee Ongruk', 'Jakkrawarn Chompoosri', 'Atchara Phumee',
                             'Usavadee Thavara', 'Apiwat Tawatsin', 'Padet Siriyasatien'],
                 'journal': 'PLoS ONE',
                 'title': 'Morbidity Rate Prediction of Dengue Hemorrhagic Fever (DHF) Using the Support Vector Machine and the '},
                {'keywords': [], 'authors': ['Federico Giovannoni', 'Elsa B. Damonte', 'Cybele C. García'],
                 'journal': 'PLoS ONE',
                 'title': 'Cellular Promyelocytic Leukemia Protein Is an Important Dengue Virus Restriction Factor'}]

        return data



    def update_net(self, ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''
        fc = input_classes.FeatureClassification()
        net = self.get_net()



    '''
    def generate_test_data(self, inputfolder):
        curdir = os.getcwd()
        testdata = CProject(curdir, "testdata")
        for ctree in testdata.get_ctrees():
            yield ctree.get_classifier_features()
    '''
