from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import CustomUser, Item, Cart#, Address
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'user':request.user}
    return render(request, 'index.html', context)


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return HttpResponse('ユーザーの作成に成功しました')

def signin(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')
    
    if user.password == password:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('ログインに失敗しました')
    
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def item(request):
    items = Item.objects.all()
    item_search = Item.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        """ テキスト用のQオブジェクトを追加 """
        item_search = item_search.filter(
                 Q(title__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    context = {'items':items,
               "item_search":item_search
               }
    template = loader.get_template("app/item.html")
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    details = item.text_set.all()
    context = {
        'item' : item,
        'details' : details,
    }
    template = loader.get_template('app/detail.html')
    return HttpResponse(template.render(context, request))

@login_required
def cart(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            Cart.objects.create(user=request.user, item=item, quantity=quantity)
            messages.success(request, f"You have added {quantity} {item.title}(s) to your history.")
            return redirect('address')
        else:
            messages.error(request, "Please specify a positive integer for quantity.")
    return render(request, 'app/cart.html', {'item': item})

@login_required
def history(request):
    history = Cart.objects.filter(user=request.user)
    context = {'history': history}
    return render(request, 'app/history.html', context)

def payment(request):
    return render(request, 'app/payment.html')

def address(request):
    return render(request, 'app/address.html')

"""
def addresses(request):
    if request.method == 'POST':
        name = str(request.POST.get('name'))
        code = str(request.POST.get('code'))
        address = str(request.POST.get('address'))
        Address.objects.create(name=name, code=code, address=address)
        return redirect('payment')
    return render(request, 'app/address.html')
"""

def end(request):
    return render(request, 'app/end.html')
