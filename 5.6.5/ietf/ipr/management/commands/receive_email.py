import sys
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from ietf.utils.log import log
from ietf.ipr.email import create_response_email

import debug                            # pyflakes:ignore

class Command(BaseCommand):
    help = (u"Receive email and save it.")
    option_list = BaseCommand.option_list + (
         make_option('--email-file', dest='email', help='File containing email (default: stdin)'),)

    def handle(self, *args, **options):
        email = options.get('email', None)
        msg = None
        help_message = 'Usage: receive_email --email-file <email-file>'

        if not email:
            msg = sys.stdin.read()
        else:
            msg = open(email, "r").read()

        try:
            message = create_response_email(msg)
            log(u"Received nomcom email from %s" % message.frm)
        except (EncryptedException, ValueError) as e:
            raise CommandError(e)
