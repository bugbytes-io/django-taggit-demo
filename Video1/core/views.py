from django.shortcuts import render
from taggit.models import Tag
from core.models import Film

# Create your views here.
def index(request):
    films = Film.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()
    context = {'films': films, 'tags': tags}
    return render(request, 'core/index.html', context)