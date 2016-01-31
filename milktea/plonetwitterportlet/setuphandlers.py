from collective.grok import gs
from milktea.plonetwitterportlet import MessageFactory as _

@gs.importstep(
    name=u'milktea.plonetwitterportlet', 
    title=_('milktea.plonetwitterportlet import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('milktea.plonetwitterportlet.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
