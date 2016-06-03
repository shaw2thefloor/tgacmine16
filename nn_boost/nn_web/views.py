from django.shortcuts import render
from django.http import HttpResponse
from backend import Backend
from input_classes import FeatureClassification
from Featurize import Featurize as feature

def index(request):

    if 'f' in request.session:
        fe = request.session['fe']
    else:
        fe = feature()




    author = request.GET.get('author')
    print(fe.get_category(author))
    # get json rep of papers
    data = Backend().get_table_data()

    request.session['f'] = fe


    return render(request, 'pubs_list.html', {'data': data})
