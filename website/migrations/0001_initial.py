from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('company_size', models.CharField(
                    blank=True,
                    choices=[
                        ('1-50', '1-50 employees'),
                        ('51-200', '51-200 employees'),
                        ('201-1000', '201-1000 employees'),
                        ('1000+', '1000+ employees'),
                    ],
                    max_length=20,
                )),
                ('interest', models.CharField(blank=True, max_length=150)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
