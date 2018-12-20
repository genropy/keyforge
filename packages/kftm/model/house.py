# encoding: utf-8
from gnr.core.gnrdecorator import metadata


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('house',pkey='house',name_long='House',name_plural='Houses',caption_field='house')
        self.sysFields(tbl, id=False)
        tbl.column('house',size=':7',name_long='House Id',name_short='Id',unique=True,indexed=True)
        tbl.column('name',size=':7',name_long='Name',name_short='Name',unique=True,indexed=True)
        tbl.column('image',size=':70',name_long='Image',name_short='Image')
        tbl.column('code', size='3', name_long='Code', unique=True, indexed=True)

    #def importFromDeck(self, houses_data):
    #    house_pkeys = houses_data.digest('#v.id')
    #    existings = self.query(where='$house IN :house_pkeys', house_pkeys=house_pkeys).fetchAsDict(key='house')
    #    if len(existings.keys())==7:
    #        return
    #    for h in houses_data.values():
    #        if h['id'] not in existings:
    #            h['house']=h.pop('id')
    #            self.insert(dict(h))

    @metadata(mandatory=True)
    def sysRecord_DIS(self):
        return self.newrecord(code='DIS',house='Dis', name='Dis', image='https://cdn.keyforgegame.com/media/houses/Dis_OooSNPO.png')

    @metadata(mandatory=True)
    def sysRecord_UNT(self):
        return self.newrecord(code='UNT',house='Untamed', name='Untamed', image='https://cdn.keyforgegame.com/media/houses/Untamed_bXh9SJD.png')

    @metadata(mandatory=True)
    def sysRecord_LOG(self):
        return self.newrecord(code='LOG',house='Logos', name='Logos', image='https://cdn.keyforgegame.com/media/houses/Logos_2mOY1dH.png')

    @metadata(mandatory=True)
    def sysRecord_MAR(self):
        return self.newrecord(code='MAR',house='Mars', name='Mars', image='https://cdn.keyforgegame.com/media/houses/Mars_CmAUCXI.png')

    @metadata(mandatory=True)
    def sysRecord_BRO(self):
        return self.newrecord(code='BRO',house='Brobnar', name='Brobnar', image='https://cdn.keyforgegame.com/media/houses/Brobnar_RTivg44.png')

    @metadata(mandatory=True)
    def sysRecord_SHD(self):
        return self.newrecord(code='SHD',house='Shadows', image='https://cdn.keyforgegame…uses/Shadows_z0n69GG.png')

    @metadata(mandatory=True)
    def sysRecord_SAN(self):
        return self.newrecord(code='SAN',house='Sanctum', name='Sanctum', image='"https://cdn.keyforgegame…uses/Sanctum_lUWPG7x.png"')

