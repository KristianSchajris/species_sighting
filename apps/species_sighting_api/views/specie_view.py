from rest_framework           import  viewsets
from rest_framework.response  import  Response
from rest_framework           import  status
from django.shortcuts         import  get_object_or_404

from ..models       import  Specie
from ..serializers  import  SpecieSerializer

class SpecieViewSet(viewsets.GenericViewSet):
    '''
        Metodos relacionados con la tabla Specie.
    '''
    queryset         = Specie.objects.all()
    serializer_class = SpecieSerializer

    def list(self, request):
        '''
            Endpoint para listar todos los registros de la tabla Specie.

            Retorna una lista de todos los registros de la tabla Specie.
        '''
        serializer = SpecieSerializer(self.queryset, many=True)

        if len(serializer.data) == 0:
            return Response({
                'message': 'Actulmente no exiten registros de especies en el sistema.',
                'status': status.HTTP_404_NOT_FOUND,
                'data': []
            })
        
        return Response({
            'message': 'La peticion se realizo correctamente.',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })


    def retrieve(self, request, pk=None):
        '''
            Endpoint para obtener un registro de la tabla Specie.

            Resive como parametro una primary key de un 
            registro de la tabla Specie y retorna los datos 
            relacionados con el registro.
        '''
        queryset   = Specie.objects.all()
        specie     = get_object_or_404(queryset, pk=pk)
        serializer = SpecieSerializer(specie)

        if serializer.data:
            return Response({
                'message': 'La peticion se realizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Lo sentimos no hay registros.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': serializer.errors
        })


    def create(self, request):
        '''
            Endpoint para crear un registro de la tabla Specie.

            Resive como parametro un los datos para realizar un registro de la tabla Specie.
        '''
        serializer = SpecieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se realizo correctamente.',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Lo sentimos ocurrio un error intete nuevamente.',
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })
    

    def update(self, request, pk=None):
        '''
            Endpoint para actualizar un registro de la tabla Specie.

            Resive como parametro la primary key del registro a actualizar y un request
            con los datos a actualizar.
        '''
        specie     = get_object_or_404(self.queryset, pk=pk)
        serializer = SpecieSerializer(specie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro fue actualizado correctamente.',
                'status': status.HTTP_202_ACCEPTED,
                'data': serializer.data
            })
    
        return Response({
            'message': 'Ocurrio un orror intete de nuevo.',
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })
    

    def destroy(self, request, pk=None):
        '''
            Endpoint para eliminar un registro de la tabla Specie.

            Resive como parametro la primary key del registro a eliminar y 
            retorna los datos del registro eliminado, de lo contrario 
            retorna un mensaje mensaje de error.
        '''
        specie = get_object_or_404(self.queryset, pk=pk)

        if specie:
            specie.delete()
            
            return Response({
                'message': 'El registro fue eliminado correctamente.',
                'status': status.HTTP_200_OK,
                'data': {}
            })
        
        return Response({
            'message': 'Ocurrio un orror intete de nuevo.',
            'status': status.HTTP_400_BAD_REQUEST,
            'data': {}
        })
