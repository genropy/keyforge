# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('benchmark_deck',pkey='id',name_long='Benchmark deck',name_plural='Benchmark decks',caption_field='deck_name', rowcaption='$deck_name')
        self.sysFields(tbl)
        tbl.column('benchmark_id',size='22',name_long='Benchmark id').relation('benchmark.id',
                                                                                        relation_name='decks',
                                                                                         mode='foreignkey',
                                                                                         one_name='Benchmarks',
                                                                                         many_name='Decks',
                                                                                         onDelete='cascade')

        tbl.column('deck_id',size='36',name_long='Deck',name_short='Deck').relation('deck.kf_id',
                                                                                    relation_name='in_benchmarks',
                                                                                    mode='foreignkey',
                                                                                     many_name='In Benchmarks',
                                                                                    one_name='Decks',
                                                                                    onDelete='cascade')
        tbl.column('notes')
        tbl.aliasColumn('deck_name', relation_path='@deck_id.name', name_long='Deck name')
        tbl.aliasColumn('deck_houses', relation_path='@deck_id.houses', name_long='Deck houses')

    def trigger_onInserting(self, record):
        if record['deck_id']:
            return
        record['deck_id']=record['kf_id']
        deck_tbl=self.db.table('kftm.deck')
        existing_deck=deck_tbl.query(where='kf_id=:kf_id', kf_id=record['deck_id']).fetch()
        if existing_deck:
            return
        deck_tbl.importDeck(record['deck_id'])
        