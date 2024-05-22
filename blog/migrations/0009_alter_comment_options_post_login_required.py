# Generated by Django 4.2 on 2024-05-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]
