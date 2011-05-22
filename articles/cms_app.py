# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ArticlesHook(CMSApp):
    name = _("Articles")
    urls = ["articles.urls"]

apphook_pool.register(ArticlesHook)(bigee2)
