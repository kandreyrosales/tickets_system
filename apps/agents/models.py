from django.db import models


class Agent(models.Model):
    """ Model for Agent
    """
    username = models.CharField(max_length=12, primary_key=True, default="")
    full_name = models.CharField(max_length=140, blank=True, null=True)
    email = models.CharField(max_length=140, blank=True)
    password = models.CharField(max_length=100, blank=True)
    tickets = models.ManyToManyField('tickets.Ticket', related_name='agents', blank=True)

    def __str__(self):
        if self.full_name:
            return u'{0}'.format(self.full_name)
        else:
            return 'Unassigned'