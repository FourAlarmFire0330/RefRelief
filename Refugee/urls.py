"""Refugee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from refrelief.views import render_html
from refrelief.views import school_list
from refrelief.views import scholarship_list
from refrelief.views import English_Course_list
from refrelief.views import events_list
from refrelief.views import community_class_list
from refrelief.views import specific_scholarship
from refrelief.views import Iraq_map
from refrelief.views import Syria_map
from refrelief.views import Burma_map
from refrelief.views import directions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', render_html),

    url(r'^refrelief/school_list', school_list),

    url(r'^refrelief/events_list', events_list),

    url(r'^refrelief/scholarship_list', scholarship_list),
    url(r'^refrelief/specific_scholarship', specific_scholarship),

    url(r'^refrelief/English_Course_list', English_Course_list),

    url(r'^refrelief/community_class_list', community_class_list),

    url(r'^refrelief/Iraq_map', Iraq_map),
    url(r'^refrelief/Syria_map', Syria_map),
    url(r'^refrelief/Burma_map', Burma_map),
    url(r'^refrelief/directions', directions),

    url(r'^i18n/', include('django.conf.urls.i18n')),
]