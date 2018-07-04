from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name="is_following", blank=True)
    # following = models.ManyToManyField(User, related_name="following", blank=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def post_save_user_reciever(sender, instance, created, *args, **kwargs):
        if created:
            profile, is_created = Profile.objects.get_or_create(user=instance)
            # default_profile = Profile.objects.get_or_create(user__id=1)[0]
            # default_profile.followers.add(instance)
            # profile.followers.add(default_profile.user)
            profile.followers.add(profile.user)

            
    post_save.connect(post_save_user_reciever, sender=User)

