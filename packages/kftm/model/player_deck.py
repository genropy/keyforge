# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('player_deck',pkey='id',name_long='player_deck',name_plural='player_deck',caption_field='deck_name', rowcaption='$deck_name')
        self.sysFields(tbl)
        tbl.column('player',size=':50',name_long='Player',name_short='Player').relation('player.nickname',
                                                                                        relation_name='decks',
                                                                                         mode='foreignkey',
                                                                                         one_name='Players',
                                                                                         many_name='Decks',
                                                                                         onDelete='cascade')
        tbl.column('deck_id',size='36',name_long='Deck',name_short='Deck').relation('deck.kf_id',
                                                                                    relation_name='players',
                                                                                    mode='foreignkey',
                                                                                     many_name='Players',
                                                                                    one_name='Decks',
                                                                                    onDelete='cascade')
        tbl.column('player_notes', name_long='Notes')
        tbl.aliasColumn('deck_name', relation_path='@deck_id.name', name_long='Deck name')
        tbl.aliasColumn('deck_houses', relation_path='@deck_id.houses', name_long='Deck houses')

    def trigger_onInserting(self, record):
        deck_tbl=self.db.table('kftm.deck')
        existing_deck=deck_tbl.query(where='kf_id=:kf_id', kf_id=record['deck_id']).fetch()
        if not existing_deck:
            deck_tbl.importDeck(record['deck_id'],short_name=record['short_name'])