from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        class Meta:
            model = models.BoastsRoastsModel
            fields = ['id','isroast','post_body','post_upvote' ,'post_downvote','date_created','last_update','s_key','total']
