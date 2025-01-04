from django.db.models import (Model, CharField, TextField, 
                            ForeignKey, SlugField,
                            IntegerField, PROTECT,
                            DateField, ImageField)


class Category(Model):
    slug = SlugField()
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

class BooksItems(Model):
    image = ImageField(default='https://i.pinimg.com/736x/3a/0c/9f/3a0c9f94bc5b671de539935368e75565.jpg')
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    description = TextField()
    price = IntegerField()
    date = DateField()
    category = ForeignKey(Category, on_delete=PROTECT, default=1)

    def __str__(self):
        return self.title