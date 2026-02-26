from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Article, ActivityLog

@receiver(post_save, sender=Article)
def log_acticle_created(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
            content_object=instance,
            action='Article created'
        )
        print(f'[Signal] Logged creation of: {instance.title}')

@receiver(m2m_changed, sender=Article.tags.through)
def log_tags_changes(sender, instance, action, **kwargs):
    if action == 'post_add':
        ActivityLog.objects.create(
            content_object = instance,
            action = 'Tags updated'
        )
        print(f'[Signal] Tags changed on: {instance.title}')