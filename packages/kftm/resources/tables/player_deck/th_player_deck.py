#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method


class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('player')
        r.fieldcell('deck_id')

    def th_order(self):
        return 'player'

    def th_query(self):
        return dict(column='id', op='contains', val='')


class ViewFromPlayer(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('deck_id', width='25em')
        r.fieldcell('deck_houses', width='20em')
        r.fieldcell('@deck_id.n_creatures')
        r.fieldcell('@deck_id.n_artifacts')
        r.fieldcell('@deck_id.n_actions')
        r.fieldcell('@deck_id.n_upgrades')
        r.fieldcell('@deck_id.tot_amber')
        r.fieldcell('@deck_id.avg_amber')
        r.fieldcell('@deck_id.avg_cr_power')
        r.fieldcell('@deck_id.avg_cr_armor')
        r.fieldcell('player_notes', width='100%')




class Form(BaseComponent):

    def th_form(self, form):
        bc=form.center.borderContainer(datapath='#FORM')
        chunkpane = bc.contentPane(region='top',border_bottom='1px solid silver', height='160px', datapath='#FORM.record')
        chunkpane.templateChunk(table='kftm.deck',record_id='^.deck_id',
                                position='absolute',top='3px',left='3px',right='7px',bottom='7px',padding='6px',
                                rounded=4,background='white',border='1px solid silver', template='deck_template')

        tc=bc.tabContainer(region='center')
        tc.contentPane(title='Cards',datapath='#FORM').plainTableHandler(table='kftm.deck_card', condition='$deck_id=:deck_id', condition_deck_id='^#FORM.record.deck_id', viewResource='ViewFromDeck')
        tc.contentPane(title='Notes',datapath='#FORM.record').simpleTextArea(value='^.player_notes', height='90%', width='95%', editor=True)
        

    def th_options(self):
        return dict(dialog_height='600px', dialog_width='800px',
            defaultPrompt=dict(title='Add deck',
                                      fields=[dict(tag='remoteSelect',
                                                  value='^.deck_id',width='25em',lbl='Search new deck', auxColumns='status,auth_tags',
                                                  method='deckSelectRpc', 
                                                  validate_notnull=True),
                                                  dict(value='^.short_name', width='25em', lbl='Short name', validate_notnull=True)], 
                                                  doSave=True))

