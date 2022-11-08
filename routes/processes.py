"""
__Seed builder__
  Extended module
"""

import seed.routes.processes as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Process
from app.serializers import ProcessSerializer
from domain.process import create_process, characters_uniques
from domain.process import decimal_to_roman, get_characters

class ProcessViewSet(SeedRoute.ProcessViewSet):
    @action(detail = False, methods = ["POST"])
    def decimal_to_roman(self, request):
      data = request.data
      has_fields_or_400(data, "user_id", "input")
      decimal = int(data["input"])
      user_id = int(data["user_id"])
      converted = create_process(decimal, user_id)
      return Response(status = status.HTTP_201_CREATED, data = converted)
    
    @action(detail=True, methods = ['GET'])
    def characters(self, request, pk = None):
      res = get_characters(pk)
      return Response(status=status.HTTP_200_OK, data = res)