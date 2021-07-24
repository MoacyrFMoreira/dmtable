from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required

@login_required()
def custom_login(request):
    return HttpResponseRedirect(reverse("gametable:table"))