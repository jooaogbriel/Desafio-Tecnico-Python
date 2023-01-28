from rest_framework import serializers
from storage.serializers import StorageSerializer
from storage.models import Storage
from .models import Datas

class DatasSerializer(serializers.Serializer):
    type_data = serializers.CharField()
    date = serializers.DateField()
    value = serializers.FloatField()
    cpf = serializers.CharField()
    card = serializers.CharField()
    hour = serializers.TimeField()

    storage = StorageSerializer(write_only=True)

    type_description = serializers.SerializerMethodField()

    def get_type_description(self, obj: Datas) -> str:
        datas_types_descriptions = [
            'débito',
            'boleto',
            'financiamento',
            'crédito',
            'recebimento empréstimo',
            'vendas',
            'recebimento TED',
            'recebimento DOC',
            'aluguel'
        ]

        data_type = int(obj.type_data) - 1

        return datas_types_descriptions[data_type]

    def create(self, validated_data: dict):
        storage_data = validated_data.pop('storage')
        print(storage_data)
        storage, _ = Storage.objects.get_or_create(**storage_data, defaults={**storage_data})

        data = Datas.objects.create(**validated_data, storage=storage)

        return data