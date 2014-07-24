from django.views import generic
from django.core.urlresolvers import reverse_lazy

from . import models




class HomePageView(generic.RedirectView):
    url = reverse_lazy('qat:card:list')


class AnswerListView(generic.ListView):
    model = models.Answer


# class LogoutView(generic.RedirectView):
#     url = reverse_lazy('home')
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)



class AnswerDetailView(generic.DetailView):
    model = models.Answer

    def get_queryset(self):
        queryset = super(AnswerDetailView, self).get_queryset()
        # queryset = queryset | models.Ask.objects.filter(id=self.request.user)
        return queryset


class AskListView(generic.ListView):
    model = models.Ask


class AskDetailView(generic.DetailView):
    model = models.Ask


class CardListView(generic.ListView):
    model = models.Card


class CardDetailView(generic.DetailView):
    model = models.Card
