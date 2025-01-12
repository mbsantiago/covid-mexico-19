import django_filters
from covid_data import models


class MunicipioSimpleFilter(django_filters.FilterSet):
    clave = django_filters.NumberFilter(
        help_text='Búsqueda exacta por clave.')
    clave_municipio = django_filters.NumberFilter(
        help_text='Búsqueda exacta por clave de municipio (dentro de la entidad.')

    descripcion = django_filters.CharFilter(
        help_text='Búsqueda exacta por descripción).')
    descripcion_contiene = django_filters.CharFilter(
        field_name='descripcion',
        help_text='Búsqueda exacta por descripción.',
        lookup_expr='icontains')

    entidad = django_filters.ModelChoiceFilter(
        queryset=models.Entidad.objects.all(),
        help_text=(
            'Entidad a la que pertenece el Municipio. Búsqueda exacta.'))
    entidad_clave = django_filters.NumberFilter(
        field_name='entidad__clave',
        help_text=(
            'Entidad a la que pertenece el Municipio. Búsqueda por clave.'))
    entidad_descripcion = django_filters.CharFilter(
        field_name='entidad__descripcion',
        help_text=(
            'Entidad a la que pertenece el Municipio. '
            'Búsqueda exacta por descripción.'))
    entidad_descripcion_contiene = django_filters.CharFilter(
        field_name='entidad__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Entidad a la que pertenece el Municipio. '
            'Búsqueda por descripción.'))

    class Meta:
        model = models.Municipio
        fields = []


