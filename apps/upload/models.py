from django.db import models


class Code(models.Model):
    code_id = models.CharField(max_length=64, null=False, blank=False)
