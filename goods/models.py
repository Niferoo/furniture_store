from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length= 150, unique = True, verbose_name = "Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name = "URL")

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(verbose_name="Цена", default=0.00, max_digits=7, decimal_places=2 )
    discount = models.DecimalField(verbose_name="Скидка", default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0,)

    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категория")

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} Количесво - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount :
            return round(self.price - ((self.price * self.discount)/100), 2)

        return self.price
