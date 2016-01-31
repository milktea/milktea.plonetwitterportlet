from zope import schema
from zope.interface import Interface
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form
from zope.interface import invariant, Invalid

from milktea.plonetwitterportlet import MessageFactory as _

class ITwitterSettings(Interface):
    twitter_username = schema.TextLine(title=_(u'Twitter Username'),
                                description=_(u"Default twitter username for the entire site. Dont inlcude '@'.  E.g 'milktea'"))
   

    @invariant
    def username(data):
        if '@' in  data.twitter_username:
            raise Invalid(_(u"Invalid username. Remove '@'"))

class TwitterControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = ITwitterSettings

TwitterControlPanelView = layout.wrap_form(TwitterControlPanelForm, ControlPanelFormWrapper)
TwitterControlPanelView.label = _(u"Milktea Plone Twitter Portlet Settings")





