from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("explore",views.explore,name="explore"),
    # path("<str:name>",views.greet,name="greet"),
    path("contact",views.contact,name="contact")
]
