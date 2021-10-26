# -*- coding: utf-8 -*-
from django.db import models, migrations
import wagtail.contrib.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendition',
            name='file',
            field=models.ImageField(upload_to=wagtail.contrib.images.models.get_rendition_upload_to, width_field='width', height_field='height'),
        ),
    ]