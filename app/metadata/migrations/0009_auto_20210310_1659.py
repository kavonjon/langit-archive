# Generated by Django 3.0.5 on 2021-03-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0008_auto_20210222_0047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollaboratorNames',
            new_name='CollaboratorName',
        ),
        migrations.AlterModelOptions(
            name='geographic',
            options={},
        ),
        migrations.RenameField(
            model_name='geographic',
            old_name='lad',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='columns_export',
            name='item_collectors_number',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='columns_export',
            name='item_document_geographic_lat_long',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='columns_export',
            name='item_geographic_lat_long',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='columns_export',
            name='item_publisher_address',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='publisher_address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
