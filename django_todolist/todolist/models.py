from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updata_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    class Meta:
        db_table = "list"

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at,
            "updata_at": self.updata_at,
            "deleted_at": self.deleted_at
        }