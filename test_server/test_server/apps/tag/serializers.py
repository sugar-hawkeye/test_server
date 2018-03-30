from rest_framework import serializers

from .models import Tag
from django.contrib.auth.models import User


# class TagSerializer(serializers.Serializer):
#     tag_id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=15)
#     priority = serializers.IntegerField()
#     is_publish = serializers.BooleanField(default=False)
#
#     def create(self, validated_data):
#         return Tag.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.priority = validated_data.get('priority',instance.priority)
#         instance.is_publish= validated_data.get('is_publish', instance.is_publish)
#         instance.save()
#         return instance



# ###### ModelSerializer
#
# class TagSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.id')
#     class Meta:
#         model = Tag
#         fields = ('tag_id','title','priority','is_publish','owner')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'tags')






#########  HyperlinkedModelSerializer

# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     # owner = serializers.ReadOnlyField(source='owner.id')
#
#     class Meta:
#         model = Tag
#         fields = ('tag_id', 'title', 'priority', 'is_publish', 'owner','url')
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail',read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'tags')







##########   nested objects

class UserSerializer(serializers.ModelSerializer):
    # tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')

class TagSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()



    class Meta:
        model = Tag
        fields = ('tag_id','title','priority','is_publish','owner')
        depth = 2

        # list_serializer_class = ResponseSerializer

