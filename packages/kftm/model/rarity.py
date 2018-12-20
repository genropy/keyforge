# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('rarity',pkey='rarity',name_long='Rarity',name_plural='Rarities',caption_field='rarity')
        self.sysFields(tbl, id=False)
        tbl.column('rarity',name_long='rarity',unique=True,indexed=True)
        tbl.column('code', size='1', name_long='Code', unique=True, indexed=True)


    
    @metadata(mandatory=True)
    def sysRecord_S(self):
        return self.newrecord(code='S',rarity='Special')

    @metadata(mandatory=True)
    def sysRecord_R(self):
        return self.newrecord(code='R',rarity='Rare')

    @metadata(mandatory=True)
    def sysRecord_C(self):
        return self.newrecord(code='C',rarity='Common')

    @metadata(mandatory=True)
    def sysRecord_U(self):
        return self.newrecord(code='U',rarity='Uncommon')

