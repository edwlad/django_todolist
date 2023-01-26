from django.contrib import admin
from .models import MyList


@admin.register(MyList)
class MyListAdmin(admin.ModelAdmin):
    def chk_end(self, obj):
        """Вычисляемое значение для только-читаемого поля."""
        # return obj.date_end is not None
        return obj.chk_end

    # list_display = tuple(v.attname for v in MyList._meta.fields)
    list_display = ("id", "desc", "date_add", "date_end", "chk_end")
    search_fields = ("desc",)
    readonly_fields = ("chk_end",)
