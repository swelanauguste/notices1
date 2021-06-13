from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.views.generic import ListView
from hitcount.views import HitCountDetailView
from .models import Publication


class PublicationDetail(HitCountDetailView):
    model = Publication
    queryset = Publication.published_objects.all()
    count_hit = True


class PublicationList(ListView):
    model = Publication
    queryset = Publication.published_objects.all()



