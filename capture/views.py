from django.shortcuts import render,redirect
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# Create your views here.

def first_view(request):
    return render(request, 'capture/first_view.html', {})

def simple_upload(request):
    if request.method == 'POST':
        # print(request.POST) : <QueryDict: {'csrfmiddlewaretoken': [‘~~~’], 'title': ['upload_1']}>
        # print(request.FILES) : <MultiValueDict: {'image': [<InMemoryUploadedFile: ses.jpg (image/jpeg)>]}>
        form = SimpleUploadForm(request.POST, request.FILES) 

        if form.is_valid():
            myfile = request.FILES['image'] # 'myself.png'
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename) # '/media/myself.png'

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'capture/simple_upload.html', context)

    else: # request.method == 'GET'
        form = SimpleUploadForm()
        context = {'form': form} # empty form
        return render(request, 'capture/simple_upload.html', context)


def detect_face(request):
    if request.method == 'POST' :
        form = ImageUploadForm(request.POST, request.FILES) # filled form
        if form.is_valid():
            post = form.save(commit=False) 
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'capture/detect_face.html', {'form':form, 'post':post})

    else:
         form = ImageUploadForm() # empty form
         return render(request, 'capture/detect_face.html', {'form':form})
