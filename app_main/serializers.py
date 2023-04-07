from rest_framework import serializers
from .models import Videocard, VideocardInfo


class VideocardInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideocardInfo
        fields = '__all__'


class VideocardListSerializer(serializers.ModelSerializer):
    info = VideocardInfoListSerializer(many=False)

    class Meta:
        model = Videocard
        fields = '__all__'


class VideocardDetailSerializer(serializers.ModelSerializer):
    info = VideocardInfoListSerializer(many=False)

    class Meta:
        model = Videocard
        fields = '__all__'
