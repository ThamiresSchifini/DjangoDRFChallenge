from django.views.decorators.csrf import csrf_exempt

from ApiemDjangoNavarra.files.models import fileHistory
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
    histogram_dict = {}
    for line in file:
        for char in str(line):
            if char.isalpha():
                char = char.upper()
                histogram_dict[char] = histogram_dict.get(char, 0) + 1

    return sorted(histogram_dict.items(), key=lambda arg: arg[1], reverse=True)

@csrf_exempt
def files(request):
    return_dict = {'errors': []}

    if request.method == 'GET':
        # acessou sem formulario
        files_history = fileHistory.objects.all()
        return_dict['files_history'] = FileHistorySerializer.list_to_JSON(files_history)
        # return HttpResponse(JSONRenderer().render(FileHistorySerializer(files_history)))


    if request.method == 'POST':
        # acessou via formulario
        if 'file' in request.FILES:
            new_register = fileHistory()
            new_register.name = (request.FILES['file']).name
            new_register.save()
            return_dict['histogram'] = create_histogram( request.FILES['file'] )            #arquivo

        else:
            return_dict['errors'].append('Por favor insira um arquivo válido.')

    return HttpResponse(JSONRenderer().render(return_dict))
    #return render(request, 'fileUpload.html', return_dict)



