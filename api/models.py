from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FarmType(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Farm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms")
    farm_area = models.IntegerField(max_length=50)
    trap_count = models.IntegerField(max_length=1000)
    farm_type_id = models.ForeignKey(FarmType, on_delete=models.DO_NOTHING)
    farm_raw_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def farm_type(self):
        return self.farm_type_id.title

    def __str__(self) -> str:
        return self.user_id+'\'s user farm'

