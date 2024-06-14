from django.db import models


# Create your models here.
class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'