from django.db import models
from django.db.models.signals import post_init

class Player(models.Model):
    sunetid = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    target = models.OneToOneField('self', null=True, blank=True)
    assign_time = models.DateTimeField(null=True, blank=True)
    living = models.BooleanField(default=True)

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def kill_target(self):
        victim = self.target
        self.target = victim.target
        victim.die()
        self.save()

    def die(self):
        self.target = None
        self.living = False
        self.save()


# Initialize living field to True for Players
#def setPlayerLiving(**kwargs):
#    player = kwargs.get('instance')
#    player.living = True;
#
#post_init.connect(setPlayerLiving, Player)
