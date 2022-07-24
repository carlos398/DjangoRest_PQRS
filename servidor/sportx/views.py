from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status
from sportx.models import PQRS
from sportx. serializers import PqrsSerializer


@api_view(['GET'])
def BackendInfo(request):
    """ 
    Endpoint para entregar información requerida acerca de como son manejados 
    desde el backend los tipos de documento, es decir lo que necesita el front 
    para mostrar la lista en el formulario y a su vez de como se lo debe entregar 
    al backend para registrarlo en la base de datos 
    
    ----------------------------------------------------------------------------
    Entregar información requerida acerca de como son manejados desde el backend 
    los tipos de PQR, es decir lo que necesita el front para mostrar la lista en 
    el formulario y a su vez de como se lo debe entregar al backend para registrarlo
     en la base de datos
    
    """

    how_it_works = [

            "Primero que todo la informacion en el backend se maneja en JavaScript Object Notation (JSON)",
            "es un formato basado en texto estándar para representar datos estructurados ",
            "en la sintaxis de objetos de JavaScript.",
            
            "se ven de la misma forma que estas viendo la iformacion de este texto, una llave y un valor",

            "pero buno vamos a lo importante, que necesita el frontend para mostrar la lista en el formulario",
            "y a su vez de como se lo debe entregar al backend para registrarlo en la base de datos"

            "nuestro front solamente necesita acceder al endpoint donde se encuentre ubicada la API",
            "segun corresponde lo que quiera hacer, es decir, si quiere listar objetos solamente debe acceder",

            "a la ruta: https://host:puerto/api/pqrs/ (en el caso  de esta app)  o segun corresponda la ruta que el backend le asigne al listado de objetos",

            "donde el recibira una lista de objetos en formato JSON que podra recorrer y mostrar segun corresponda en el formulario",
            "o en una tabla ",

            "en caso de que quiera comunicarse con la API del backend siempre debe hacerlo mediante una peticion HTTP ya sea",
            "GET POST PUT DELETE segun lo que guste hacer",

            "que hace cada peticion? lo listaremos a continuacion",

            "GET: es para obtener un objeto o una lista de objetos",
            "POST: es para crear un objeto",
            "PUT: es para actualizar un objeto",
            "DELETE: es para eliminar un objeto",

            "de esa forma el frontend podra seleccionar que metodo puede usar en el respectivo endpoint segun lo que corresponda hacer",
            
    ]


    how_to_use = [ " primero que todo el frontend necesitara acceder a la API de la siguiente forma:",

            "http://localhost:8000/api/pqrs/ con una peticion GET",
            "donde 'localhost' es el nombre del servidor, '8000' es el puerto, y 'api' es el inicio de nuestro endpoint",
            "y 'pqrs' es la parte final de nuestro endpoint donde conseguiremos la lista de objetos en formato JSON",

            "para crear un objeto, necesitamos acceder a la siguiente forma:",
            "http://localhost:8000/api/pqrs/create con metodo POST",
            "este endpoint nos permitira crear un objeto en formato JSON",
            "que deben ser enviados en el cuerpo de la solicitud",

            "para acceder a un objeto en particular, necesitamos acceder a la siguiente forma:", 
            "http://localhost:8000/api/pqrs/<id> con metodo GET",
            "donde 'id' es el id del objeto que queremos obtener",

            "en este endpoint podemos obtener el objeto que busquemos al pasar la pk en el endpoint con un metodo GET",
            "o podemos actualizar el objeto que busquemos al pasar la pk en el endpoint con un metodo PUT",
            "o podemos eliminar el objeto que busquemos al pasar la pk en el endpoint con un metodo DELETE",

            "para eliminar un varios objetos, necesitamos acceder a la siguiente forma:",
            "http://localhost:8000/api/pqrs/deleteseveral/<pks> con metodo DELETE",
            "donde 'pks' es una lista de ids separados por comas, que son los ids de los objetos que queremos eliminar "]

    return Response({'how it works': how_it_works, 'how_to_use': how_to_use})


@api_view(['GET'])
def PqrsList(request):
    """ 
    Endpoint para entregar la lista de PQRS registrados en la base de datos 
    
    ----------------------------------------------------------------------------
    Endpoint to display the list of PQRS registered in the database. 
    
    """

    pqrs = PQRS.objects.all()
    serializer = PqrsSerializer(pqrs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def PqrsCreate(request):
    """ 
    Endpoint para registrar un nuevo PQRS en la base de datos 
    
    ----------------------------------------------------------------------------
    Endpoint to register a new PQRS in the database. 
    
    """

    serializer = PqrsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def PqrsDetail(request, pk):
    """ 
    Endpoint para entregar la información de un PQRS en particular 
    
    ----------------------------------------------------------------------------
    Endpoint to display the information of a PQRS in particular. 
    
    """
    try:
        pqrs = PQRS.objects.get(pk=pk)
    except PQRS.DoesNotExist:
        return Response(
            data={'message': 'PQRS with id {} does not exist'.format(pk)},
            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PqrsSerializer(pqrs)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PqrsSerializer(pqrs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        pqrs.delete()
        return Response(data={'message': 'success fully deleted'} ,status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def DeleteSeveralPqrs(request, pks):
    """ 
    Endpoint para eliminar varios PQRS de la base de datos 
    
    ----------------------------------------------------------------------------
    Endpoint to delete several PQRS from the database. 
    
    """

    pks = pks.split(',')
    for pk in pks:
        try:
            pqrs = PQRS.objects.get(pk=pk)
        except PQRS.DoesNotExist:
            return Response(
                data={'message': 'PQRS with id {} does not exist'.format(pk)},
                status=status.HTTP_400_BAD_REQUEST)
        pqrs.delete()
    return Response(data={'message': f'{pks}success fully deleted'} ,status=status.HTTP_204_NO_CONTENT)