from django.db import models
from datetime import datetime
from .managers import MyListManager


class MyList(models.Model):
    objects = MyListManager()

    desc = models.CharField(
        max_length=120,
        help_text="Описание задачи",
    )
    date_add = models.DateTimeField(
        default=datetime.now,
        help_text="Дата создания задачи",
        db_index=True,
    )
    date_end = models.DateTimeField(
        default=None,
        help_text="Дата выполнения задачи",
        blank=True,
        null=True,
        db_index=True,
    )

    def __str__(self) -> str:
        return " | ".join(f"{v}: {getattr(self, v)}" for v in ("id", "desc"))
