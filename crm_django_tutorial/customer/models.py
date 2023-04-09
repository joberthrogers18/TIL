from django.db import models


class Customer(models.Model):
    """
    Class model about customers users
    """
    name = models.CharField("Name", max_length=255)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
