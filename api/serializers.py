from rest_framework import serializers
from main.models import MyList

# from django.contrib.auth import get_user_model


class NonModelSerializer(serializers.Serializer):
    """Сериализатор с не-модельными полями."""


# class MyListSerializer(serializers.HyperlinkedModelSerializer):
class MyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyList
        # fields = "__all__"
        # fields = ("id", "desc", "date_add", "date_end", "chk_end")
        fields = tuple(v.attname for v in MyList._meta.fields)
        # read_only_fields = fields
