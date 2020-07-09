from django.shortcuts import render

from .models import Platform


def show_platform(request, slug):
    platform = Platform.objects.get(slug=slug)
    main_page = platform.pages.filter(main=True).first()
    context = {'page': main_page}
    return render(request, 'platforms/show.html', context)
