from movielist_app.models import Review, Watchlist, StreamPlatform, Review
from rest_framework import status
from movielist_app.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from movielist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

from rest_framework import mixins
from rest_framework import generics


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist,
                                                review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("you have already reviewed this movie")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['ratings']
        else:
            watchlist.avg_rating = (watchlist.avg_rating +
                                    serializer.validated_data['ratings']) / 2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]


# class ReviewDetails(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamDetailsAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Platform not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerisalizer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Show not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            movie = Watchlist.objects.get(pk=pk)
        movoie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ! this bellow code is using the function based views
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method =='GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'nhi mila movie'},status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method =='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method =='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)