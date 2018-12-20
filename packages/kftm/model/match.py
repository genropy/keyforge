# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('match',pkey='id',name_long='Match result',name_plural='Matches results',caption_field='full_caption')
        self.sysFields(tbl, counter=True)
        tbl.column('date', dtype='D', name_long='Date')

        tbl.column('win_player',size=':50',name_long='Winner', validate_notnull=True).relation('kftm.player.nickname',relation_name='won_matches', mode='foreignkey')
        tbl.column('lose_player',size=':50',name_long='Loser', validate_notnull=True).relation('kftm.player.nickname',relation_name='lost_matches', mode='foreignkey')
        tbl.column('win_deck',size='36',name_long='Winner Deck', validate_notnull=True).relation('deck.kf_id',
                                                                  relation_name='won_matches',
                                                                  mode='foreignkey',
                                                                  onDelete='setnull')
        tbl.column('lose_deck',size='36',name_long='Loser deck', validate_notnull=True).relation('deck.kf_id',
                                                                  relation_name='lost_matches',
                                                                  mode='foreignkey',
                                                                  onDelete='setnull')
        tbl.column('win_keys',dtype='I',name_long='W.Keys', validate_notnull=True)
        tbl.column('lose_keys',dtype='I',name_long='L.Keys', validate_notnull=True)
        tbl.column('win_chains',dtype='I',name_long='W.Chains')
        tbl.column('lose_chains',dtype='I',name_long='L.Chains')
        tbl.formulaColumn('result', "$win_keys||'-'||$lose_keys", name_long='Result')
        tbl.formulaColumn('players_title', "$win_player||' VS '||$lose_player", name_long='Players')
        tbl.formulaColumn('decks_title', "@win_deck.short_name||' VS '||@lose_deck.short_name", name_long='Decks')
        tbl.formulaColumn('full_caption', "$title||':'||$result", name_long='Full caption')


    def defaultValues(self):
        return dict(date=self.db.workdate, win_keys=3, win_chains=0, lose_chains=0, lose_keys=0)
