from rest_framework           import  viewsets
from rest_framework.response  import  Response
from rest_framework           import  status
from django.shortcuts         import  get_object_or_404

from ..models       import  Place
from ..serializers  import  PlaceSerializer

class PlaceViewSet(viewsets.GenericViewSet):
    '''
        Enpoints para realizar operaziones relacionadas al modelos Place.
    '''

    queryset         = Place.objects.all()
    serializer_class = PlaceSerializer

    def list(self, request):
        '''
            Endpoint para obtener todos los lugares registrados en el sistema.

            retorna una lista con los datos de los lugares registrados en el sistema.
        '''

        serializer = PlaceSerializer(self.queryset, many=True)

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
    

    def retrieve(self, request, pk=None):
        '''
            Endopint para obtener los datos de un lugar especifico registrado en el sistema.

            Resive el id de lugar y retorna la data relacionada al id.
        '''

        place       = get_object_or_404(self.queryset, pk=pk)
        serializer  = PlaceSerializer(place)

        if serializer.data:
            return Response({
                'message': 'La peticion se realizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        else:
            return Response({
                'message': 'La especie no se encuentra registrada en el sistema.',
                'status': status.HTTP_404_NOT_FOUND,
                'data': serializer.errors
            })
    

    def create(self, request):
        '''
            Endpoint para registrar un lugar nuevo en el sistema.

            Resive los datos de un lugar a rergistrar en el sistema 
            y retorna la data del lugar registrado si la peticion 
            se realiza correctamente.
        '''
        serializer = PlaceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se realizo correctamente.',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': serializer.errors
        })
    

    def update(self, request, pk=None):
        '''
            Endpoint para actualizar datos de un lugar registrado en el sistema.

            Resive el id de un lugar registrado y la data a actualizar,
            si la peticion se realiza correctamente retorna la data del lugar actualizado
            de lo contrario retorna un mensaje de error.
        '''
        place      = get_object_or_404(self.queryset, pk=pk)
        serializer = PlaceSerializer(place, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se actualizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': serializer.errors
        })

    def destroy(self, request, pk=None):
        '''
            Endpoint para eliminar un lugar registrado en el sistema.

            Resive el id de un lugar que se desea eliminar 
            si la peticion se realiza correctamente retorna 
            un mensaje de exito,de lo contrario retorna 
            un mensaje de error.
        '''
        place = get_object_or_404(self.queryset, pk=pk)

        if place:
            place.delete()

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
