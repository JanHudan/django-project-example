from api.models import *
from api.serializers import *
from api.src.mixins import RequestHandler

class TesterAPI(RequestHandler):
    queryset = TesterModel.objects.all()
    serializer_class = TesterSerializer

class CompanyAPI(RequestHandler):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

class ProjectAPI(RequestHandler):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class HardwareAPI(RequestHandler):
    queryset = HardwareModel.objects.all()
    serializer_class = HardwareSerializer