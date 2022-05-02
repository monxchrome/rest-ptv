from django.contrib import admin
from .models import City, Statistics


class StatisticsInlineAdmin(admin.StackedInline):
    model = Statistics
    extra = 0
    inline_classes = ('grp-collapse grp-open',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title', )
    list_editable = ('title', )
    inline_classes = ('grp-collapse grp-open',)
    inlines = [StatisticsInlineAdmin]

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    pass