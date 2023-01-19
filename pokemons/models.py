from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=50) #포켓몬 이름
    nature = models.CharField(max_length=50) #포켓몬 성격
    ability = models.CharField(max_length=50) #포켓몬 특성
    teratype = models.CharField(max_length=50) #포켓몬 테라스탈 타입
    stats = models.TextField() #노력치
    skills = models.TextField() #기술배치
    item = models.CharField(max_length=50) #포켓몬 아이템
    description = models.TextField(null=True) #조정 의미
