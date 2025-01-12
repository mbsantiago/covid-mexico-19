from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoSiNoVista(CatalogoVista):
    queryset = models.SiNo.objects.all()
    serializer_class = otros.SiNoSerializer

    def list(self, *args, **kwargs):
        """
        Si No - Valores posibles.

        Regresa la lista de valores posibles para los campos de tipo "SíNo",
        según el formato de la información liberada. No requiere parámetros.
        Ejemplo:

            <host:port>/api/catalogos/si_no/

        """
        return super().list(*args, **kwargs)
