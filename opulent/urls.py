"""opulent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from operator import index
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Pages.views import aboutView, contactView, faqView, index0, index1, index2 , index3, index4, index5, index6, notFoundView, projectView, serviceView

from opulent import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index0, name='zero'),
    path('contact-us/', contactView, name='contact'),
    path('faq/', faqView, name='faq'),
    path('about-us/', aboutView, name='about'),
    path('service/<slug:url_title>', serviceView, name='service'),
    path('project/<slug:url_title>', projectView, name='project'),
    path('404/', notFoundView, name='404'),
    path('one/', index1, name='one'),
    path('two/', index2, name='two'),
    path('three/', index3, name='three'),
    path('four/', index4, name='four'),
    path('five/', index5, name='five'),
    path('six/', index6, name='six'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
