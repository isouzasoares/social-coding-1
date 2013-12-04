import foursquare

from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from .models import Place, Consumer
from project import settings


class HomepageView(TemplateView):
    template_name = "portal/index.html"


class PlaceListView(ListView):
    model = Place
    template_name = "portal/listagem.html"

    # 4 estabelecimentos mais avaliados
    qs = Place.objects.annotate(num_ratings=Count('rating'))
    queryset = qs.order_by('-num_ratings')[:4]


class LikeView(ListView):
    model = Place
    template_name = "portal/curtir.html"

def fq_login(request):
    client = _create_fq_client()
    auth_uri = client.oauth.auth_url()
    return redirect(auth_uri)


def fq_auth(request):
    client = _create_fq_client()
    code = request.GET.get('code')
    access_token = client.oauth.get_token(code)
    client.set_access_token(access_token)

    # Get the foursquare's data
    user = client.users()
    consumer_id = user['user']['id']
    consumer_gender = user['user']['gender'][:1]
    
    # Consumer(foursquare_uid=consumer_id, sex=consumer_gender)
    return redirect('/listagem/')


def _create_fq_client():
    return foursquare.Foursquare(
        client_id=settings.FOURSQUARE_CLIENTID,
        client_secret=settings.FOURSQUARE_SECRET,
        redirect_uri=settings.FOURSQUARE_REDIRECTURI)
