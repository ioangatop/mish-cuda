from rest_framework_mongoengine.serializers import DocumentSerializer
from . import models


class allSerializer(DocumentSerializer):
    class Meta:
        model = models.USPTO_all
        fields = '__all__'  # 这个是将所有的字段都序列化


class partSerializer(DocumentSerializer):
    class Meta:
        model = models.USPTO_all
        #fields = '__all__'
        fields = ['_id', 'reaction_smiles', 'reference', 'temperature']
