from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.shortcuts import render
from .models import Video

# Create your views here.

video_template = 'media/video.html'
video_list_template = 'media/videos_list.html'


def videos_list(request):
    videos = Video.objects.all().order_by('-created')
    title = 'Video'
    context = {'videos': videos, 'title': title}
    return render(request, video_list_template, context)


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    context = {'video': video}
    return render(request, video_template, context)
