from django.db.models import CharField, IntegerField, Model

# from django_boost.models.mixins import LogicalDeletionMixin


class Book(Model):
    title = CharField(max_length=100, null=True)
    price = IntegerField(default=0)

    class Meta:
        db_table = "books"
