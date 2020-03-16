from django.views.decorators.csrf import csrf_exempt

from ApiemDjangoNavarra.files.models import fileHistory
<<<<<<< HEAD
from ApiemDjangoNavarra.files.serializers import FileHistorySerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import requests


def create_histogram_from_file(file):
=======
from rest_framework import viewsets
from ApiemDjangoNavarra.files.serializers import FileHistorySerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

#class FileHistoryViewsSet(viewsets.ModelViewSet):
 #   queryset = fileHistory.objects.all()
  #  serializer_class = FileHistorySerializer

def rank(tupla):
    return tupla[1]
    # lambda arg: arg[1]

def quadrado(n):
    return n**2
    # lambda n: n**2


def create_histogram(file):
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92
    histogram_dict = {}
    for line in file:
        for char in str(line):
            if char.isalpha():
                char = char.upper()
                histogram_dict[char] = histogram_dict.get(char, 0) + 1

    return sorted(histogram_dict.items(), key=lambda arg: arg[1], reverse=True)

<<<<<<< HEAD
def create_histogram_from_content(content):
    histogram_dict = {}

    for char in str(content):
        if char.isalpha():
            char = char.upper()
            histogram_dict[char] = histogram_dict.get(char, 0) + 1

    return sorted(histogram_dict.items(), key=lambda arg: arg[1], reverse=True)

=======
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92
@csrf_exempt
def files(request):
    return_dict = {'errors': []}

    if request.method == 'GET':
        # acessou sem formulario
        files_history = fileHistory.objects.all()
        return_dict['files_history'] = FileHistorySerializer.list_to_JSON(files_history)
<<<<<<< HEAD
=======
        # return HttpResponse(JSONRenderer().render(FileHistorySerializer(files_history)))

>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92

    if request.method == 'POST':
        # acessou via formulario
        if 'file' in request.FILES:
            new_register = fileHistory()
            new_register.name = (request.FILES['file']).name
            new_register.save()
<<<<<<< HEAD
            return_dict['histogram'] = create_histogram_from_file( request.FILES['file'] )            #arquivo
=======
            return_dict['histogram'] = create_histogram( request.FILES['file'] )            #arquivo
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92

        else:
            return_dict['errors'].append('Por favor insira um arquivo válido.')

    return HttpResponse(JSONRenderer().render(return_dict))
<<<<<<< HEAD


def remote(request):
    return_dict = {'errors': []}
    url = request.GET.get('url')

    resposta = requests.get(url)
    if resposta.status_code == 404:
        return_dict['errors'].append('Por favor insira uma url válida.')

    return_dict['histogram'] = create_histogram_from_content( resposta.content )

    return HttpResponse(JSONRenderer().render(return_dict))
=======
    #return render(request, 'fileUpload.html', return_dict)
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92



