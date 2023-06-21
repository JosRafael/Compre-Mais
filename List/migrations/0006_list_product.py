

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0005_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('importance', models.IntegerField()),
                ('list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='List.list')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prod', to='List.product')),
                ('product_second_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondOption', to='List.product')),
            ],
        ),
    ]
