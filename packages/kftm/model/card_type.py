# encoding: utf-8
from gnr.core.gnrdecorator import metadata



class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('card_type',pkey='type',name_long='card_type',name_plural='card_type',caption_field='type')
        self.sysFields(tbl, id=False)
        tbl.column('type',size=':8',name_long='Type',unique=True,indexed=True)
        tbl.column('code',size='2',name_long='Code',unique=True,indexed=True)


    @metadata(mandatory=True)
    def sysRecord_AR(self):
        return self.newrecord(code='AR',type='Artifact')

    @metadata(mandatory=True)
    def sysRecord_UP(self):
        return self.newrecord(code='UP',type='Upgrade')

    @metadata(mandatory=True)
    def sysRecord_CR(self):
        return self.newrecord(code='CR',type='Creature')

    @metadata(mandatory=True)
    def sysRecord_AC(self):
        return self.newrecord(code='AC',type='Action')
 
