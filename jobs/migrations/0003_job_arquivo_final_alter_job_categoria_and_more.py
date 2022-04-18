# Generated by Django 4.0.3 on 2022-04-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_jobs_job_rename_referencias_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='arquivo_final',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='categoria',
            field=models.CharField(choices=[('D', 'Design'), ('EV', 'Edição de Vídeo')], max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
