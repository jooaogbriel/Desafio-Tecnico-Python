from rest_framework import serializers


class StorageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    owner = serializers.CharField()
