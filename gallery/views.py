from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from gallery.models import Image

def gallery_view(request):
    today = date.today()
    last_month_start = date(today.year, today.month - 1, 1)
    last_month_end = date(today.year, today.month, 1) - timedelta(days=1)

    images = Image.objects.filter(created_date__range=(last_month_start, last_month_end))

    context = {"images": images}
    return render(request, 'gallery.html', context)

def image_detail(request, id_img):
    photo = get_object_or_404(Image, id=id_img)
    context = {'photo': photo}

    render(request, 'image_detail.html', context)