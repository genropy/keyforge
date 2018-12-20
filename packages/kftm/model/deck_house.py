# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('deck_house',pkey='id',name_long='Deck houses',name_plural='Deck houses',caption_field='id')
        self.sysFields(tbl)
        tbl.column('deck_id',size='36',name_long='Deck',name_short='Deck').relation('deck.kf_id',relation_name='deck_houses', onDelete='cascade')
        tbl.column('house',size=':7',name_long='House',name_short='House').relation('house.house',relation_name='decks', onDelete='cascade')
