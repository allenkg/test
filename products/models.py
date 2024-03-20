from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db.models import JSONField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(
        verbose_name=_('Product name'),
        max_length=30,
        blank=False,
        null=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(50)]
    )
    description = models.TextField(
        verbose_name=_('Product description'),
        max_length=500,
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        verbose_name=_('Product price'),
        max_digits=10,
        decimal_places=2,
        validators=[MaxValueValidator(99999999), MinValueValidator(0)],
        default=0,
    )
    qty = models.IntegerField(
        verbose_name=_('Product quantity'),
        validators=[MaxValueValidator(99999999), MinValueValidator(0)],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        related_query_name="product",
    )


class ProductHistory(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now)
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True,
    )
    product_data = JSONField(default=dict())
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
