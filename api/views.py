from django.shortcuts import render  # noqa
from rest_framework import viewsets
from main.models import MyList
from .serializers import MyListSerializer
from django.db.models import QuerySet


class MyListApi(viewsets.ModelViewSet):
    queryset = MyList.objects.all().order_by("-date_add")
    serializer_class = MyListSerializer
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    # filterset_class =  MyListFilterSet

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()
        par = self.request.query_params

        if temp := par.get("title", ""):
            qs = qs.filter(desc__iregex=rf"{temp}")

        if temp := par.get("ordering", ""):
            temp = temp.lower().replace(" ", "")
            try:
                tuple(map(qs.model._meta.get_field, temp.replace("-", "").split(",")))
                qs = qs.order_by(*temp.split(","))
            except Exception:
                pass

        if temp := par.get("is_active", "").lower():
            match temp:
                case "1" | "true":
                    qs = qs.filter(chk_end=False)
                case "0" | "false":
                    qs = qs.filter(chk_end=True)
        return qs
