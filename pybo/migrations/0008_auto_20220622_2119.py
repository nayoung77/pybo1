# Generated by Django 3.1.3 on 2022-06-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_auto_20220622_2028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='question',
            name='post_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
