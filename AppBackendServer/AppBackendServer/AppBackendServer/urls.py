
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from AppBackEndApi import views
from rest_framework.authtoken import views as authviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^promotionlist/(?P<token>\w{0,50})/$',views.PromotionList.as_view()),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)