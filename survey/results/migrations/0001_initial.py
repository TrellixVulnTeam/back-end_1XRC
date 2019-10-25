# Generated by Django 2.2.6 on 2019-10-24 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('answers', '0001_initial'),
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('choices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='answers.Answer')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.Evaluation')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Questions')),
            ],
        ),
    ]