"""todo URL Configuration

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
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", homepage, name='home'),
                  path('test', test, name='test'),
                  path('test2', test2, name='test2'),
                  path('toMeet', to_meet, name='toMeet'),
                  path('add-todo', add_todo, name='add-todo'),
                  path('meet_person', meet_person, name='meet_person'),
                  path('habits', habits, name='habits'),
                  path('add_habits', add_habits, name='add_habits'),
                  path('delete-todo/<id>', delete_todo, name='delete-todo'),
                  path('mark-todo/<id>', mark_todo, name='mark-todo'),
                  path('unmark-todo/<id>', unmark_todo, name='unmark-todo'),
                  path('delete-meet/<id>', delete_meet, name='delete-meet'),
                  path('mark-meet/<id>', mark_meet, name='mark-meet'),
                  path('unmark-meet/<id>', unmark_meet, name='unmark-meet'),
                  path('done-todo/<id>', done_todo, name='done-todo'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
