from django.db.models import Sum, Count
from django.http import JsonResponse
from .models import Category

def get_top_categories(request):
    categories = (
        Category.objects.annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(total_price__isnull=False)
        .order_by('-total_price')
        .values('name', 'total_price', 'product_count')
    )
    return JsonResponse(list(categories[:5]), safe=False)
