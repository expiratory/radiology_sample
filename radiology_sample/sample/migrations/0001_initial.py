# Generated by Django 4.2.3 on 2023-10-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок описания')),
                ('text', models.TextField(verbose_name='Текст описания')),
                ('datetime_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('datetime_of_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('modality', models.CharField(choices=[('RG', 'Рентген'), ('CT', 'КТ'), ('MRI', 'МРТ')], default='', max_length=50, verbose_name='Модальность исследования')),
                ('region_of_interest', models.CharField(choices=[('HEAD', 'Голова'), ('NECK', 'Шея'), ('THORAX', 'Грудная клетка'), ('ABDOMEN', 'Брюшная полость'), ('LIMBS', 'Конечности')], default='', max_length=50, verbose_name='Зона исследования')),
                ('specialization', models.CharField(choices=[('TRAUMA', 'Травматология'), ('PHYSICIAN', 'Терапия/педиатрия'), ('OTOLARYNGOLOGY', 'Оториноларингология'), ('NEUROLOGY', 'Неврология'), ('ONCOLOGY', 'Онкология')], default='', max_length=50, verbose_name='Специализация')),
            ],
        ),
    ]
