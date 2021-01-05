from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from . import serializers
from . import models

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Posts to be viewed"""
    queryset = models.BoastsRoastsModel.objects.all()
    serializers_class = serializers.PostSerializer

    @action(detail=False)
    def boasts(self,request,pk=None):
        all_boast = models.BoastsRoastsModel.objects.filter(isboats=False).order_by('-date_created')
        serializer = self.get_serializer(all_boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self,request,pk=None):
        all_roasts = models.BoastsRoastsModel.objects.filter(isroast=False).order_by('-date_created')
        serializer = self.get_serializer(all_roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def heighest_rated(self,request,pk=None):
        all_boasts = models.BoastsRoastsModel.objects.all()
        sort_post_by_vote = list(all_boasts)
        sort_post_by_vote = sorted(sort_post_by_vote, key=lambda a: a.total,reverse=True)
        serializer = self.get_serializer(sort_post_by_vote, many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=['post'])
    def upvote(self,request,pk=None):
        post = models.BoastsRoastsModel.objects.get(id=pk)
        post.post_upvote = post.post_upvote + 1 
        post.save()
        return Response({'status': 'ok'})

    @action(detail=True,methods=['post'])
    def downvote(self,request,pk=None):
        post = models.BoastsRoastsModel.objects.get(id=pk)
        post.post_downvote = post.post_downvote - 1 
        post.save()
        return Response({'status': 'ok'})
