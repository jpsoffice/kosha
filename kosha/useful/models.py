from django.db.models import Model, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, auto_now_add=False, editable=False)

    class Meta:
        abstract = True
