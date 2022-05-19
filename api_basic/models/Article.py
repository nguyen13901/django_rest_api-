import uuid
from api_basic.models.Author import Author

from django.db import models
from django.utils import timezone


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    create_at = models.DateTimeField(default=timezone.now())
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id}\nauthor: {self.author}\ntitle: {self.title}'

    class Meta:
        db_table = "article"
