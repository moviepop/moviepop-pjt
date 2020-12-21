from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# Create your models here.
class User(AbstractUser):
    # preference = models.CharField(max_length=20)
    GENRES = (
        (12, '모험'),
        (14, '판타지'),
        (16, '애니메이션'),
        (18, '드라마'),
        (27, '공포'),
        (28, '액션'),
        (35, '코미디'),
        (36, '역사'),
        (37, '서부'),
        (53, '스릴러'),
        (80, '범죄'),
        (99, '다큐멘터리'),
        (878, 'SF'),
        (9648, '미스터리'),
        (10402, '음악'),
        (10749, '로맨스'),
        (10751, '가족'),
        (10752, '전쟁'),
        (10770, 'TV영화')
    )
    preference = MultiSelectField(choices = GENRES, verbose_name="선호하는 영화 장르")
    preference_code = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10, verbose_name="닉네임")


class Blog(models.Model):
    text = models.TextField()
