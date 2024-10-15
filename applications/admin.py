from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats.base_formats import XLSX

from .models import Status, MovieApp, SpecialistApp, MoviePortfolio, MovieContract, CopyrightInformation
from .resources import MovieAppResource


# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MovieApp)
class MovieAppAdmin(ImportExportActionModelAdmin):
    resource_class = MovieAppResource
    formats = [XLSX]
    list_display = ('name', 'status', 'agreement_to_placement', 'agreement_to_vote', 'agreement_to_no_commerce_show')
    list_filter = ('genre',)
    search_fields = ('name', 'shooting_group__last_name')

    fields = (
        'user',
        'status',
        'name',
        'debut',
        'agreement_to_placement',
        'agreement_to_vote',
        'agreement_to_no_commerce_show',
        'kind',
        'category',
        'genre',
        'timing',
        'logline',
        'year',
        'rolled_certificate',
        'age_limit',
        'country',
        'other_country',
        'regions',
        'other_region',
        'locality',
        'get_shooting_group',
        'actors',
        'other_shooting_group',
        'get_portfolio_data',
        'get_copying_info',
        'contract',
        'shooting_group',
    )

    readonly_fields = ('get_shooting_group', 'get_portfolio_data', 'get_copying_info')

    def get_detail(self, spec_id):

        content = f"""
        <a target="_blank" style="margin-left: 20px;"class="related-widget-wrapper-link view-related" 
        id="view_id_Movie_shooting_group-0-mainshootinggroup" 
        data-href-template="/admin/movies/mainshootinggroup/__fk__/change/?_to_field=id" 
        title="Просмотреть выбранный объект" 
        href="/admin/movies/mainshootinggroup/{spec_id}/change/?_to_field=id">
        <img src="/static/admin/img/icon-viewlink.svg" alt="" width="20" height="20">
        </a>
        """
        return content

    def get_shooting_group(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        for i in obj.shooting_group.all():
            context += (
                    f'<li class="list-group-item"><strong>{i.speciality.name}</strong> {i.last_name} '
                    f'{i.first_name} - {i.birthday} {self.get_detail(i.pk)}</li>')
        context += "</ul>"
        return mark_safe(context)

    def get_portfolio_data(self, obj):
        context = '<div style="display: flex;"><div>'

        context += f"<strong>{obj.portfolio._meta.get_field('festivals').verbose_name}:</strong> <p>{obj.portfolio.festivals}</p>"
        context += f"<strong>{obj.portfolio._meta.get_field('internet').verbose_name}:</strong> <p>{obj.portfolio.internet}</p>"
        context += f"<strong>{obj.portfolio._meta.get_field('smi').verbose_name}:</strong> <p>{obj.portfolio.smi}</p>"
        context += f"<strong>{obj.portfolio._meta.get_field('materials').verbose_name}:</strong> <p>{obj.portfolio.materials}</p>"
        context += "</div>"
        context += f"""<a class="related-widget-wrapper-link change-related" id="change_id_copyright_information" 
        data-href-template="/admin/applications//movieportfolio/__fk__/change/?_to_field=id&amp;_popup=1" 
        data-popup="yes" title="Изменить выбранный объект типа " Информация="" о="" правообладателе""="" 
        href="/admin/applications/movieportfolio/{obj.portfolio.pk}/change/?_to_field=id&amp;_popup=1">
        <img src="/static/admin/img/icon-changelink.svg" alt="" width="20" height="20"></a>"""

        context += "</div>"
        return mark_safe(context)

    def get_copying_info(self, obj):
        context = '<div style="display: flex;"><div>'

        context += f"<strong>{obj.copyright_information._meta.get_field('possessor').verbose_name}:</strong> <p>{obj.copyright_information.possessor}</p>"
        context += f"<strong>{obj.copyright_information._meta.get_field('possessor_email').verbose_name}:</strong> <p>{obj.copyright_information.possessor_email}</p>"
        context += f"<strong>{obj.copyright_information._meta.get_field('phone').verbose_name}:</strong> <p>{obj.copyright_information.phone}</p>"
        context += f"<strong>{obj.copyright_information._meta.get_field('contact_email').verbose_name}:</strong> <p>{obj.copyright_information.contact_email}</p>"
        context += "</div>"
        context += f"""<a class="related-widget-wrapper-link change-related" id="change_id_copyright_information" 
        data-href-template="/admin/applications//movieportfolio/__fk__/change/?_to_field=id&amp;_popup=1" 
        data-popup="yes" title="Изменить выбранный объект типа " Информация="" о="" правообладателе""="" 
        href="/admin/applications/movieportfolio/{obj.copyright_information.pk}/change/?_to_field=id&amp;_popup=1">
        <img src="/static/admin/img/icon-changelink.svg" alt="" width="20" height="20"></a>"""

        context += "</div>"
        return mark_safe(context)

    get_shooting_group.short_description = "Съемочная группа"
    get_portfolio_data.short_description = " Портфолио"
    get_copying_info.short_description = " Информация о правообладателе"


@admin.register(SpecialistApp)
class SpecialistAppAdmin(admin.ModelAdmin):
    pass


@admin.register(MoviePortfolio)
class MoviePortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(CopyrightInformation)
class CopyrightInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieContract)
class MovieContractAdmin(admin.ModelAdmin):
    pass
