from django.core.management.base import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):
    help = 'Populates the Product table with initial data'

    def handle(self, *args, **options):
        categories = [
            Category(name=item, description=f'Description for {item}')
            for item in ['Cars', 'Goods', 'Phones', 'Cats', 'Dogs']
        ]
        created_categories = Category.objects.bulk_create(categories)
        print(created_categories[2].name)
        category = Category.objects.filter(name='Phones')[0]

        products = [
            Product(
                name=f'Iphone {str(index)}',
                description=f'Description of Iphone{str(index)}',
                price=100.00 + index,
                qty=index*5,
                category=category
            )
            for index in range(1, 15)]
        Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS('Product and Category tables are successfully populated.'))
