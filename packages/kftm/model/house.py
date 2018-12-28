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
        
        #tbl.column('tot_matches', dtype = 'L', name_long = 'Nr.Matches')
        #tbl.column('won_matches', dtype = 'L', name_long = 'Won Matches')
        #tbl.column('lost_matches', dtype = 'L', name_long = 'Lost Matches')
        #tbl.column('tot_keys', dtype = 'L', name_long = 'Tot.Keys')

        tbl.formulaColumn('frm_tot_matches', select=dict(columns='SUM($tot_matches)', table='kftm.deck', where='@houses.house=:#THIS.house'), dtype='N', name_long='Nr.Matches (FRM)')
        tbl.formulaColumn('frm_won_matches', select=dict(columns='SUM($won_matches)', table='kftm.deck', where='@houses.house=:#THIS.house'), dtype='N', name_long='Won Matches (FRM)')
        tbl.formulaColumn('frm_lost_matches', select=dict(columns='SUM($lost_matches)', table='kftm.deck', where='@houses.house=:#THIS.house'), dtype='N', name_long='Lost Matches (FRM)')
        #tbl.formulaColumn('frm_tot_keys', select=dict(columns='SUM($tot_keys)', table='kftm.deck', where='@houses.house=:#THIS.house'), dtype='N', name_long='Tot keys (FRM)')
        tbl.formulaColumn('frm_win_ratio', '$frm_won_matches/$frm_tot_matches', dtype='N', name_long='Win ratio')
        tbl.formulaColumn('frm_key_ratio', '$frm_tot_keys/$frm_tot_matches', dtype='N', name_long='Win ratio')


    #def updateTotals(self, match_record):
    #    def cb_deck(r):
    #        r['tot_matches']=r['frm_tot_matches']
    #        r['won_matches']=r['frm_won_matches']
    #        r['lost_matches']=r['frm_lost_matches']
    #        r['tot_keys']=r['frm_tot_keys']
#
    #    self.batchUpdate(cb_deck,
    #                      columns='*,$frm_tot_matches,$frm_won_matches,$frm_lost_matches,$frm_tot_keys',
    #                      where='$kf_id=:win_deck_id OR $kf_id=:lose_deck_id',
    #                      win_deck_id=match_record['win_deck_id'],
    #                      lose_deck_id=match_record['lose_deck_id'] )
#


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

