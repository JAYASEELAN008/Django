
from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect , render
from django.http import JsonResponse
from django.contrib import messages

# Home page
def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'home.html', context)

# Category-wise product list
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category.html', context)

# Product details page
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,  # Pass the product object
        'range': range(5),   # Pass a range of 5 for the stars
    }

    return render(request, 'product.html', context)


# search bar


def search_products(request):
    query = request.GET.get('query', '')  # Get the search term from the form
    products = Product.objects.filter(name__icontains=query) if query else []  # Search products
    return render(request, 'result.html', {'products': products, 'query': query})


# carsoule
def carsoule_products(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'home.html', {'products': products})


def offers(request):
    # Example context with sample offers
    context = {
        'offers': [
            {'name': 'Buy One Get One Free', 'details': 'Applicable on select categories.'},
            {'name': '20% Off on First Order', 'details': 'Use code FIRST20 at checkout.'},
        ]
    }
    return render(request, 'offers.html', context)


#cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})

    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image': product.image.url, 
        }

    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to the cart.')

    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    

    
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart.")
    
    return redirect('view_cart')



#ratings
def rate_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        rating = float(request.POST.get('rating'))  # Rating value sent from the client
        
        # Update the product's ratings (You can add more complex logic like averaging ratings)
        product.ratings = rating
        product.save()

        return JsonResponse({'message': 'Rating updated successfully!', 'new_rating': rating})

    return JsonResponse({'message': 'Invalid request'}, status=400)


