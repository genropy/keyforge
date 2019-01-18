#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title', edit=True)
        r.fieldcell('deck_one_id', edit=True)
        r.fieldcell('deck_two_id', edit=True)
        r.fieldcell('instructions', edit=True)
        r.fieldcell('suggested_by')

    def th_order(self):
        return 'deck_id'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('deck_id' )
        fb.field('house' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
