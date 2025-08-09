from django.shortcuts import redirect, render

from .forms import NewsForm


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_list")
    else:
        form = NewsForm()
    return render(request, "news/add_news.html", {"form": form})
