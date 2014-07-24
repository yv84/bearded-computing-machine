from django.views import generic

from . import models


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class CardListView(generic.ListView):
    model = models.Card

    def get_queryset(self):
        queryset = super(CardListView, self).get_queryset()
        return queryset


class CardDetailView(generic.DetailView):
    model = models.Card

    # def get_queryset(self):
    #     queryset = super(CardDetailView, self).get_context_data(**kwargs)
    #     queryset = queryset.all()[0]
    #     return queryset
