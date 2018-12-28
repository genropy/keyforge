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
        bc=form.center.borderContainer(datapath='#FORM')
        chunkpane = bc.contentPane(region='top',border_bottom='1px solid silver', height='160px', datapath='#FORM.record')
        chunkpane.templateChunk(table='kftm.deck',record_id='^.kf_id',
                                position='absolute',top='3px',left='3px',right='7px',bottom='7px',padding='6px',
                                rounded=4,background='white',border='1px solid silver', template='deck_template')

        tc=bc.tabContainer(region='center')
        tc.contentPane(title='Cards',datapath='#FORM').plainTableHandler(relation='@cards', viewResource='ViewFromDeck', nodeId='deck_cards')
       
    def th_options(self):
        return dict(dialog_height='600px', dialog_width='800px',modal=True)


