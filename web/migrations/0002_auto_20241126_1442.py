# Generated by Django 3.2.25 on 2024-11-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adobetemplate',
            name='Type',
            field=models.CharField(choices=[('Adobe Photoshop', 'Adobe Photoshop'), ('Adobe Primier Pro', 'Adobe Primier Pro'), ('Adobe Illustrator', 'Adobe Illustrator'), ('Adobe InDesign', 'Adobe InDesign'), ('Adobe XD', 'Adobe XD'), ('Adobe Lightroom', 'Adobe Lightroom'), ('Adobe Lightroom Classic', 'Adobe Lightroom Classic'), ('Adobe After Effects', 'Adobe After Effects'), ('Adobe Animate', 'Adobe Animate'), ('Adobe Dreamweaver', 'Adobe Dreamweaver'), ('Adobe Audition', 'Adobe Audition'), ('Adobe Bridge', 'Adobe Bridge'), ('Adobe Dimension', 'Adobe Dimension'), ('Adobe Fresco', 'Adobe Fresco'), ('Adobe Character Animator', 'Adobe Character Animator'), ('Adobe Media Encoder', 'Adobe Media Encoder'), ('Adobe Rush', 'Adobe Rush'), ('Adobe Spark', 'Adobe Spark'), ('Adobe Substance 3D Painter', 'Adobe Substance 3D Painter'), ('Adobe Substance 3D Designer', 'Adobe Substance 3D Designer'), ('Adobe Substance 3D Sampler', 'Adobe Substance 3D Sampler'), ('Adobe Substance 3D Stager', 'Adobe Substance 3D Stager'), ('Adobe Acrobat Pro DC', 'Adobe Acrobat Pro DC'), ('Adobe Sign', 'Adobe Sign'), ('Adobe FrameMaker', 'Adobe FrameMaker'), ('Marketo Engage', 'Marketo Engage'), ('Adobe Presenter', 'Adobe Presenter')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='desktoptemplate',
            name='Type',
            field=models.CharField(choices=[('Kivy', 'Kivy'), ('Pyqt', 'Pyqt'), ('Tkinter', 'Tkinter'), ('C++', 'C++'), ('C#', 'C#'), ('Java', 'Java'), ('Electron (JavaScript, HTML, CSS)', 'Electron (JavaScript, HTML, CSS)'), ('Swift', 'Swift'), ('Rust', 'Rust')], max_length=200, null=True),
        ),
    ]
