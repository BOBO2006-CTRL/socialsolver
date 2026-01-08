from django.db import models


class Issue(models.Model):

    CATEGORY_CHOICES = [
        ("roads", "Дороги"),
        ("housing", "ЖКХ"),
        ("transport", "Транспорт"),
        ("ecology", "Экология"),
        ("other", "Другое"),
    ]

    STATUS_CHOICES = [
        ("new", "На рассмотрении"),
        ("done", "Решено"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="other",
        blank=True,     # 🔹 ВАЖНО
        null=True       # 🔹 ВАЖНО
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title