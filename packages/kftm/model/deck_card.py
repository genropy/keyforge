# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('deck_card',pkey='id',name_long='Deck cards',name_plural='Deck cards',caption_field='id')
        self.sysFields(tbl)
        tbl.column('deck_id',size='36',name_long='Deck Id',name_short='Deck Id').relation('deck.kf_id',relation_name='cards', onDelete='cascade')
        tbl.column('card_id',size='36',name_long='Card Id',name_short='Card Id').relation('card.kf_id',relation_name='decks', onDelete='cascade')
        tbl.aliasColumn('deck_name', relation_path='@deck_id.name', name_long='Deck name')
        tbl.aliasColumn('deck_players', relation_path='@deck_id.@players.player', name_long='Player')
        tbl.aliasColumn('card_title', relation_path='@card_id.card_title', name_long='Card title')
        tbl.aliasColumn('card_type', relation_path='@card_id.card_type', name_long='Card type')
        tbl.aliasColumn('card_house', relation_path='@card_id.house', name_long='House')
        tbl.aliasColumn('card_amber', dtype='I', relation_path='@card_id.amber', name_long='Amber')
        tbl.aliasColumn('card_power', dtype='I', relation_path='@card_id.power', name_long='Cr.Power')
        tbl.aliasColumn('card_armor', dtype='I', relation_path='@card_id.armor', name_long='Cr.Armor')
        tbl.aliasColumn('card_text', relation_path='@card_id.card_text_only', name_long='Text')