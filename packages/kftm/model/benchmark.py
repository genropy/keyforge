# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('benchmark',pkey='id',name_long='Benchmark',name_plural='Benchmarks',caption_field='title', rowcaption='$title')
        self.sysFields(tbl)
        tbl.column('player', size=':50',name_long='Player',name_short='Player').relation('player.nickname',
                                                                                        relation_name='benchmarks',
                                                                                         mode='foreignkey',
                                                                                         one_name='Players',
                                                                                         many_name='Benchmarks',
                                                                                         onDelete='cascade')
        tbl.column('title', name_long='Title')
        tbl.column('notes', name_long='Notes')

