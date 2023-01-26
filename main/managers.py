from django.db import models
from django.db.models import QuerySet


class MyListManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        qs: QuerySet = super().get_queryset()
        qs = qs.annotate(
            # chk_end=models.Value("date_end", output_field=models.BooleanField())
            # chk_end=models.F("date_end"). .__eq__(models.Value(None))
            # chk_end=models.Value("date_end", output_field=models.CharField()).bitand(
            #     models.Value(True)
            # )
            # chk_end=models.ExpressionWrapper(
            #     models.Value("date_end"), output_field=models.BooleanField()
            # )
            # chk_end=models.Value("False")
            chk_end=models.Case(
                models.When(date_end=None, then=models.Value("False")),
                # models.When(registered_on__lte=a_month_ago, then=models.Value("5%")),
                default=models.Value("True"),
            )
        )
        print(qs.query)
        return qs
