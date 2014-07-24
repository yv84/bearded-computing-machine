from django.core.urlresolvers import reverse
from django.db import models


class Answer(models.Model):
    answer = models.CharField(max_length=10000)
    correctly = models.BooleanField(default=False)

    def __str__(self):
        return self.answer[:50]

    def get_absolute_url(self):
        return reverse('qat:answer:detail', kwargs={'pk': self.pk})


class Ask(models.Model):
    ask = models.CharField(max_length=10000)
    answer1 = models.OneToOneField(Answer, related_name='answer1')
    answer2 = models.OneToOneField(Answer, related_name='answer2')
    answer3 = models.OneToOneField(Answer, related_name='answer3')
    answer4 = models.OneToOneField(Answer, related_name='answer4')
    answer5 = models.OneToOneField(Answer, related_name='answer5')

    def __str__(self):
        return self.ask[:50]

    def get_absolute_url(self):
        return reverse('qat:ask:detail', kwargs={'pk': self.pk})


class Card(models.Model):
    nomer = models.IntegerField()
    ask1 = models.OneToOneField(Ask, related_name='ask1')
    ask2 = models.OneToOneField(Ask, related_name='ask2')
    ask3 = models.OneToOneField(Ask, related_name='ask3')
    ask4 = models.OneToOneField(Ask, related_name='ask4')
    ask5 = models.OneToOneField(Ask, related_name='ask5')
    ask6 = models.OneToOneField(Ask, related_name='ask6')
    ask7 = models.OneToOneField(Ask, related_name='ask7')
    ask8 = models.OneToOneField(Ask, related_name='ask8')
    ask9 = models.OneToOneField(Ask, related_name='ask9')

    def __str__(self):
        return "".join(["card ", str(self.nomer)])

    def get_absolute_url(self):
        return reverse('qat:card:detail', kwargs={'pk': self.pk})
