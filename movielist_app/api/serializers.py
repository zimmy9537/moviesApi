from rest_framework import serializers
from movielist_app.models import Watchlist, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Review
        exclude=('watchlist',)
        # fields="__all__"

class WatchlistSerializer(serializers.ModelSerializer):
    
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Watchlist
        fields = "__all__"

    def validate_title(self, title):
        if len(title) < 5:
            raise serializers.ValidationError("Name is too short")
        else:
            return title

    def validate(self, attrs):
        if attrs['title'] == attrs['storyline']:
            raise serializers.ValidationError(
                "title and the storyline can not be same")
        return attrs


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchlistSerializer(many=True,read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active=serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, name):
#         if len(name)<5:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return name

#     def validate(self, attrs):
#         if attrs['name']==attrs['description']:
#             raise serializers.ValidationError("name and the description can not be same")
#         return attrs