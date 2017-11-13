from __future__ import absolute_import

from django.core.cache import cache

from sentry.web.frontend.base import BaseView
from sentry.web.helpers import render_to_response
from sentry.api.endpoints.setup_wizard import SETUP_WIZARD_CACHE_KEY


class SetupWizardView(BaseView):

    def get(self, request, wizard_hash):
        """
        This opens a page where with an active session fill stuff into the cache
        Redirects to organization whenever cache has been deleted
        """
        context = {
            'hash': wizard_hash
        }
        key = '%s%s' % (SETUP_WIZARD_CACHE_KEY, wizard_hash)
        wizard_data = cache.get(key)
        if wizard_data is None:
            return self.redirect_to_org(request)
        return render_to_response('sentry/setup-wizard.html', context, self.request)
