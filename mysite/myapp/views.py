from django.shortcuts import render

# Create your views here.
from django.core.cache import cache

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Role


def index(request):
    cache.set("foo", "value")

    role_list = Role.objects.order_by('-user_id')[:5]
    template = loader.get_template('myapp/index.html')
    context = RequestContext(request, {
        'role_list': role_list,
        'value': cache.get("foo")
    })
    return HttpResponse(template.render(context))

