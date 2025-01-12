import os
import datetime

from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand
from covid_update.descarga import descargar_datos
from covid_update.actualizar.casos import actualizar_casos


class Command(BaseCommand):
    help = 'Actualizar los casos de la base de datos de COVID'

    def add_arguments(self, parser):
        parser.add_argument(
            '--log',
            type=str,
            help='Ruta al archivo de log')
        parser.add_argument(
            '--verbose',
            action='store_true')
        parser.add_argument(
            '--descargar',
            action='store_true',
            help='Descargar los datos')
        parser.add_argument(
            '--forzar',
            action='store_true',
            help='Ignorar actualizaciones recientes')

    def handle(self, *args, **options):
        if options['descargar']:
            mensaje = 'Descargando datos...'
            self.stdout.write(self.style.NOTICE(mensaje))
            descargar_datos()

        log = options.get('log', None)
        if log is None:
            directorio = os.path.join(
                settings.BASE_DIR,
                settings.DATOS_BASE_DIR,
                settings.LOGS_DIR)

            if not os.path.exists(directorio):
                os.makedirs(directorio)

            fecha = datetime.datetime.now().isoformat()
            log = os.path.join(directorio, f'{fecha}.log')

        if options['verbose']:
            log = None

        forzar = options.get('forzar', False)
        mensaje = 'Actualizando casos'
        self.stdout.write(self.style.NOTICE(mensaje))
        codigo = actualizar_casos(log=log, forzar=forzar)

        if codigo == 0:
            cache.clear()

            mensaje = 'Datos actualizados correctamente'
            self.stdout.write(self.style.SUCCESS(mensaje))
        elif codigo == 1:
            mensaje = (
                'No hay datos nuevos que actualizar. Si no los '
                'has descargado corre de nuevo con la opcion '
                '--descargar.')
            self.stdout.write(self.style.WARNING(mensaje))
        else:
            mensaje = 'Error inesperado'
            self.stdout.write(self.style.ERROR(mensaje))
