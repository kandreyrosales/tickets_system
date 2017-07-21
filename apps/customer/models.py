from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class RegisterCustomer(CreateView):
    """ Model for Customer
    """
    model = User
    template_name = 'customer/register_customer.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('ticket:tickets_view')


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = (
#             ("Is_customer", "Customer"),
#             ("Is_agent", "Agent"),
#         )


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()