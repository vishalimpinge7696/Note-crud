from django.db import models

# Create your models here.


class Note(models.Model):
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'note'
        verbose_name_plural = 'NOTE'
        managed = True

    def __str__(self):
        return self.note