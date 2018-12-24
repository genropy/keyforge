# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('player',pkey='nickname',name_long='Player',name_plural='Players',caption_field='nickname')
        tbl.column('nickname',size=':50',name_long='Nickname',name_short='Nickname',unique=True,indexed=True, unmodifiable=True,)
        tbl.column('firstname',size=':50',name_long='First name',name_short='First name')
        tbl.column('lastname',size=':50',name_long='Last name',name_short='Last name')
        tbl.column('user_id',size='22',name_long='User',name_short='User', unmodifiable=True).relation('adm.user.id',relation_name='player', mode='foreignkey', one_one=True)
        tbl.column('tot_matches', dtype = 'L', name_long = 'Nr.Matches')
        tbl.column('won_matches', dtype = 'L', name_long = 'Won Matches')
        tbl.column('lost_matches', dtype = 'L', name_long = 'Lost Matches')
        tbl.column('tot_keys', dtype = 'L', name_long = 'Tot.Keys')


        tbl.formulaColumn('frm_tot_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$win_player=#THIS.nickname OR $lose_player=#THIS.nickname'), dtype='N', name_long='Nr.Matches (FRM)')
        tbl.formulaColumn('frm_won_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$win_player=#THIS.nickname'), dtype='N', name_long='Won Matches (FRM)')
        tbl.formulaColumn('frm_lost_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$lose_player=#THIS.nickname'), dtype='N', name_long='Lost Matches (FRM)')
        tbl.formulaColumn('frm_tot_keys', select=dict(columns='SUM($win_keys)+SUM($lose_keys)', table='kftm.match', where='$win_player=#THIS.nickname OR $lose_player=#THIS.nickname'), dtype='N', name_long='Tot keys (FRM)')


    def updateTotals(self, match_record):
        def cb_deck(r):
            r['tot_matches']=r['frm_tot_matches']
            r['won_matches']=r['frm_won_matches']
            r['lost_matches']=r['frm_lost_matches']
            r['tot_keys']=r['frm_tot_keys']

        self.batchUpdate(cb_deck,
                          columns='*,$frm_tot_matches,$frm_won_matches,$frm_lost_matches,$frm_tot_keys',
                          where='$nickname=:win_player OR $nickname=:lose_player',
                          win_player=match_record['win_player'],
                          lose_player=match_record['lose_player'])