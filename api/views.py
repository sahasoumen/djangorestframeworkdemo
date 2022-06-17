from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from base.models import Project
from .serializers import ProjectSerializer


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def project(request, pk):
    try:
        p = Project.objects.get(pk=pk)

        if request.method == 'PUT':
            return update(request, p)
        elif request.method == 'DELETE':
            p.delete()
            return Response({'message': 'Project deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = ProjectSerializer(p)
            return Response(serializer.data)

    except Project.DoesNotExist:
        return Response({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)


def update(request, p):
    serializer = ProjectSerializer(p, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
