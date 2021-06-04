from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View

from shorty.models import Url


class RedirectView(View):
    def get(self, request, short):
        try:
            url = Url.objects.get(short_id=short)
            url.counter += 1
            url.save()
            #url = get_object_or_404(Url, short_id=short)
        except Url.DoesNotExist:
            url = Url()
            url.long_url = 'https://gkiserpong.org'

        return redirect(url.long_url)