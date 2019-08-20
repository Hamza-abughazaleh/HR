from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns

from main.api import views

snippet_list = views.CandidatesViewSet.as_view({
    'get': 'list',
})
snippet_detail = views.CandidatesViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    # urls for Django Rest Framework API

    url(r'^candidates/', csrf_exempt(views.CandidatesCreateAPIView.as_view()), name='candidates-registration'),
    url(r'^login/$', csrf_exempt(views.LoginView.as_view()), name='api-login'),
    url(r'^logout/$', csrf_exempt(views.LogoutView.as_view()), name='api-logout'),

]

urlpatterns += format_suffix_patterns([
    url(r'^candidates-list/', snippet_list, name='candidates-list'),
    url(r'^candidates-detail/(?P<pk>\d+)', snippet_detail, name='candidates-detail'),
])