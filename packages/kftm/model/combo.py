class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('card_trait',pkey='id',name_long='card_trait',name_plural='card_trait',caption_field='id')
        self.sysFields(tbl)
        tbl.column('card_one_id',size='36',name_long='Card one',name_short='Card One').relation('card.kf_id',relation_name='2_combos', mode='foreignkey', onDelete='cascade')
        tbl.column('card_two_id',size='36',name_long='Card two',name_short='Card Two').relation('card.kf_id',relation_name='1_combos', mode='foreignkey', onDelete='cascade')
        tbl.column('instructions', name_long='Instructions')
        tbl.column('title', name_long='Title')
        tbl.column('player',size=':50',name_long='Suggested by').relation('player.nickname',
                                                                                        relation_name='suggested_combos',
                                                                                         mode='foreignkey',
                                                                                         one_name='Players',
                                                                                         many_name='Decks',
                                                                                         onDelete='cascade')