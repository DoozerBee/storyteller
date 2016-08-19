# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 00:57
from __future__ import unicode_literals

import athanor.core.models
from django.db import migrations, models
import django.db.models.deletion
import storyteller.abstract.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abstract', '0001_initial'),
        ('objects', '0005_auto_20150403_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('category', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('list_order', models.PositiveIntegerField(db_index=True, default=0)),
                ('custom', models.BooleanField(default=False)),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kind_children', to='exalted3.Merit')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='exalted3.Merit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('category1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personas_1', to='exalted3.Category')),
                ('category2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personas_2', to='exalted3.Category')),
                ('category3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personas_3', to='exalted3.Category')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='objects.ObjectDB')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonaCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('value', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonaMerit',
            fields=[
                ('abstractpersonamerit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstract.AbstractPersonaMerit')),
                ('merit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_merits', to='exalted3.Merit')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merits', to='exalted3.Persona')),
            ],
            bases=('abstract.abstractpersonamerit',),
        ),
        migrations.CreateModel(
            name='PersonaPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pools', to='exalted3.Persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonaStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(db_index=True, default=0)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='exalted3.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaTraitValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='exalted3.Persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SheetColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('title', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('border', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('textfield', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('texthead', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('colon', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('section_name', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('triple_column_name', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('advantage_name', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('advantage_border', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('slash', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('statdot', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('statfill', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('statname', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('damagename', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('damagetotal', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
                ('damagetotalnum', models.CharField(default=b'n', max_length=20, validators=[athanor.core.models.validate_color])),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('start_rating', models.PositiveSmallIntegerField(db_index=True, default=0, null=True)),
                ('list_order', models.PositiveIntegerField(db_index=True, default=0)),
                ('custom', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255, unique=True)),
                ('default_template', models.BooleanField(default=False)),
                ('category1_name', models.CharField(default=b'Category1', max_length=255)),
                ('category2_name', models.CharField(default=b'Category2', max_length=255)),
                ('category3_name', models.CharField(default=b'Category3', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', storyteller.abstract.models.CapitalCharField(db_index=True, max_length=255)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trait_choices', to='exalted3.Template')),
            ],
        ),
        migrations.CreateModel(
            name='TraitValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255)),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='exalted3.Trait')),
            ],
        ),
        migrations.AddField(
            model_name='stat',
            name='features',
            field=models.ManyToManyField(related_name='stats', to='exalted3.StatTag'),
        ),
        migrations.AddField(
            model_name='stat',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kind_children', to='exalted3.Stat'),
        ),
        migrations.AddField(
            model_name='stat',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='exalted3.Stat'),
        ),
        migrations.AddField(
            model_name='sheetcolor',
            name='template',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sheet_colors', to='exalted3.Template'),
        ),
        migrations.AddField(
            model_name='personatraitvalue',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='exalted3.TraitValue'),
        ),
        migrations.AddField(
            model_name='personastat',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_stats', to='exalted3.Stat'),
        ),
        migrations.AddField(
            model_name='personastat',
            name='tags',
            field=models.ManyToManyField(related_name='persona_stats', to='exalted3.StatTag'),
        ),
        migrations.AddField(
            model_name='personapool',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_pools', to='exalted3.Pool'),
        ),
        migrations.AddField(
            model_name='personacommit',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commitments', to='exalted3.PersonaPool'),
        ),
        migrations.AddField(
            model_name='persona',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='exalted3.Template'),
        ),
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='exalted3.Template'),
        ),
        migrations.AlterUniqueTogether(
            name='traitvalue',
            unique_together=set([('trait', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='trait',
            unique_together=set([('template', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='stat',
            unique_together=set([('key', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='sheetcolor',
            unique_together=set([('template', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='personastat',
            unique_together=set([('persona', 'stat')]),
        ),
        migrations.AlterUniqueTogether(
            name='personamerit',
            unique_together=set([('persona', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together=set([('key', 'character')]),
        ),
        migrations.AlterUniqueTogether(
            name='merit',
            unique_together=set([('key', 'parent')]),
        ),
    ]
