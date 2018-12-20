# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('trait',pkey='trait',name_long='Trait',name_plural='Traits',caption_field='trait')
        tbl.column('trait',size=':20',name_long='Trait',name_short='Trait',unique=True,indexed=True)
