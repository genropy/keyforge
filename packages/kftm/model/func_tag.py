# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('func_tag',pkey='code',name_long='Func.Tag',name_plural='Func.Tags',caption_field='description', lookup=True, rowcaption='description')
        self.sysFields(tbl, id=False)
        tbl.column('description',name_long='Description',unique=True, indexed=True)
        tbl.column('code',size=':3', name_long='Code',unique=True, indexed=True)

    @metadata(mandatory=True)
    def sysRecord_AMC(self):
        return self.newrecord(code='AMC',description='Amber control')

    @metadata(mandatory=True)
    def sysRecord_CRM(self):
        return self.newrecord(code='CRM',description='Creatures removal')

    @metadata(mandatory=True)
    def sysRecord_GA(self):
        return self.newrecord(code='GA',description='Gain amber')
        
    @metadata(mandatory=True)
    def sysRecord_DD(self):
        return self.newrecord(code='DD',description='Deal damage')

    @metadata(mandatory=True)
    def sysRecord_AC(self):
        return self.newrecord(code='AC',description='Archive Card')

    @metadata(mandatory=True)
    def sysRecord_FK(self):
        return self.newrecord(code='FK',description='Forge Key')

    @metadata(mandatory=True)
    def sysRecord_DC(self):
        return self.newrecord(code='DC',description='Draw cards')


#

    #@metadata(mandatory=True)
    #def sysRecord_SA(self):
    #    return self.newrecord(code='SA',description='Steal amber')
#
    #@metadata(mandatory=True)
    #def sysRecord_LA(self):
    #    return self.newrecord(code='LA',description='Lose amber')
#

    #@metadata(mandatory=True)
    #def sysRecord_DM(self):
    #    return self.newrecord(code='DMC',description='Destroy many')
#
    #@metadata(mandatory=True)
    #def sysRecord_CA(self):
    #    return self.newrecord(code='CA',description='Capture amber')
#
    #@metadata(mandatory=True)
    #def sysRecord_AEC(self):
    #    return self.newrecord(code='AEC',description='Archive enemy creature')
#
    #@metadata(mandatory=True)
    #def sysRecord_CEC(self):
    #    return self.newrecord(code='CEC',description='Control enemy creature')
#
    #@metadata(mandatory=True)
    #def sysRecord_DOC(self):
    #    return self.newrecord(code='DEC',description='Destroy creature')
#

    #@metadata(mandatory=True)
    #def sysRecord_RFC(self):
    #    return self.newrecord(code='RFC',description='Raise forge cost')
#
    #@metadata(mandatory=True)
    #def sysRecord_SC(self):
    #    return self.newrecord(code='SC',description='Stun creature')
#
    #@metadata(mandatory=True)
    #def sysRecord_RC(self):
    #    return self.newrecord(code='RC',description='Ready creature')
#
    #@metadata(mandatory=True)
    #def sysRecord_CHC(self):
    #    return self.newrecord(code='CHC',description='Control house choice')
#


