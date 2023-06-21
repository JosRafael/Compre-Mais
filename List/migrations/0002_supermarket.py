

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
