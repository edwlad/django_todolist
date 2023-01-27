from django.contrib import admin
from django.db import models
from .models import MyList
from datetime import datetime


@admin.register(MyList)
class MyListAdmin(admin.ModelAdmin):
    # def chk_end(self, obj):
    #     """Вычисляемое значение для только-читаемого поля."""
    #     # return obj.date_end is not None
    #     return obj.chk_end

    # list_display = tuple(v.attname for v in MyList._meta.fields)
    list_display = ("id", "desc", "date_add", "chk_end", "date_end")
    fields = ("desc", "date_add", ("chk_end", "date_end"))
    search_fields = ("desc",)
    # readonly_fields = ("date_end",)
    # list_filter = ("date_add", "date_end")

    actions = ("make_on_end", "make_off_end", "make_not_end")

    @admin.action(description="Выполнить задачи")
    def make_on_end(self, request, queryset: models.QuerySet):
        queryset.update(chk_end=True, date_end=datetime.now())

    @admin.action(description="Отменить выполнение задачи")
    def make_off_end(self, request, queryset: models.QuerySet):
        queryset.update(chk_end=False, date_end=None)

    @admin.action(description="Изменить статус выполнения")
    def make_not_end(self, request, queryset: models.QuerySet):
        # for item in queryset:
        #     item.chk_end = not item.chk_end
        #     item.save()
        queryset.update(
            chk_end=models.Case(
                models.When(chk_end=True, then=False),
                default=True,
            ),
            date_end=models.Case(
                models.When(chk_end=True, then=None),
                default=datetime.now(),
            ),
        )


# admin.site.register(MyList, MyListAdmin)
