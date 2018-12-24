# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('match',pkey='id',name_long='Match result',name_plural='Matches results',caption_field='full_caption')
        self.sysFields(tbl, counter=True)
        tbl.column('date', dtype='D', name_long='Date')

        tbl.column('win_player',size=':50',name_long='Winner', validate_notnull=True).relation('kftm.player.nickname',relation_name='matches_won', mode='foreignkey')
        tbl.column('lose_player',size=':50',name_long='Loser', validate_notnull=True).relation('kftm.player.nickname',relation_name='matches_lost', mode='foreignkey')
        tbl.column('win_deck_id',size='36',name_long='Winner Deck', validate_notnull=True, group='_').relation('deck.kf_id',
                                                                  relation_name='matches_won',
                                                                  mode='foreignkey',
                                                                  onDelete='setnull')
        tbl.column('lose_deck_id',size='36',name_long='Loser deck', validate_notnull=True, group='_').relation('deck.kf_id',
                                                                  relation_name='matches_lost',
                                                                  mode='foreignkey',
                                                                  onDelete='setnull')
        tbl.column('win_keys',dtype='I',name_long='W.Keys', validate_notnull=True)
        tbl.column('lose_keys',dtype='I',name_long='L.Keys', validate_notnull=True)
        tbl.column('win_chains',dtype='I',name_long='W.Chains')
        tbl.column('lose_chains',dtype='I',name_long='L.Chains')
        tbl.column('tournament_id',name_long='Tournament').relation('kftm.tournament.id',relation_name='results', mode='foreignkey')

        #tbl.formulaColumn('involved_houses', select=dict(table='kftm.house', columns='$house', where='@decks.deck_id=#THIS.win_deck OR @decks.deck_id=#THIS.lose_deck', group_by='$house', distinct='$house'), name_long='Involved houses')
        tbl.formulaColumn('houses_title', "@win_deck_id.houses||' VS '||@lose_deck_id.houses", name_long='Houses')
        tbl.formulaColumn('result', "$win_keys||'-'||$lose_keys", name_long='Result')
        tbl.formulaColumn('players_title', "$win_player||' VS '||$lose_player", name_long='Players')
        tbl.formulaColumn('decks_title', "@win_deck_id.short_name||' VS '||@lose_deck_id.short_name", name_long='Decks')
        tbl.formulaColumn('decks_houses_title', "@win_deck_id.short_name||' ('||@win_deck_id.houses||') VS '||@lose_deck_id.short_name||' ('||@lose_deck_id.houses||')'", name_long='Decks/Houses')
        tbl.formulaColumn('full_caption', "'M'||$_row_count||': '||$decks_title ||' ('|| $result ||')'", name_long='Full title')


    def trigger_onInserted(self, record):
        self.db.deferToCommit(self.deferredUpdateTotals, match_record=record)

    def trigger_onUpdated(self, record, old_record):
        self.db.deferToCommit(self.deferredUpdateTotals, match_record=record)

    def trigger_onDeleted(self, record):
        self.deferredUpdateTotals(record)
    
    def deferredUpdateTotals(self, match_record):
        self.db.deferToCommit(self.updateTotals, match_record=match_record)

    def updateTotals(self, match_record=None):
        self.db.table('kftm.deck').updateTotals(match_record)
        self.db.table('kftm.player').updateTotals(match_record)
        
   
    def defaultValues(self):
        return dict(date=self.db.workdate, win_keys=3, win_chains=0, lose_chains=0, lose_keys=0)
