from django.shortcuts import render
from django.utils import timezone

from .models import Comment
from .forms import Form


def index(request):

    if request.method == 'POST':
        info = request.POST

        comment = Comment(
            text = info['text'],
            ip_address = get_client_ip(request),
            pub_date = timezone.now())

        comment.save()
    form = Form()
    commentsList = Comment.objects.order_by('-pub_date')
    context = {'commentsList': commentsList, 'form': form}
    return render(request, 'comments/index.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip