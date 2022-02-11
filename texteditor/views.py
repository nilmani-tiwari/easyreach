from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Editor
from .forms import EditorForm
def TextHtml(request):
    form=EditorForm()
    return render(request,'texteditor/index.html',{'form':form})
