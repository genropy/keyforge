# encoding: utf-8
from gnr.core.gnrdecorator import metadata


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('act_trigger',pkey='trigger',name_long='Activation trigger',name_plural='Activation trigger',caption_field='trigger')
        self.sysFields(tbl, id=False)
        tbl.column('trigger',size=':30',name_long='Trigger',name_short='Trigger',unique=True,indexed=True)
        tbl.column('code', size=':12')

    @metadata(mandatory=True)
    def sysRecord_PLAY(self):
        return self.newrecord(trigger='Play', code='PLAY')

    @metadata(mandatory=True)
    def sysRecord_ACTION(self):
        return self.newrecord(trigger='Action', code='ACTION')

    @metadata(mandatory=True)
    def sysRecord_REAP(self):
        return self.newrecord(trigger='Reap', code='REAP')

    @metadata(mandatory=True)
    def sysRecord_FIGHT(self):
        return self.newrecord(trigger='Fight', code='FIGHT')

    @metadata(mandatory=True)
    def sysRecord_BEFORE_FIGHT(self):
        return self.newrecord(trigger='Before Fight', code='BEFORE_FIGHT')

    @metadata(mandatory=True)
    def sysRecord_OMNI(self):
        return self.newrecord(trigger='Omni', code='OMNI')

    @metadata(mandatory=True)
    def sysRecord_DESTROYED(self):
        return self.newrecord(trigger='Destroyed', code='DESTROYED')


