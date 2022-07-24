from audioop import avg
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

parser_classes = (MultiPartParser, FormParser)

@api_view(['GET'])
def SongOverview(request):
	api_urls = {
		'all_songs': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/song/pk/delete'
	}

	return Response(api_urls)
  
@api_view(['POST'])
def add_items(request):
    files = request.FILES
    post_data = request.POST
    data = {
        'name': post_data.get("name"), 
        'date_of_release': post_data.get("date_of_release"),
        'artist': post_data.get("artist"),
        'avg_rating': post_data.get("avg_rating"),
        'image': files.get("image"),
    }

    item = SongSerializer(data=data)
  
    # validating for already existing data
    if Song.objects.filter(**data).exists():
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
        items = Song.objects.filter(**request.query_param.dict()).annotate(rating_count=Sum('avg_rating')).order_by('-rating_count')[:10]
    else:
        items = Song.objects.all().annotate(rating_count=Sum('avg_rating')).order_by('-rating_count')[:10]
  
    # if there is something in items else raise error
    if items:
        serializer = SongSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_items(request, pk):
    item = Song.objects.get(pk=pk)
    data = SongSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Song, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
