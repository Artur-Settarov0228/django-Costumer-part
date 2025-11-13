from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product


def viewList(request:HttpRequest)->HttpResponse:
    if request.method == "POST":
        ratings = Product(
            rating = request.POST.get("rating")
        )
        ratings.save()
        return HttpResponse("ovozingiz qabul qilindi")
    return render(request=request, template_name="list_view.html")
