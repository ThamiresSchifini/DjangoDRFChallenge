from django.views.decorators.csrf import csrf_exempt

from ApiemDjangoNavarra.files.models import fileHistory
from ApiemDjangoNavarra.files.serializers import FileHistorySerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import requests


def create_histogram_from_file(file):
    histogram_dict = {}
    for line in file:
        for char in str(line):
            if char.isalpha():
                char = char.upper()
                histogram_dict[char] = histogram_dict.get(char, 0) + 1

    return sorted(histogram_dict.items(), key=lambda arg: arg[1], reverse=True)

def create_histogram_from_content(content):
    histogram_dict = {}

    for char in str(content):
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

    if request.method == 'POST':
        # acessou via formulario
        if 'file' in request.FILES:
            new_register = fileHistory()
            new_register.name = (request.FILES['file']).name
            new_register.save()
            return_dict['histogram'] = create_histogram_from_file( request.FILES['file'] )            #arquivo

        else:
            return_dict['errors'].append('Por favor insira um arquivo válido.')

    return HttpResponse(JSONRenderer().render(return_dict))


def remote(request):
    return_dict = {'errors': []}
    url = request.GET.get('url')

    resposta = requests.get(url)
    if resposta.status_code == 404:
        return_dict['errors'].append('Por favor insira uma url válida.')

    return_dict['histogram'] = create_histogram_from_content( resposta.content )

    return HttpResponse(JSONRenderer().render(return_dict))



