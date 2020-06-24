from django.db import models
import uuid

class File(models.Model):

  file = models.FileField(blank=False, null=False)
  img_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  #remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)