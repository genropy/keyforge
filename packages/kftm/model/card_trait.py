# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('card_trait',pkey='id',name_long='card_trait',name_plural='card_trait',caption_field='id')
        self.sysFields(tbl)
        tbl.column('card_id',size='36',name_long='Card Id',name_short='Card Id').relation('card.kf_id',relation_name='rel_traits', mode='foreignkey')
        tbl.column('trait',size=':20',name_long='Trait',name_short='Trait').relation('trait.trait',relation_name='rel_cards', mode='foreignkey')
