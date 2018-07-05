from django.db import models
from django.conf import settings
from .utils import code_generator
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name="is_following", blank=True)
    # following = models.ManyToManyField(User, related_name="following", blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            subject = 'Activation Key'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'This is my test message {}'.format(self.activation_key)
            recipient_list = [self.user.email]
            html_message = '<h1>This is my HTML test {} </h1>'.format(self.activation_key)
            # sent_mail = send_mail( subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message )
            sent_mail = False
            return sent_mail            


    def post_save_user_reciever(sender, instance, created, *args, **kwargs):
        if created:
            profile, is_created = Profile.objects.get_or_create(user=instance)
            # default_profile = Profile.objects.get_or_create(user__id=1)[0]
            # default_profile.followers.add(instance)
            # profile.followers.add(default_profile.user)
            profile.followers.add(profile.user)

            
    post_save.connect(post_save_user_reciever, sender=User)

