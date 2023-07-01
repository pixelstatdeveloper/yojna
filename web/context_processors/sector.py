from yojna.models import SectorModel


def index(request):
    sectors = SectorModel.objects.all()
    return {'sectors': sectors}
