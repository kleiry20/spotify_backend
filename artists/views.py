from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer

@api_view(['GET'])
def ArtistOverview(request):
	api_urls = {
		'all_artists': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/artist/pk/delete'
	}

	return Response(api_urls)
  
@api_view(['POST'])
def add_items(request):
    item = ArtistSerializer(data=request.data)
  
    # validating for already existing data
    if Artist.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Artist.objects.filter(**request.query_param.dict()).annotate(rating_count=Sum('avg_rating')).order_by('-rating_count')[:10]
    else:
        items = Artist.objects.all().annotate(rating_count=Sum('avg_rating')).order_by('-rating_count')[:10]
  
    # if there is something in items else raise error
    if items:
        serializer = ArtistSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_items(request, pk):
    item = Artist.objects.get(pk=pk)
    data = ArtistSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Artist, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
