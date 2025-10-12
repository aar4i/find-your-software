from django.db import models

class Software(models.Model):
    name = models.CharField(max_length=255, unique=True)
    features = models.TextField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'software'
        managed = False  # Django won't manage the table's lifecycle;
        verbose_name = 'Software'
        verbose_name_plural = 'Software'

    def __str__(self):
        return self.name