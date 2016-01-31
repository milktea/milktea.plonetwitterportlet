from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import invariant, Invalid
from milktea.plonetwitterportlet import MessageFactory as _

grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):

    twitter_username = schema.TextLine(
            title = u"Add Twitter Username",
            description=u"Override default twitter username of the entire site. (Config at http://localhost:8080/Plone/@@twitter-controlpanel). If not, leave blank.",
            required=False,
        )

    @invariant
    def username(data):
        if data.twitter_username:
            if '@' in  data.twitter_username:
                raise Invalid(_(u"Invalid username. Remove '@'"))

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    
    def __init__(self, twitter_username=None):
        self.twitter_username = twitter_username
       
       
    @property
    def title(self):
        return "Milktea Twitter Portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/milkteatwitterportlet.pt')
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
    def contents(self):
        portlet_username = self.data.twitter_username
        if portlet_username:
            return portlet_username
        else:
            return self.twitter_default()

    def twitter_default(self):
        registry = getUtility(IRegistry)
        field = 'milktea.plonetwitterportlet.controlpanel.ITwitterSettings.twitter_username'
        twitter_username = ''
        if registry.get(field):
            twitter_username = registry.get(field).encode()
        return twitter_username

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Milktea Twitter Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Milktea Twitter Portlet"
    description = ''
