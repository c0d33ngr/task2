from enum import Enum
from rest_framework import serializers

ENUM = (
    ("addition", "addition"),
    ("subtraction", "subtraction"),
    ("multiplication", "multiplication")
)

class CalculationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=ENUM)
    x = serializers.IntegerField()
    y = serializers.IntegerField()