class MunicipioFilter(MunicipioSimpleFilter):
    casos_positivos = django_filters.NumberFilter(
        help_text='Número de casos confirmados. Búsqueda exacta.',
        field_name='casos_positivos',
        label='Casos positivos')
    casos_positivos_gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados. Mayor que.',
        field_name='casos_positivos',
        lookup_expr='gt',
        label='Casos positivos mayor que')
    casos_positivos_lt = django_filters.NumberFilter(
        help_text='Número de casos confirmados. Menor que.',
        field_name='casos_positivos',
        lookup_expr='lt',
        label='Casos positivos menor que')
    casos_positivos_gte = django_filters.NumberFilter(
        help_text='Número de casos confirmados. Mayor o igual que.',
        field_name='casos_positivos',
        lookup_expr='gte',
        label='Casos positivos mayor o igual que')
    casos_positivos_lte = django_filters.NumberFilter(
        help_text='Número de casos confirmados. Menor o igual que.',
        field_name='casos_positivos',
        lookup_expr='lte',
        label='Casos positivos menor o igual que')

    casos_negativos = django_filters.NumberFilter(
        help_text='Número de casos negativos. Búsqueda exacta.',
        field_name='casos_negativos',
        label='Casos negativos')
    casos_negativos_gt = django_filters.NumberFilter(
        help_text='Número de casos negativos. Mayor que.',
        field_name='casos_negativos',
        lookup_expr='gt',
        label='Casos negativos mayor que')
    casos_negativos_lt = django_filters.NumberFilter(
        help_text='Número de casos negativos. Menor que.',
        field_name='casos_negativos',
        lookup_expr='lt',
        label='Casos negativos menor que')
    casos_negativos_gte = django_filters.NumberFilter(
        help_text='Número de casos negativos. Mayor o igual que.',
        field_name='casos_negativos',
        lookup_expr='gte',
        label='Casos negativos mayor o igual que')
    casos_negativos_lte = django_filters.NumberFilter(
        help_text='Número de casos negativos. Menor o igual que.',
        field_name='casos_negativos',
        lookup_expr='lte',
        label='Casos negativos menor o igual que')

    casos_sospechosos = django_filters.NumberFilter(
        help_text='Número de casos sospechosos. Búsqueda exacta.',
        field_name='casos_sospechosos',
        label='Casos sospechosos')
    casos_sospechosos_gt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos. Mayor que.',
        field_name='casos_sospechosos',
        lookup_expr='gt',
        label='Casos sospechosos mayor que')
    casos_sospechosos_lt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos. Menor que.',
        field_name='casos_sospechosos',
        lookup_expr='lt',
        label='Casos sospechosos menor que')
    casos_sospechosos_gte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos. Mayor o igual que.',
        field_name='casos_sospechosos',
        lookup_expr='gte',
        label='Casos sospechosos mayor o igual que')
    casos_sospechosos_lte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos. Menor o igual que.',
        field_name='casos_sospechosos',
        lookup_expr='lte',
        label='Casos sospechosos menor o igual que')

    defunciones_confirmadas = django_filters.NumberFilter(
        help_text='Número de defunciones de casos confirmados. Búsqueda exacta.',
        field_name='defunciones_confirmadas',
        label='Defunciones confirmadas')
    defunciones_confirmadas_gt = django_filters.NumberFilter(
        help_text='Número de defunciones de casos confirmados. Mayor que.',
        field_name='defunciones_confirmadas',
        lookup_expr='gt',
        label='Defunciones confirmadas mayor que')
    defunciones_confirmadas_lt = django_filters.NumberFilter(
        help_text='Número de defunciones de casos confirmados. Menor que.',
        field_name='defunciones_confirmadas',
        lookup_expr='lt',
        label='Defunciones confirmadas menor que')
    defunciones_confirmadas_gte = django_filters.NumberFilter(
        help_text='Número de defunciones de casos confirmados. Mayor o igual que.',
        field_name='defunciones_confirmadas',
        lookup_expr='gte',
        label='Defunciones confirmadas mayor o igual que')
    defunciones_confirmadas_lte = django_filters.NumberFilter(
        help_text='Número de defunciones de casos confirmados. Menor o igual que.',
        field_name='defunciones_confirmadas',
        lookup_expr='lte',
        label='Defunciones confirmadas menor o igual que')

    defunciones_sospechosas = django_filters.NumberFilter(
        help_text='Número de defunciones de casos sospechosos. Búsqueda exacta.',
        field_name='defunciones_sospechosas',
        label='Defunciones sospechosas')
    defunciones_sospechosas_gt = django_filters.NumberFilter(
        help_text='Número de defunciones de casos sospechosos. Mayor que.',
        field_name='defunciones_sospechosas',
        lookup_expr='gt',
        label='Defunciones sospechosas mayor que')
    defunciones_sospechosas_lt = django_filters.NumberFilter(
        help_text='Número de defunciones de casos sospechosos. Menor que.',
        field_name='defunciones_sospechosas',
        lookup_expr='lt',
        label='Defunciones sospechosas menor que')
    defunciones_sospechosas_gte = django_filters.NumberFilter(
        help_text='Número de defunciones de casos sospechosos. Mayor o igual que.',
        field_name='defunciones_sospechosas',
        lookup_expr='gte',
        label='Defunciones sospechosas mayor o igual que')
    defunciones_sospechosas_lte = django_filters.NumberFilter(
        help_text='Número de defunciones de casos sospechosos. Menor o igual que.',
        field_name='defunciones_sospechosas',
        lookup_expr='lte',
        label='Defunciones sospechosas menor o igual que')

    intubados_confirmados = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido intubados. Búsqueda exacta.',
        field_name='intubados_confirmados',
        label='Intubados confirmados')
    intubados_confirmados_gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido intubados. Mayor que.',
        field_name='intubados_confirmados',
        lookup_expr='gt',
        label='Intubados confirmados mayor que')
    intubados_confirmados_lt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido intubados. Menor que.',
        field_name='intubados_confirmados',
        lookup_expr='lt',
        label='Intubados confirmados menor que')
    intubados_confirmados_gte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido intubados. Mayor o igual que.',
        field_name='intubados_confirmados',
        lookup_expr='gte',
        label='Intubados confirmados mayor o igual que')
    intubados_confirmados_lte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido intubados. Menor o igual que.',
        field_name='intubados_confirmados',
        lookup_expr='lte',
        label='Intubados confirmados menor o igual que')

    intubados_sospechosos = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido intubados. Búsqueda exacta.',
        field_name='intubados_sospechosos',
        label='Intubados sospechosos')
    intubados_sospechosos_gt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido intubados. Mayor que.',
        field_name='intubados_sospechosos',
        lookup_expr='gt',
        label='Intubados sospechosos mayor que')
    intubados_sospechosos_lt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido intubados. Menor que.',
        field_name='intubados_sospechosos',
        lookup_expr='lt',
        label='Intubados sospechosos menor que')
    intubados_sospechosos_gte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido intubados. Mayor o igual que.',
        field_name='intubados_sospechosos',
        lookup_expr='gte',
        label='Intubados sospechosos mayor o igual que')
    intubados_sospechosos_lte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido intubados. Menor o igual que.',
        field_name='intubados_sospechosos',
        lookup_expr='lte',
        label='Intubados sospechosos menor o igual que')

    hospitalizados_confirmados = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido hospitalizados. Búsqueda exacta.',
        field_name='hospitalizados_confirmados',
        label='Hospitalizados confirmados')
    hospitalizados_confirmados_gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido hospitalizados. Mayor que.',
        field_name='hospitalizados_confirmados',
        lookup_expr='gt',
        label='Hospitalizados confirmados mayor que')
    hospitalizados_confirmados_lt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido hospitalizados. Menor que.',
        field_name='hospitalizados_confirmados',
        lookup_expr='lt',
        label='Hospitalizados confirmados menor que')
    hospitalizados_confirmados_gte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido hospitalizados. Mayor o igual que.',
        field_name='hospitalizados_confirmados',
        lookup_expr='gte',
        label='Hospitalizados confirmados mayor o igual que')
    hospitalizados_confirmados_lte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que han sido hospitalizados. Menor o igual que.',
        field_name='hospitalizados_confirmados',
        lookup_expr='lte',
        label='Hospitalizados confirmados menor o igual que')

    hospitalizados_sospechosos = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido hospitalizados. Búsqueda exacta.',
        field_name='hospitalizados_sospechosos',
        label='Hospitalizados sospechosos')
    hospitalizados_sospechosos_gt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido hospitalizados. Mayor que.',
        field_name='hospitalizados_sospechosos',
        lookup_expr='gt',
        label='Hospitalizados sospechosos mayor que')
    hospitalizados_sospechosos_lt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido hospitalizados. Menor que.',
        field_name='hospitalizados_sospechosos',
        lookup_expr='lt',
        label='Hospitalizados sospechosos menor que')
    hospitalizados_sospechosos_gte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido hospitalizados. Mayor o igual que.',
        field_name='hospitalizados_sospechosos',
        lookup_expr='gte',
        label='Hospitalizados sospechosos mayor o igual que')
    hospitalizados_sospechosos_lte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que han sido hospitalizados. Menor o igual que.',
        field_name='hospitalizados_sospechosos',
        lookup_expr='lte',
        label='Hospitalizados sospechosos menor o igual que')

    ambulatorios_confirmados = django_filters.NumberFilter(
        help_text='Número de casos confirmados que son ambulatorios. Búsqueda exacta.',
        field_name='ambulatorios_confirmados',
        label='Ambulatorios confirmados')
    ambulatorios_confirmados_gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que son ambulatorios. Mayor que.',
        field_name='ambulatorios_confirmados',
        lookup_expr='gt',
        label='Ambulatorios confirmados mayor que')
    ambulatorios_confirmados_lt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que son ambulatorios. Menor que.',
        field_name='ambulatorios_confirmados',
        lookup_expr='lt',
        label='Ambulatorios confirmados menor que')
    ambulatorios_confirmados_gte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que son ambulatorios. Mayor o igual que.',
        field_name='ambulatorios_confirmados',
        lookup_expr='gte',
        label='Ambulatorios confirmados mayor o igual que')
    ambulatorios_confirmados_lte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que son ambulatorios. Menor o igual que.',
        field_name='ambulatorios_confirmados',
        lookup_expr='lte',
        label='Ambulatorios confirmados menor o igual que')

    ambulatorios_sospechosos = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que son ambulatorios. Búsqueda exacta.',
        field_name='ambulatorios_sospechosos',
        label='Ambulatorios sospechosos')
    ambulatorios_sospechosos_gt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que son ambulatorios. Mayor que.',
        field_name='ambulatorios_sospechosos',
        lookup_expr='gt',
        label='Ambulatorios sospechosos mayor que')
    ambulatorios_sospechosos_lt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que son ambulatorios. Menor que.',
        field_name='ambulatorios_sospechosos',
        lookup_expr='lt',
        label='Ambulatorios sospechosos menor que')
    ambulatorios_sospechosos_gte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que son ambulatorios. Mayor o igual que.',
        field_name='ambulatorios_sospechosos',
        lookup_expr='gte',
        label='Ambulatorios sospechosos mayor o igual que')
    ambulatorios_sospechosos_lte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que son ambulatorios. Menor o igual que.',
        field_name='ambulatorios_sospechosos',
        lookup_expr='lte',
        label='Ambulatorios sospechosos menor o igual que')

    criticos_confirmados = django_filters.NumberFilter(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos. Búsqueda exacta.',
        field_name='criticos_confirmados',
        label='Criticos confirmados')
    criticos_confirmados_gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos. Mayor que.',
        field_name='criticos_confirmados',
        lookup_expr='gt',
        label='Criticos confirmados mayor que')
    criticos_confirmados_lt = django_filters.NumberFilter(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos. Menor que.',
        field_name='criticos_confirmados',
        lookup_expr='lt',
        label='Criticos confirmados menor que')
    criticos_confirmados_gte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos. Mayor o igual que.',
        field_name='criticos_confirmados',
        lookup_expr='gte',
        label='Criticos confirmados mayor o igual que')
    criticos_confirmados_lte = django_filters.NumberFilter(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos. Menor o igual que.',
        field_name='criticos_confirmados',
        lookup_expr='lte',
        label='Criticos confirmados menor o igual que')

    criticos_sospechosos = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos. Búsqueda exacta.',
        field_name='criticos_sospechosos',
        label='Criticos sospechosos')
    criticos_sospechosos_gt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos. Mayor que.',
        field_name='criticos_sospechosos',
        lookup_expr='gt',
        label='Criticos sospechosos mayor que')
    criticos_sospechosos_lt = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos. Menor que.',
        field_name='criticos_sospechosos',
        lookup_expr='lt',
        label='Criticos sospechosos menor que')
    criticos_sospechosos_gte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos. Mayor o igual que.',
        field_name='criticos_sospechosos',
        lookup_expr='gte',
        label='Criticos sospechosos mayor o igual que')
    criticos_sospechosos_lte = django_filters.NumberFilter(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos. Menor o igual que.',
        field_name='criticos_sospechosos',
        lookup_expr='lte',
        label='Criticos sospechosos menor o igual que')


    class Meta:
        model = models.Municipio
        fields = []
