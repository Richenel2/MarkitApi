# Generated by Django 3.2.5 on 2021-07-15 06:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('prix', models.IntegerField()),
                ('ville', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
                ('image', models.ImageField(upload_to='ProduitImage/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeFaireLivrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.livraison')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.produit')),
            ],
        ),
        migrations.AddField(
            model_name='livraison',
            name='produits',
            field=models.ManyToManyField(through='api.SeFaireLivrer', to='api.Produit'),
        ),
        migrations.AddField(
            model_name='livraison',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.user'),
        ),
    ]
