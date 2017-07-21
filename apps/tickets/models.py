from django.db import models
from django.contrib.auth.models import User

# status list of tickets
STATUS = (('O', 'Open'), ('IP', 'In progress'), ('C', 'Close'))


class Ticket(models.Model):
    """ Model for Ticket
    """
    description = models.CharField(max_length=140)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])
    agent = models.ForeignKey(User, null=True, blank=True)
    close_date = models.DateField(verbose_name='Close Date', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_by', null=True, blank=True)
    response = models.TextField(max_length=254, null=True, blank=True)

    def __str__(self):
        return u'Description:{0} - Status:{1}'.format(self.description, self.get_status_display())
