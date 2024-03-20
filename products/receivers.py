from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Product, ProductHistory


@receiver(pre_save, sender=Product)
def track_product_quantity_changes(sender, instance, **kwargs):
    if instance.pk:  # Проверяем, существует ли уже объект в базе данных (т.е. является ли это обновлением)
        old_product = Product.objects.get(pk=instance.pk)
        if old_product.qty != instance.qty:  # Проверяем, изменилось ли количество продукта
            ProductHistory.objects.create(
                product=instance,
                product_data={
                    "old_qty": old_product.qty,
                    "new_qty": instance.qty,
                }
            )