#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('card_title', width='18em')
        r.fieldcell('house', width='7em')
        r.fieldcell('card_type', name='Type', width='7em')
        r.fieldcell('card_text_only', name='Card text', width='100%')
        r.fieldcell('traits', width='12em')
        r.fieldcell('amber',name='AE')
        r.fieldcell('power', name='PW')
        r.fieldcell('armor', name='AR')
        r.fieldcell('rarity', width='7em')
        #r.fieldcell('card_number')
        #r.fieldcell('expansion')
        r.fieldcell('is_maverick', name='Mav.', width='4em')
        #r.fieldcell('flavor_text', width='40%')

    def th_order(self):
        return 'house,card_type'

    def th_query(self):
        return dict(column='card_title', op='contains', val='')

    def th_top_custom(self,top):
        top.slotToolbar('5,sections@house,*,sections@card_type,*,sections@rarity,5',childname='subbar',_position='<bar')
 
    def th_options(self):
        return dict(widget='dialog')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer( datapath='#FORM.record')
        bc.contentPane(region='left', width='210px', title='Image',margin='8px').img(src='^.front_image', width='200px', margin='2px')
        tc=bc.tabContainer(region='center')
        fb = tc.contentPane(region='center', title='Card data',margin='10px').formbuilder(cols=3, border_spacing='4px', readOnly=True, fld_readOnly=True)
        fb.field('card_title' , lbl='Title', colspan=3, width='39em')
        fb.field('house' ,lbl='House', width='8em')
        fb.field('card_type' ,lbl='Type', width='8em')
        fb.field('rarity', width='8em')
        fb.field('traits', colspan=3,  width='39em')
        fb.field('amber' ,width='4em')
        fb.field('power' ,width='4em')
        fb.field('armor' ,width='4em')
        fb.field('card_text_only', colspan=3, width='39em', tag='simpleTextArea', height='12ex', lbl='Text')
        fb.field('flavor_text', colspan=3, width='39em', tag='simpleTextArea', height='12ex')
        self.functionTags(tc.contentPane(title='Function tags', datapath='#FORM.record'))
        tc.contentPane(title='Decks', datapath='#FORM').plainTableHandler(relation='@decks',margin='2px', viewResource='ViewFromCard')
    
    def functionTags(self, pane):
        fb = pane.formbuilder(cols=1, width='100%')
        fb.checkboxtext(value='^.func_tags',
                        colspan=1, cols=2,
                        caption_field='description',
                        table='kftm.func_tag')

    
    def th_options(self):
        return dict(dialog_height='370px', dialog_width='820px', modal=True)
