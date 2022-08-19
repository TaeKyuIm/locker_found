from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Locker(models.Model):
    location = models.CharField(max_length=50)
    start_time = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)], default=9) # 락커 오픈시간
    end_time = models.SmallIntegerField(validators=[MinValueValidator(12), MaxValueValidator(24)], default=22) # 락커 끝내는 시간
    # """
    # MinValueValidator, MaxValidator를 활용하는 경우 IntegerField에서 최대, 최소값을 지정해줄 수 있습니다.
    # 만약 조건에 맞지 않는 값이 올경우 ValidationError를 출력합니다.
    # """
    small_price = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)], default=2000, help_text='무인 사물함의 기본가격을 적어주세요!')
    mid_price = models.SmallIntegerField(blank=True, null=True) # 소형 가격
    big_price = models.SmallIntegerField(blank=True, null=True) # 중형 가격
    image = models.ImageField(upload_to='lockers/', default='default.png') # 대형 가격
    latitude = models.DecimalField(max_digits=8, decimal_places=6) # 지도에서 y 좌표
    longitude = models.DecimalField(max_digits=9, decimal_places=6) # 지도에서 x 좌표
    """
    카카오 maps에서 마킹을 찍으면 (latitude, longitude) 형태로 나옴.
    33.450701, 126.570667 각각 8, 9 자리이고, 소수점 자리는 6자리로 고정.
    """

    def __str__(self):
        return self.location
    
    
class MeMo(models.Model):
    locker = models.ForeignKey(Locker, related_name="locker", on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField(blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    usage_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.locker
