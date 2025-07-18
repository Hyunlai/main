from django.shortcuts import render, redirect
from .models import UserFile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

@login_required
def dashboard(request):
    files = UserFile.objects.filter(user=request.user)
    return render(request, 'files/dashboard.html', {'files': files})

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        user_file = UserFile.objects.create(user=request.user, file=uploaded_file)
        return redirect('dashboard')
    return render(request, 'files/upload.html')

@login_required
def delete_file(request, file_id):
    file = UserFile.objects.get(id=file_id, user=request.user)
    file.delete()
    return redirect('dashboard')
