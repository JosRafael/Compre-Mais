

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0006_list_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagRecipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('tagCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='List.tagrecipt')),
            ],
        ),
    ]
