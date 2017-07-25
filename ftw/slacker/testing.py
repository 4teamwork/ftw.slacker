from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig


class FtwSlackerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ftw.slacker
        xmlconfig.file('configure.zcml',
                       ftw.slacker,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        pass

FTW_SLACKER_FIXTURE = FtwSlackerLayer()
FTW_SLACKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_SLACKER_FIXTURE,), name="ftw.slacker:Functional")
