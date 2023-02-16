from .models import Product


def special_product():
    try:
        product = Product.objects.get(is_featured=True, title="Get Hired")
        return product
    except:
        return None
