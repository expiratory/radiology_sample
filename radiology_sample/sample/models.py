from django.db import models


class Sample(models.Model):
    MODALITY_CHOICES = (
        ("RG", "Рентген"),
        ("CT", "КТ"),
        ("MRI", "МРТ"),
    )

    REGION_OF_INTEREST_CHOICES = (
        ("HEAD", "Голова"),
        ("NECK", "Шея"),
        ("THORAX", "Грудная клетка"),
        ("ABDOMEN", "Брюшная полость"),
        ("LIMBS", "Конечности"),
    )

    SPECIALIZATION_CHOICES = (
        ("TRAUMA", "Травматология"),
        ("PHYSICIAN", "Терапия/педиатрия"),
        ("OTOLARYNGOLOGY", "Оториноларингология"),
        ("NEUROLOGY", "Неврология"),
        ("ONCOLOGY", "Онкология"),
    )

    title = models.CharField(max_length=256, verbose_name='Заголовок описания',
                             blank=False, null=False)
    text = models.TextField(verbose_name='Текст описания', blank=False, null=False)
    datetime_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    datetime_of_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    modality = models.CharField(verbose_name='Модальность исследования', max_length=50, choices=MODALITY_CHOICES,
                                default="", blank=False, null=False)
    region_of_interest = models.CharField(verbose_name='Зона исследования', max_length=50,
                                          choices=REGION_OF_INTEREST_CHOICES, default="", blank=False, null=False)
    specialization = models.CharField(verbose_name='Специализация', max_length=50, choices=SPECIALIZATION_CHOICES,
                                      default="", blank=False, null=False)
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    additional_image = models.ImageField(blank=True, null=True, verbose_name='Дополнительное изображение')
