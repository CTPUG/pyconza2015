# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
    os.path.join(pyconzadir, 'bower_components'),
)

TEMPLATE_DIRS = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATE_DIRS


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
     "items": []},
    {"name": "venue", "label": _("Venue"),
     "url": reverse_lazy("wafer_page", args=("venue",))},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "praekelt", "label": _(u"» Praekelt ★"),
          "url": reverse_lazy("wafer_sponsor", args=(2,))},
         {"name": "takealot", "label": _(u"» Takealot ★"),
          "url": reverse_lazy("wafer_sponsor", args=(4,))},
         {"name": "oracle", "label": _(u"» Oracle ★"),
          "url": reverse_lazy("wafer_sponsor", args=(1,))},
         {"name": "psf", "label": _(u"PSF"),
          "url": reverse_lazy("wafer_sponsor", args=(3,))},
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
     ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         #{"name": "schedule", "label": _("Schedule"),
         # "url": reverse_lazy("wafer_full_schedule")},
         #{"name": "schedule-next-up", "label": _("Next up"),
         # # Once conference has started use:
         # # "url": reverse_lazy("wafer_current")},
         # "url": "/schedule/current/?day=2015-10-01&time=08:30"},
         {"name": "accepted-talks", "label": _("Accepted Talks"),
          "url": reverse_lazy("wafer_users_talks")},
     ]},
    {"menu": "events", "label": _("News"),
     "items": []},
    {"menu": "previous-pycons", "label": _("Past PyConZAs"),
     "items": [
         {"name": "pyconza2012", "label": _("PyConZA 2012"),
          "url": "http://2012.za.pycon.org/"},
         {"name": "pyconza2013", "label": _("PyConZA 2013"),
          "url": "http://2013.za.pycon.org/"},
         {"name": "pyconza2014", "label": _("PyConZA 2014"),
          "url": "http://2014.za.pycon.org/"},
     ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com/pyconza"},
    {"name": "googleplus", "label": "Google+",
     "image": "/static/img/googleplus.png",
     "url": "https://plus.google.com/events/ccqgtdbrk712n64ruc66s4tpsms"},
    {"name": "facebook", "label": "Facebook",
     "image": "/static/img/facebook.png",
     "url": "https://www.facebook.com/pyconza2015"},
)


CRISPY_TEMPLATE_PACK = 'bootstrap3'
MARKITUP_FILTER = ('markdown.markdown', {
    'safe_mode': False,
    'extensions': [
        'outline',
        'attr_list',
        'attr_cols',
        'markdown.extensions.tables',
    ],
})
# Use HTTPS jquery URL so it's accessible on HTTPS pages (e.g. editing a talk)
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js'
