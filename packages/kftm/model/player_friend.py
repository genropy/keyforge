# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('player_friend',pkey='id',name_long='Player friend',name_plural='Player friends',caption_field='id')
        self.sysFields(tbl)
        tbl.column('player',size=':50',name_long='Player',name_short='Player').relation('kftm.player.nickname',relation_name='my_friends', mode='foreignkey')
        tbl.column('friend',size=':50',name_long='Fried',name_short='Friend').relation('kftm.player.nickname',relation_name='friended_by', mode='foreignkey')
