from import_export import resources, fields
from import_export.widgets import ManyToManyWidget

from movies.models import Genre, Region
from .models import MovieApp


class MovieAppResource(resources.ModelResource):
    genres = fields.Field(
        column_name='genres',  # Название столбца в файле
        attribute='genre',  # Название поля ManyToMany в модели
        widget=ManyToManyWidget(Genre, separator=',', field='name')  # Указываем модель Genre и разделитель
    )
    regions = fields.Field(
        column_name='regions',  # Название столбца в файле
        attribute='regions',  # Название поля ManyToMany в модели
        widget=ManyToManyWidget(Region, separator=',', field='name')  # Указываем модель Genre и разделитель
    )

    class Meta:
        model = MovieApp
        fields = (
            'name',
            'year',
            'rolled_certificate',
            'category__name',
            'kind__name',
            'timing',
            'actors',
            'age_limit__name',
            'logline',
            'debut',
            'music',
            'country',
            'other_country',
            'other_region',
            'other_shooting_group',
            'agreement_to_placement',
            'agreement_to_vote',
            'agreement_to_no_commerce_show',
            'created_date',
            'portfolio',
            'copyright_information__possessor',
            'genres',
            'regions'
            )
