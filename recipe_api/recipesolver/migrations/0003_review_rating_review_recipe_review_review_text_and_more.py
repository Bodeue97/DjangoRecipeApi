# Generated by Django 4.2.6 on 2023-12-04 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipesolver', '0002_remove_review_rating_remove_review_recipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='recipesolver.recipe'),
        ),
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='recipes', to='recipesolver.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty_level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='recipes', to='recipesolver.difficultylevel'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='recipesolver.ingredient'),
        ),
    ]
