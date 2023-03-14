from rest_framework                 import  viewsets, status, filters
from rest_framework.response        import  Response
from rest_framework.decorators      import  action
from django_filters.rest_framework  import  DjangoFilterBackend
from django.shortcuts               import  get_object_or_404

from ..models       import  Sighting
from ..serializers  import  SightingSerializer

class SightingViewSet(viewsets.GenericViewSet, filters.SearchFilter):
    '''
        Metodos relacionados con la operaciones de la tabla Sighting.
    '''
    queryset         = Sighting.objects.all()
    serializer_class = SightingSerializer


    def list(self, request):
        '''
            Endpoint para obtener un listado de registros de la tabla Sighting.

            Retorna un listado de registros de la tabla Sighting.
        '''
        serializer = SightingSerializer(self.queryset, many=True)

        if serializer.data:
            return Response({
                'message': 'La peticion se realizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Lo sentimos no hay registros.',
            'status': status.HTTP_404_NOT_FOUND,
        })

    def retrieve(self, request, pk=None):
        '''
            Endpoint para obtener un registro de la tabla Sighting.

            Resive como parametro una primary key y retorna un registro de la tabla Sighting.
        '''
        sighting   = get_object_or_404(self.queryset, pk=pk)
        serializer = SightingSerializer(sighting, many=False)

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
            Endpoint para crear un registro de la tabla Sighting.

            Resive como parametro una request con los datos para la creacion 
            de un avistamiento y retorna un registro de la tabla Sighting.
        '''
        serializer = SightingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se creo correctamente.',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })


    def update(self, request, pk=None):
        '''
            Endpoint para actualizar un registro de la tabla Sighting.

            Resive como parametro una request con los datos para la actualizacion 
            y el id del registro a actualizar y retorna los datos del registro 
            actualizado.
        '''
        sighting   = get_object_or_404(self.queryset, pk=pk)
        serializer = SightingSerializer(sighting, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se actualizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })
    

    def destroy(self, request, pk=None):
        '''
            Endpoint para eliminar un registro de la tabla Sighting.

            Resive como parametro una primary key del registro a eliminar 
            y retorna un mensaje de confirmacion, si la peticion se 
            realizo correctamente, de lo contrario retornara un menaje de error.
        '''
        sighting = get_object_or_404(self.queryset, pk=pk)

        if sighting:
            sighting.delete()

            return Response({
                'message': 'El registro se elimino correctamente.',
                'status': status.HTTP_200_OK,
                'data': {}
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': {}
        })
