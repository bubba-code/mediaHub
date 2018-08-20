from hub.models import Movie
from django.http import HttpResponse
from django.template import loader


def index(request):
    movie_list = Movie.objects.order_by('-movieRelYear')
    template = loader.get_template('hub/index.html')
    context = {
        'movie_list': movie_list,
    }
    return HttpResponse(template.render(context, request))