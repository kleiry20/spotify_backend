from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Rating
from .serializers import RatingSerializer

@api_view(['GET'])
def RatingOverview(request):
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
    item = RatingSerializer(data=request.data)
  
    # validating for already existing data
    if Rating.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        rating = Rating.objects.get(song=item.data['song'], app_user=item.data['app_user']) 
        rating.update_rating()
        return Response(item.data)
    else:
        print(item.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Rating.objects.filter(**request.query_param.dict())
    else:
        items = Rating.objects.all()
  
    # if there is something in items else raise error
    if items:
        serializer = RatingSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_item(request, user_id, song_id):
    item = Rating.objects.get(app_user_id=user_id, song_id=song_id)
    data = RatingSerializer(instance=item, data=request.data)
  
    # if there is something in items else raise error
    if item:
        serializer = RatingSerializer(item)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_items(request, pk):
    item = Rating.objects.get(pk=pk)
    data = RatingSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        rating = Rating.objects.get(song=item.song.id, app_user=item.app_user.id) 
        rating.update_rating()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Rating, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
