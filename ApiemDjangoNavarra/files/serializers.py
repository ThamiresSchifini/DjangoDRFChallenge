from rest_framework import serializers
from ApiemDjangoNavarra.files.models import fileHistory

class FileHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = fileHistory
        fields = ['name', 'id']

    @staticmethod
    def list_to_JSON(fileHistory):
        file_serializer_history=[]
        for register in fileHistory:
            file_serializer_history.append(FileHistorySerializer(register).data)
        return file_serializer_history