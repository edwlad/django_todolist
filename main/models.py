from django.db import models
from datetime import datetime

# from .managers import MyListManager


class MyList(models.Model):
    # objects = MyListManager()

    desc = models.CharField(
        max_length=120,
        help_text="Описание задачи",
        verbose_name="Задача",
    )
    date_add = models.DateTimeField(
        default=datetime.now,
        help_text="Дата создания задачи",
        verbose_name="Создано",
    )
    date_end = models.DateTimeField(
        default=None,
        help_text="Дата завершения задачи",
        verbose_name="Завершено",
        blank=True,
        null=True,
    )
    chk_end = models.BooleanField(
        default=False,
        help_text="Завершить",
        verbose_name="",
    )

    def __str__(self) -> str:
        return f"{self.id}: {self.desc}"

    def save(self, *args, **kwargs) -> None:
        if self.chk_end and self.date_end is None:
            self.date_end = datetime.now()
        elif not self.chk_end and self.date_end is not None:
            self.date_end = None
        return super().save(*args, **kwargs)
