#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
import requests
from gnr.core.gnrbag import Bag
from time import sleep


class View(BaseComponent):

    #def th_hiddencolumns(self):
    #    return '$players,$cards,$traits'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name', width='25em')
        #r.fieldcell('power_level' )
        #r.fieldcell('chains' )
        r.fieldcell('houses', width='18em')
        r.fieldcell('n_creatures')
        r.fieldcell('n_artifacts')
        r.fieldcell('n_actions')
        r.fieldcell('n_upgrades')
        r.fieldcell('tot_amber')
        r.fieldcell('avg_amber')
        r.fieldcell('avg_cr_power')
        r.fieldcell('avg_cr_armor')
        r.fieldcell('tot_matches')
        r.fieldcell('won_matches')
        r.fieldcell('lost_matches')
        r.fieldcell('victory_rate')
        r.fieldcell('avg_keys')
        r.fieldcell('players', width='100%')
        
        

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='name', op='contains', val='')

    def th_queryBySample(self):
        return dict(fields=[dict(field='name',lbl='Name',width='10em'),
                            dict(field='houses',lbl='Houses',width='10em'),
                            dict(field='players',lbl='Players',width='10em'),
                            dict(field='cards',lbl='Cards',width='15em'),
                            dict(field='deck_traits',lbl='Traits',width='10em')], cols=5, isDefault=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('kf_id' )
        fb.field('name' )
        #fb.field('expansion' )
        fb.field('power_level' )
        fb.field('chains' )
        fb.field('houses')
        fb.field('n_creatures')
        fb.field('n_artifacts')
        fb.field('n_actions')
        fb.field('n_upgrades')
        fb.field('tot_amber')
        fb.field('avg_amber')
        fb.field('avg_cr_power')
        fb.field('avg_cr_armor')
   
