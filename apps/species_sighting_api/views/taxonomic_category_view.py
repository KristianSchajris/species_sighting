from rest_framework           import  viewsets
from rest_framework.response  import  Response
from rest_framework           import  status
from django.shortcuts         import  get_object_or_404

from ..models        import  TaxonomicCategory
from  ..serializers  import  TaxonomicCategorySerializer

class TaxonomicCategoryViewSet(viewsets.GenericViewSet):

    '''
        Metodos relacionados a las opreaciones del modelo TaxonomicCategory.
    '''

    queryset         = TaxonomicCategory.objects.all()
    serializer_class = TaxonomicCategorySerializer

    def list(self, request):
        '''
            Enpoint para listar todos los registros de la tabla TaxonomicCategory.

            Retorna una lista con los registros de la tabla TaxonomicCategory.
        '''
        serializer = TaxonomicCategorySerializer(self.queryset, many=True)

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
            Enpoint para obtener un registro de la tabla TaxonomicCategory.

            Resive como parametro el id de un registro Taxonomico.
        '''
        taxonomic_category = get_object_or_404(self.queryset, pk=pk)
        serializer         = TaxonomicCategorySerializer(taxonomic_category)

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
            Enpoint para crear un registro de la tabla TaxonomicCategory.

            Resive como parametro un json con los datos de un registro Taxonomico.
        '''
        serializer = TaxonomicCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se realizo correctamente.',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Lo sentimos no hay registros.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': serializer.errors
        })
    
    def update(self, request, pk=None):
        '''
            Enpoint para actualizar un registro de la tabla TaxonomicCategory.

            Resive como parametro un json con los datos de un registro Taxonomico.
        '''
        taxonomic_category = get_object_or_404(self.queryset, pk=pk)
        serializer         = TaxonomicCategorySerializer(taxonomic_category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'message': 'El registro se actualizo correctamente.',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        
        return Response({
            'message': 'Lo sentimos no hay registros.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': serializer.errors
        })


    def destroy(self, request, pk=None):
        '''
            Enpoint para eliminar un registro de la tabla TaxonomicCategory.

            Resive como parametro el id de un registro Taxonomico.
        '''
        taxonomic_category = get_object_or_404(self.queryset, pk=pk)

        if taxonomic_category:
            taxonomic_category.delete()
            
            return Response({
                'message': 'El registro se elimino correctamente.',
                'status': status.HTTP_200_OK,
                'data': taxonomic_category
            })
        
        return Response({
            'message': 'Ocurrio un error intente de nuevo.',
            'status': status.HTTP_404_NOT_FOUND,
            'data': {}
        })
