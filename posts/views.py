from .serializers import LanguageSerializers,ParadigmSerializers,ProgrammerSerializers
from rest_framework import viewsets, permissions

from .models import Language,Paradigm,Programmer


class ParadigmViewSet(viewsets.ModelViewSet):
    
    serializer_class = ParadigmSerializers
    queryset = Paradigm.objects.all()
   

class LanguageViewSet(viewsets.ModelViewSet):
    
    serializer_class = LanguageSerializers
    queryset = Language.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProgarammerViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProgrammerSerializers
    queryset = Programmer.objects.all()
