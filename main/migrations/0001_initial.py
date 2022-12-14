# Generated by Django 3.2.16 on 2022-12-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_local', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('uf', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=100)),
                ('num_residencial', models.IntegerField()),
                ('cep', models.CharField(max_length=30)),
                ('fone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=150)),
                ('nome_responsavel', models.CharField(max_length=150)),
                ('cpf_responsavel', models.CharField(max_length=150)),
                ('disponibilidade', models.TextField(max_length=800)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
