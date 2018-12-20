# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('card_trigger',pkey='id',name_long='Card trigger',name_plural='Card triggers',caption_field='id')
        self.sysFields(tbl)
        tbl.column('card_id',size='36',name_long='Card',name_short='Card').relation('card.kf_id',relation_name='triggers', onDelete='cascade')
        tbl.column('trigger',size=':30',name_long='Trigger',name_short='Trigger').relation('act_trigger.trigger',relation_name='cards', onDelete='cascade')
        tbl.aliasColumn('card_type', '@card_id.card_type', name_long='Card type')