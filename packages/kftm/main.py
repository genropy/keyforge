#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='kftm package',sqlschema='kftm',sqlprefix=True,
                    name_short='Kftm', name_long='Keyforge tournament manager', name_full='Kftm')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
