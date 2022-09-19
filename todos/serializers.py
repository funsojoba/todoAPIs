from rest_framework import serializers

from .models import Todo


class TodoSerializers(serializers.ModelSerializers):
    class Meta:
        fields (
            "id",
            "title",
            "body",
        )