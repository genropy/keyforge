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
        r.fieldcell('card_text', width='100%')


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
        pane = form.record
        pane.img(src='^.@card_id.front_image', width='200px', margin='2px')
        #fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('card_id' )

    #def th_form(self, form):
    #        bc = form.center.borderContainer( datapath='#FORM.record')
    #    bc.contentPane(region='left', width='210px', title='Image',margin='8px').img(src='^@card_id.front_image', width='200px', margin='2px')
    #    tc=bc.tabContainer(region='center')
    #    fb = tc.contentPane(region='center', title='Card data',margin='10px').formbuilder(cols=3, border_spacing='4px', readOnly=True, fld_readOnly=True, datapath='.@card_id')
    #    #fb.field('card_title' , lbl='Title', colspan=3, width='39em')
    #    #fb.field('house' ,lbl='House', width='8em')
    #    #fb.field('card_type' ,lbl='Type', width='8em')
    #    #fb.field('rarity', width='8em')
    #    #fb.field('traits', colspan=3,  width='39em')
    #    #fb.field('amber' ,width='4em')
    #    #fb.field('power' ,width='4em')
    #    #fb.field('armor' ,width='4em')
    #    #fb.field('card_text_only', colspan=3, width='39em', tag='simpleTextArea', height='12ex', lbl='Text')
    #    #fb.field('flavor_text', colspan=3, width='39em', tag='simpleTextArea', height='12ex')
    #    self.functionTags(tc.contentPane(title='Function tags', datapath='#FORM.record'))
    #    #tc.contentPane(title='Decks', datapath='#FORM').plainTableHandler(relation='@decks',margin='2px', viewResource='ViewFromCard')
    #
    #def functionTags(self, pane):
    #    fb = pane.formbuilder(cols=1, width='100%')
    #    fb.checkboxtext(value='^.@card_id.func_tags',
    #                    colspan=1, cols=2,
    #                    caption_field='description',
    #                    table='kftm.func_tag')
#



    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
