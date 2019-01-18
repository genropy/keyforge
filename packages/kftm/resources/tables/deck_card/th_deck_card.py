#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class ViewFromCard(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('deck_name', width='33em')
        r.fieldcell('deck_players', width='100%')
        #r.fieldcell('card_id')

    def th_order(self):
        return 'deck_id'

    def th_query(self):
        return dict(column='id', op='contains', val='')

class ViewFromDeck(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('card_title', name='Title', width='16em')
        r.fieldcell('card_type', name='Type', width='6em')
        r.fieldcell('card_house', name='House', width='6em')
        r.fieldcell('card_amber', width='5em')
        r.fieldcell('card_power',  width='5em')
        r.fieldcell('card_armor',  width='5em')
        #r.fieldcell('card_text', width='100%')


        #r.fieldcell('card_id')

    def th_order(self):
        return 'card_house'

    def th_query(self):
        return dict(column='id', op='contains', val='')

    def th_top_custom(self,top):
        top.slotToolbar('*,sections@card_type,*',childname='subbar',_position='<bar')

    def th_sections_card_type(self):
        types = self.db.table('kftm.card_type').query().fetch()
        result = [dict(code='all',caption='All')]
        for h in types:
            result.append(dict(code=h['type'], caption=h['type'], condition='$card_type=:type', condition_type=h['type']))
        return result



class Form(BaseComponent):

    def th_form(self, form):
        tc = form.center.tabContainer(datapath='#FORM')
        self.cardTab(tc.borderContainer(title='Card', datapath='.record'))
        tc.contentPane(title='Card external page', region='center').iframe(src='^#FORM.record.@card_id.external_site_url', width='100%')

    def cardTab(self, bc):
        left=bc.contentPane(region='left', width='205px')
        left.img(src='^.@card_id.front_image', width='200px', margin='2px')
        fb=bc.contentPane(region='center', title='Card data',margin='10px').formbuilder(cols=2, border_spacing='4px', datapath='.@card_id', table='kftm.card')
        fb.field('external_site_url', lbl='Ext.URL', colspan=2, width='90%')
        fb.field('super' , label='Super card', lbl='')
        fb.field('situational' , label='Situational', lbl='')
        fb.div('',lbl='Functions', colspan=2)
        fb.field('func_tags', tag='checkBoxText',
                        colspan=2, cols=2,
                        caption_field='description',
                        table='kftm.func_tag')




    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
