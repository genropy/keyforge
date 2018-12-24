# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tournament',pkey='id',name_long='Tournament',name_plural='Tournaments',caption_field='id')
        self.sysFields(tbl)
        tbl.column('title',size=':50',name_long='Title',name_short='Title',unique=True,indexed=True)
        tbl.column('long_description',name_long='Long description',name_short='Long description')
        tbl.column('tournament_type',size=':10',name_long='Type',name_short='Type').relation('kftm.tournament_type.code',relation_name='tournaments', mode='foreignkey', onDelete='setnull')
        tbl.column('date_start',dtype='D',name_long='Date start',name_short='Date end')
        tbl.column('date_end',dtype='D',name_long='Date end',name_short='Date end')
