# encoding: utf-8
from gnr.core.gnrdecorator import metadata


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('keyword',pkey='keyword',name_long='Keyword ability',name_plural='Keyword abilities',caption_field='keyword')
        tbl.column('keyword',size=':30',name_long='Keyword',name_short='Keyword',unique=True,indexed=True)


    #@metadata(mandatory=True)
    #def sysRecord_E(self):
    #    return self.newrecord(type='Elusive')
#
    #@metadata(mandatory=True)
    #def sysRecord_R(self):
    #    return self.newrecord(code='R',type='Rare')
#
    #@metadata(mandatory=True)
    #def sysRecord_C(self):
    #    return self.newrecord(code='C',type='Common')
#
    #@metadata(mandatory=True)
    #def sysRecord_U(self):
    #    return self.newrecord(code='U',type='Uncommon')
#
