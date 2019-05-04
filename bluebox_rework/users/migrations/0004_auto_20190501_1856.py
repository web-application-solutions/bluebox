# Generated by Django 2.2 on 2019-05-01 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190501_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNum', models.IntegerField(null=True, verbose_name='Card Number')),
                ('expirationDate', models.DateField(verbose_name='Expiration Date')),
                ('ccvNum', models.IntegerField(verbose_name='CCV Num')),
            ],
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='purchase_date',
            new_name='purchaseDate',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='CCVNumber',
        ),
        migrations.RemoveField(
            model_name='users',
            name='CCVNumber',
        ),
        migrations.RemoveField(
            model_name='users',
            name='expirationDate',
        ),
        migrations.AddField(
            model_name='transaction',
            name='cardNum',
            field=models.IntegerField(null=True, verbose_name='Card Number'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionID',
            field=models.IntegerField(null=True, verbose_name='Transaction ID'),
        ),
        migrations.AddField(
            model_name='users',
            name='transactionID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Transaction', verbose_name='Transaction ID'),
        ),
        migrations.AddField(
            model_name='users',
            name='cardNum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Card', verbose_name='Card Number'),
        ),
    ]
