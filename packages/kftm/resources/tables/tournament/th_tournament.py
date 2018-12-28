#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title')
        r.fieldcell('long_description')
        r.fieldcell('tournament_type')
        r.fieldcell('date_start')
        r.fieldcell('date_end')



    def th_order(self):
        return 'type'

    def th_query(self):
        return dict(column='title', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('title')
        fb.field('long_description')
        fb.field('tournament_type')
        fb.field('date_start')
        fb.field('date_end')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
