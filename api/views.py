from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CalculationSerializer



@api_view(['POST'])
def calculation(request):
    operation_type = request.data['operation_type']

    serializer = CalculationSerializer(data=request.data)
    if serializer.is_valid():
        operation_type = serializer.validated_data['operation_type']
        x = serializer.validated_data['x']
        y = serializer.validated_data['y']

        if operation_type == "addition":
            result = x + y
        if operation_type == "subtraction":
            result = x - y
        if operation_type == "multiplication":
            result = x * y

    output = {
        "slackUsername": "c0d33ngr",
        "operation_type": operation_type,
        "result": result
    }
    return Response(output)
