from rest_framework import serializers

from doctor.models import Specialization, Doctor


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorDetailSerializer(DoctorSerializer):
    specializations = SpecializationSerializer(many=True, read_only=True)
