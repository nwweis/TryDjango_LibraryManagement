from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
def book_list_view(request):
    queryset = Book.objects.all()
    context = {
        'object_list': queryset
        }

    return render(request, "books_list.html", context)


def book_create_view(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = BookForm()

    context = {
        'form': form
        }

    return render(request, 'books_create.html', context)


def book_update_view(request, id=id):
    obj = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request, 'books_update.html', context)


def book_detail_view(request, id=id):
    obj = get_object_or_404(Book, id=id)
    
    context = {
        'obj':obj
    }

    return render(request, 'books_detail.html', context)


def book_detail_view(request, id=id):
    obj = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../')

    context = {
        'obj': obj
    }

    return render(request, 'books_delete.html', context)