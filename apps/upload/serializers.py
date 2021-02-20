from rest_framework.serializers import ModelSerializer
from .models import Code


class CodeSerializer(ModelSerializer):
    MESSAGE_TYPE = 'compile-code'
    VERSION = 1
    KEY_FIELD = None

    class Meta:
        model = Code
        fields = ['code_id']
