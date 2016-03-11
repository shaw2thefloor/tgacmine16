from pybrain.tools.shortcuts import buildNetwork

class Backend:

    net = buildNetwork(2, 3, 1)

    def get_table_data():
        '''
            get pre-boosted data for front-end display
        '''
        return "hello larry"

    def update_net(ids=[]):
        '''
            ids is an array of document ids the features of which
            will be used to update the classifier
        '''
