from django.db import models


class Gymkhana_body(models.Model):
    nameofbody = models.CharField(max_length=100, default="Gymkhana")
    secretary_name = models.CharField(max_length=100, default="Secy")

    def __str__(self):
        return self.nameofbody
