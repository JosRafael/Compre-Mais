

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0008_productrecipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]
