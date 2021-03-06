# Generated by Django 2.1.5 on 2019-03-12 09:42

import django.db.models.deletion
import jsonfallback.fields
from django.db import migrations, models

import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0112_auto_20190304_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dependency_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependent_questions', to='pretixbase.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='dependency_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
