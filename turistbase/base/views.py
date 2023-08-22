from django.shortcuts import render, redirect
from .form import BookingForm


def index(request):
    form = BookingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # ... другие действия после сохранения ...чуть позже мы из дополним
            return redirect('success_page')  # перенаправить на страницу благодарности
    return render(request, 'base/index.html', {'form': form})

def about(request):
    return render(request,"base/about-us.html")



