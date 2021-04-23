from django.utils.translation import ugettext_lazy as _


MULTIPLE_CHOICE = 0
MULTIPLE_RESPONSE = 1
TRUE_FALSE = 2
SHORT_ANSWER = 3

TYPE = (
    (MULTIPLE_CHOICE, _('Multiple Choice')),
    (MULTIPLE_RESPONSE, _('Multiple Response')),
    (TRUE_FALSE, _('True or False')),
    (SHORT_ANSWER, _('Short Answer'))
 )