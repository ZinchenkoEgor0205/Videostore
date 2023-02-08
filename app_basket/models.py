# from django.contrib.auth.models import User
# from django.db import models
#
# from app_main.models import Videocard


# class Basket(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='basket')
#     videocard = models.ForeignKey(Videocard, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
#     add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)