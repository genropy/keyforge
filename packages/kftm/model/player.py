# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('player',pkey='nickname',name_long='Player',name_plural='Players',caption_field='nickname')
        tbl.column('nickname',size=':50',name_long='Nickname',name_short='Nickname',unique=True,indexed=True)
        tbl.column('firstname',size=':50',name_long='First name',name_short='First name')
        tbl.column('lastname',size=':50',name_long='Last name',name_short='Last name')
        tbl.column('user_id',size='22',name_long='User',name_short='User').relation('adm.user.id',relation_name='player', mode='foreignkey', one_one=True)
