from .models import MyModel
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # Modify the instance within the signal handler
    instance.name = "Modified in signal"
    instance.save() 