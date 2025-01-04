import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

from .permissions import is_user
from .forms import CategoryForm, BookForm
from ..general.models import BooksItems, Category
from cart.api.models import Cart, CartItem

# Block Categories

def categories_page(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
        
    return render(request, 'add_category.html', {'form': 'form'})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'edit_category.html', {'form': form, 'category': category})


# Block Items

def items_page(request, category_id=None):
    if categories_page:
        items = BooksItems.objects.filter(category_id=category_id).order_by('title')
    else:
        items = BooksItems.objects.all().order_by('title')
    return render(request, 'items.html', {'items': items, 'category_id': category_id})

def item_page(request, category_id, pk):
    category = Category.objects.get(id=category_id)
    book = BooksItems.objects.get(id=pk)

    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user_id=request.user.id).first()
    else:
        session_key = request.session.session_key
        user_cart = Cart.objects.filter(session_key=session_key).first()

    cart_item = None
    if user_cart:
        cart_item = user_cart.items.filter(product_id=book.id).first()

    return render(request, 'item.html', {
        'category': category,
        'book': book,
        'cart_item': cart_item,
    })

def edit_item(request, category_id, pk):
    item = get_object_or_404(BooksItems, id=pk)
    category = Category.objects.get(pk=category_id)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(f'/categories/{category_id}/items')

        else:
            print(form.errors)

    else:
        form = BookForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'category': category, 'category_id': category_id, 'item': item})

def add_item(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():

            item = form.save(commit=False)
            item.category = category
            item.save()
            return redirect(f'/categories/{category_id}/items') 
    else:
        form = BookForm()
    context = {
        'form': form,
        'category_name': category.title,
        'category_id': category_id,
    }
        
    return render(request, 'add_item.html', context)

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(BooksItems, pk=product_id)
        quantity = json.loads(request.body)['quantity']

        if request.user.is_authenticated:
            user_cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            user_cart, _ = Cart.objects.get_or_create(session_key=session_key)

        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            cart=user_cart,
            defaults={'quantity': quantity, 'price': product.price}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({'message': 'Товар успешно добавлен в корзину', 'quantity': cart_item.quantity}, status=201)
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)