from django.db import models
from django.conf import settings
from django.utils import timezone
from phone_field import PhoneField
from jumin.fields import JuminField

class Survey(models.Model):
    STATEMENT = [
        ('피의자','피의자'),
        ('피해자','피해자'),
        ('목격자','목격자'),
        ('참고인','참고인')
    ]
    #사건명
    case_name = models.CharField(max_length=200)
    #조서관 이름
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #조서작성자 이름
    name = models.CharField(max_length=100)
    #조서 생성 날짜
    created_date = models.DateTimeField(default=timezone.now)
    #생년 월일
    date_of_birth = models.DateField(null=False, blank=False)
    #주민등록번호
    registration_number = JuminField()
    #본적
    address = models.CharField(max_length=100)
    #직업
    job = models.CharField(max_length=100)
    #자택 전화
    home_phone_number =PhoneField(blank=True, help_text='자택 전화')
    #직장 전화
    job_phone_number = PhoneField(blank=True, help_text='직장 전화')
    #피의자
    suspect_name = models.CharField(max_length=100)
    #피의자에 대한 신분
    statement = year_in_school = models.CharField(
        max_length=3,
        choices=STATEMENT,
        default='목격자',
    )
    #조서내용
    survey = models.TextField()



    def __str__(self):
        return self.case_name