import foursquare
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Place
from project import settings


class HomepageView(TemplateView):
    template_name = "portal/index.html"


class PlaceListView(ListView):
    model = Place
    template_name = "portal/listagem.html"


def fq_login(request):
    client = _create_fq_client()
    auth_uri = client.oauth.auth_url()
    return redirect(auth_uri)


def fq_auth(request):
    client = _create_fq_client()
    code = request.GET.get('code')
    access_token = client.oauth.get_token(code)
    client.set_access_token(access_token)

    # Get the user's data
    user = client.users()
    return redirect("/listagem/")


def _create_fq_client():
    return foursquare.Foursquare(
        client_id=settings.FOURSQUARE_CLIENTID,
        client_secret=settings.FOURSQUARE_SECRET,
        redirect_uri=settings.FOURSQUARE_REDIRECTURI)
