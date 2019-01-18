#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        r.fieldcell('date', width='7em')
        r.fieldcell('players_title', width='15em')
        r.fieldcell('@win_deck_id.short_name', width='10em', name='W.Deck')
        r.fieldcell('@lose_deck_id.short_name', width='10em',  name='L.Deck')
        r.fieldcell('decks_houses_title', width='100%')
        r.fieldcell('result', width='5em')
        r.fieldcell('win_chains', name='W.Ch', width='5em')
        r.fieldcell('lose_chains', name='L.Ch', width='5em')
        
    def th_order(self):
        return 'date'

    def th_query(self):
        return dict(column='id', op='contains', val='')

    def th_options(self):
        return dict(widget='dialog')

class ViewGeneral(View):

    def th_options(self):
        return dict(widget='dialog')

    def th_queryBySample(self):
        return dict(fields=[dict(field='win_player',lbl='Winner',width='15em'),
                            dict(field='lose_player',lbl='Loser',width='15em'),
                            dict(field='houses_title',lbl='Houses',width='15em')], cols=3, isDefault=True)

                          #  dict(field='classe_cliente_id', lbl='Classe',width='15em',tag='checkBoxText',
                          #          condition='$__syscode IS NULL',
                          #          op='in',table='erpy_coge.classe_cliente',popup=True)],
                          #  cols=3,isDefault=True)


    def th_top_custom(self,top):
            top.slotToolbar('*,sections@wonlost,*',childname='subbar',_position='<bar')
 
    def th_sections_wonlost(self):
        
        result = [dict(code='all',caption='All'),
                  dict(code='mine',caption='Mine', condition='$win_player=:env_player OR $lose_player=:env_player'),
                  dict(code='won', caption='Won', condition='$win_player=:env_player', condition_player='^#FORM.pkey'),
                  dict(code='lost', caption='Lost', condition='$lose_player=:env_player', condition_player='^#FORM.pkey')]
        return result



class ViewFromPlayer(View):

    def th_order(self):
        return 'date'

    def th_options(self):
        return dict(widget='dialog')

    def th_top_custom(self,top):
        top.slotToolbar('*,sections@wonlost,*',childname='subbar',_position='<bar')
 
    def th_sections_wonlost(self):
        
        result = [dict(code='all',caption='All'),
                  dict(code='won', caption='Won', condition='$win_player=:player', condition_player='^#FORM.pkey'),
                  dict(code='lost', caption='Lost', condition='$lose_player=:player', condition_player='^#FORM.pkey')]
        return result


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record

        fb = pane.div(margin_right='10px').formbuilder(cols=2, border_spacing='4px', colswidth='auto', fld_width='100%', width='100%')
        fb.field('date', width='7em')
        fb.div(colspan=3)
        fb.field('win_player', colspan=1)
        fb.field('lose_player',  colspan=1)
        fb.field('win_deck_id' ,colspan=1, auxColumns='$short_name,$houses')
        fb.field('lose_deck_id', colspan=1,  auxColumns='$short_name,$houses')
        #fb.div('Keys', colspan=2)
        fb.field('win_keys', width='5em')
        fb.field('lose_keys', width='5em')
        #fb.div('Chains', colspan=2)
        fb.field('win_chains',lbl='W.Chains', width='5em')
        fb.field('lose_chains',lbl='L.Chains', width='5em')
        




    def th_options(self):
        return dict(dialog_height='150px', dialog_width='640px', modal=True)


class ResultPage(Form):
  
    #def th_options(self):
    #    return dict(showtoolbar=False, autoSave=True)

     def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('date', width='7em')
        fb.div(colspan=3)
        fb.field('win_player', colspan=1)
        fb.field('lose_player',  colspan=1)
        fb.field('win_deck_id' ,colspan=1, auxColumns='$short_name,$houses', rowcaptiomn='$short_name')
        fb.field('lose_deck_id', colspan=1,  auxColumns='$short_name,$houses', rowcaptiomn='$short_name')
        #fb.div('Keys', colspan=2)
        fb.field('win_keys', width='5em')
        fb.field('lose_keys', width='5em')
        #fb.div('Chains', colspan=2)
        fb.field('win_chains',lbl='W.Chains', width='5em')
        fb.field('lose_chains',lbl='L.Chains', width='5em')
        fb.field('online')
        fb.field('tournament_id', lbl='Tournament', hasdownarrow=True)

        bar = form.bottom.bar.replaceSlots('savebtn','mysave_btn')
        bar.mysave_btn.button('Save and new', iconClass='fh_semaphore',
                                  action='this.form.save({destPkey:"*newrecord*"})',
                                  disabled='^#FORM.invalid')


