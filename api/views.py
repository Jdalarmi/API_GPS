from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.http import JsonResponse
from api.models import Address, Position
from api.serializers import AddressSerializer,PositionSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=AddressSerializer)
@api_view(['POST'])
def register_address(request):
    """
    Exemplo de corpo da requisição:

    {
        "nome": "Nome do estabelecimento",
        "x": "Cordenada x",
        "y": "Crodenada y"
    }
    """
    if request.method == 'GET':
        raise APIException(403, 'Sem acesso get')
    
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response("Invalid")

@api_view(["GET"])
def get_all_address(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=PositionSerializer)
@api_view(["POST"])
def get_location(request):

    """
    Exemplo de corpo da requisição:

    {
        "campo X": "Cordenada x",
        "campo y": "Cordenada y
    }
    """

    data = request.data

    position_x = data['position_x']
    position_y = data['position_y']


    d_max = abs(position_x - position_y)

    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    serializer = serializer.data

    lista_resultado = []
    
    for objeto in serializer:
        lista = [objeto['name']]
        x = abs(objeto['x'] - position_x)
        y =abs(objeto['y'] - position_y)
        soma_x_y = x + y
        if soma_x_y <= d_max:
            lista_resultado.append(lista)
        
   
    return Response(lista_resultado, status=status.HTTP_200_OK)

@swagger_auto_schema(method='put')
@api_view(['PUT'])
def delete_by_id(request, pk):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Metodo não permitido'}, status.HTTP_400_BAD_REQUEST)
    try:
        address = Address.objects.get(id=pk)
        address.delete()
        return Response(f'Endereço foi deletado com sucesso!', status=200)
    except Address.DoesNotExist:
        return Response('Esse endereço não se encontra na base de dados', status=500)