# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-04 13:12
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, shema_editor):
    Recipient = apps.get_model('mailtrigger','Recipient')

    irsg = Recipient.objects.create(
        slug = 'irsg',
        desc = 'The IRSG',
        template = 'The IRSG <irsg@irtf.org>'
    )

    MailTrigger = apps.get_model('mailtrigger', 'MailTrigger')
    slug = 'irsg_ballot_saved'
    desc = 'Recipients when a new IRSG ballot position with comments is saved'
    irsg_ballot_saved = MailTrigger.objects.create(
        slug=slug,
        desc=desc
    )
    irsg_ballot_saved.to.add(irsg)
    irsg_ballot_saved.cc.set(Recipient.objects.filter(slug__in=['doc_affecteddoc_authors','doc_affecteddoc_group_chairs','doc_affecteddoc_notify','doc_authors','doc_group_chairs','doc_group_mail_list','doc_notify','doc_shepherd']))

    # We cannot just change the slug of the existing ballot_saved table,
    # because that will loose all the m2m entries in .to and .cc
    ballot_saved = MailTrigger.objects.get(slug='ballot_saved')
    iesg_ballot_saved = MailTrigger.objects.create(slug='iesg_ballot_saved')
    iesg_ballot_saved.to.set(ballot_saved.to.all())
    iesg_ballot_saved.cc.set(ballot_saved.cc.all())
    iesg_ballot_saved.desc = ballot_saved.desc
    iesg_ballot_saved.save()

def reverse(apps, shema_editor):
    MailTrigger = apps.get_model('mailtrigger', 'MailTrigger')
    MailTrigger.objects.filter(slug='irsg_ballot_saved').delete()
    MailTrigger.objects.filter(slug='iesg_ballot_saved').delete()
    # 
    Recipient = apps.get_model('mailtrigger','Recipient')
    Recipient.objects.filter(slug='irsg').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('mailtrigger', '0012_dont_last_call_early_reviews'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]