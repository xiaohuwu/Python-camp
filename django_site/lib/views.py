import json
from audioop import reverse
from builtins import isinstance, bytes, type
from locale import str

from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict

from .models import Book


# import the logging library
import logging

# Get an instance of a logger
mylog = logging.getLogger("django.server")

def index(request):
    return ""



class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()
    #重定向
    return HttpResponseRedirect(reverse('lib:detail'))  #redirect('/lib/detail/')


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    mylog.info("Test!!")
    context = {'book_list': book_list}
    return render(request, 'lib/detail.html', context)

def deleteBook(request, book_id):
    Book.objects.filter(id=book_id).delete()
    return HttpResponseRedirect(reverse('lib:detail'))



