
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('promoTag', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='List.product')),
                ('supermarket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='List.supermarket')),
            ],
        ),
    ]
