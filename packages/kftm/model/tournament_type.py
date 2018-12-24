# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tournament_type',pkey='code',name_long='Tournament Type',name_plural='Tournament Types',caption_field='description')
        self.sysFields(tbl,id=False)
        tbl.column('code',size=':10',name_long='Code',name_short='Code',unique=True,indexed=True)
        tbl.column('description',size=':50',name_long='Description',name_short='Description',unique=True,indexed=True)
