from django.db import migrations

def add_products(apps, schema_editor):
    Product = apps.get_model('api', 'Product')
    products = [
        {"id": 1, "name": "Круассан", "description": "Свежий круассан с маслом", "price": 600, "category": "pastry", "image": "https://img.freepik.com/premium-photo/delicious-fresh-pastry-croissant-french-croissant-breakfast_198067-115371.jpg"},
        {"id": 2, "name": "Пирог с яблоком", "description": "Нежный пирог с яблоками", "price": 2500, "category": "pie", "image": "https://avatars.mds.yandex.net/i?id=60f1286fe9e5cfd82ab596c693448c2b_l-8710170-images-thumbs&n=13"},
        {"id": 3, "name": "Булочка с корицей", "description": "Ароматная булочка", "price": 400, "category": "bun", "image": "https://img.freepik.com/free-photo/close-up-cinnamon-rolls-plate_23-2148604548.jpg?semt=ais_hybrid&w=740"},
        {"id": 4, "name": "Шоколадный круассан", "description": "Круассан с шоколадной начинкой", "price": 600, "category": "pastry", "image": "https://zima94.ru/upload/iblock/2bd/01r5ux5l56ywtu5gws3vyvz7wsjxmsjd.jpg"},
        {"id": 5, "name": "Яблочный тарт", "description": "Мини-тарт с яблоками и корицей", "price": 2800, "category": "pie", "image": "https://i.ytimg.com/vi/-IE-8KOT70k/maxresdefault.jpg"},
        {"id": 6, "name": "Булочка с маком", "description": "Булочка с маковой начинкой", "price": 400, "category": "bun", "image": "https://i.ytimg.com/vi/2Uk-LGF-r7E/maxresdefault.jpg"},
        {"id": 7, "name": "Слойка с ягодами", "description": "Слойка с черникой и клубникой", "price": 700, "category": "pastry", "image": "https://media.ovkuse.ru/images/recipes/46446eda-4728-4f0a-9d0e-194d39b26141/46446eda-4728-4f0a-9d0e-194d39b26141_1200_630.webp"},
        {"id": 8, "name": "Пирожок с мясом", "description": "Нежный пирожок с мясной начинкой", "price": 1000, "category": "pie", "image": "https://dostavkaedyokolica.ru/upload/iblock/f0f/qimz00j3z8xyl8svfeso1gizv3g985mb.jpg"},
        {"id": 9, "name": "Булочка с шоколадом", "description": "Булочка с кусочками шоколада", "price": 400, "category": "bun", "image": "https://aidigo-shop.ru/upload/iblock/cff/cffd36d32d375cdc34038a85ffcce8fb.jpg"},
        {"id": 10, "name": "Эклер с кремом", "description": "Лёгкий эклер с ванильным кремом", "price": 700, "category": "pastry", "image": "https://i.ytimg.com/vi/B4LHSchJGLY/maxresdefault.jpg"},
        {"id": 11, "name": "Карамельный эклер", "description": "Эклер с карамельным кремом сверху", "price": 750, "category": "pastry", "image": "https://i.pinimg.com/736x/4a/3f/93/4a3f934d3012ae17be4cea7f3fe1a489.jpg"},
        {"id": 12, "name": "Пирожок с вишней", "description": "Нежный пирожок с кислой вишнёвой начинкой", "price": 400, "category": "pie", "image": "https://i.pinimg.com/originals/20/57/76/205776b971a4bbfbefe81b4260a82ddd.jpg"}
    ]
    for prod in products:
        Product.objects.update_or_create(id=prod["id"], defaults=prod)

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_remove_order_title_order_total_and_more'),  # предыдущая миграция
    ]

    operations = [
        migrations.RunPython(add_products),
    ]
