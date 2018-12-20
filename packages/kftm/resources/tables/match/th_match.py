#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        r.fieldcell('date', width='7em')
        r.fieldcell('win_player', width='14em')
        r.fieldcell('lose_player', width='14em')
        r.fieldcell('decks_title')
        r.fieldcell('result')
        r.fieldcell('lose_chains')
        r.fieldcell('lose_keys')
    def th_order(self):
        return 'date'

    def th_query(self):
        return dict(column='id', op='contains', val='')

    def th_options(self):
        return dict(widget='dialog')


class ViewFromPlayer(View):

    def th_order(self):
        return 'date'

    def th_options(self):
        return dict(widget='dialog')

    def th_top_custom(self,top):
        top.slotToolbar('*,sections@wonlost,*',childname='subbar',_position='<bar')
 
    def th_sections_wonlost(self):
        
        result = [dict(code='all',caption='All'),
                  dict(code='won', caption='Won', condition='$win_player=:env_curr_player'),
                  dict(code='lost', caption='Lost', condition='$lose_player=:env_curr_player')]
        return result


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record

        fb = pane.div(margin_right='10px').formbuilder(cols=4, border_spacing='4px', colswidth='auto', fld_width='100%', width='100%')
        fb.field('date', width='7em')
        fb.div(colspan=3)
        fb.field('win_player', colspan=2)
        fb.field('lose_player',  colspan=2)
        fb.field('win_deck' ,colspan=4, auxColumns='$short_name,$houses')
        fb.field('lose_deck', colspan=4,  auxColumns='$short_name,$houses')
        fb.field('win_chains',lbl='W.Chains', width='5em')
        fb.field('win_keys', width='5em')
        fb.field('win_chains',lbl='L.Chains', width='5em')
        fb.field('lose_keys', width='5em')




    def th_options(self):
        return dict(dialog_height='160px', dialog_width='620px', modal=True)
