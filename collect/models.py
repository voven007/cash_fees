from django.db import models

from users.models import User


class Event(models.Model):
    title = models.CharField(verbose_name='Событие', max_length=256)

    class Meta:
        verbose_name = 'Название события'
        verbose_name_plural = 'Названия событий'

    def __str__(self):
        return f'{self.title}'


class Collect(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название')
    event = models.ManyToManyField('Event', verbose_name='Событие')
    text = models.TextField(verbose_name='Описание сбора')
    target_amount = models.DecimalField(
        verbose_name='Сумма сбора', max_digits=10, decimal_places=2)
    cover = models.ImageField(
        verbose_name='Обложка сбора',
        upload_to='image/',
        null=True,
        blank=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания сбора', auto_now_add=True)
    end_time = models.DateTimeField(verbose_name='Дата завершения сбора')

    class Meta:
        verbose_name = 'Сбор'
        verbose_name_plural = 'Сборы'
        default_related_name = 'collects'

    def __str__(self):
        return f'{self.pk}'


class Payment(models.Model):
    collect = models.ForeignKey(
        Collect, verbose_name='Сбор', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    amount = models.DecimalField(
        verbose_name='Сумма', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(
        verbose_name='Время совершения платежа', auto_now_add=True)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        default_related_name = 'payments'

    def __str__(self):
        return f'{self.amount}'
