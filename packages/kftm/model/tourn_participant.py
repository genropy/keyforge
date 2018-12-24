# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tourn_participant',pkey='id',name_long='Participant',name_plural='Participants',caption_field='id')
        self.sysFields(tbl)
        tbl.column('player',name_long='Player', validate_notnull=True).relation('kftm.player.nickname',relation_name='tournaments', mode='foreignkey')
        tbl.column('tournament_id',name_long='Tournament').relation('kftm.tournament.id',relation_name='participants', mode='foreignkey')
