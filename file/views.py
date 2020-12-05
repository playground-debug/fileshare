from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import File
import os
from django.db.models import Count


def homepage(request):
    files = File.objects
    return render(request, 'files/home.html', {'files': files})


@login_required
def uploadfile(request):
    if request.method == 'GET':
        return render(request, 'files/uploadfile.html')
    else:
        document = File()
        file = request.FILES['document']
        filename = request.POST['filename']
        document.filename = filename
        document.file = file
        document.user = request.user
        name, extension = os.path.splitext(file.name)
        if len(filename) == 0:
            document.filename = name
        document.filetype = extension[1:]
        document.dateUploaded = timezone.datetime.now()
        document.save()
        return redirect('homepage')


def portal(request):
    context = {
        "total": File.objects.count(),

        "filetype": File.objects.values('filetype')
        .order_by('filetype')
        .annotate(count=Count('filetype')),

        "users": File.objects.values('user__username')
        .order_by('user__username')
        .annotate(count=Count('user__username'))
    }
    return render(request, 'files/portal.html', context)
