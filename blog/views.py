from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    items_per_page = request.GET.get('items_per_page', 5)  # Получаем количество элементов на странице (по умолчанию 5)
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'items_per_page': items_per_page})

