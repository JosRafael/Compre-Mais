

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0007_tagrecipt_recipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRecipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prod_in_recipe', to='List.product')),
                ('recipt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='List.recipt')),
            ],
        ),
    ]
