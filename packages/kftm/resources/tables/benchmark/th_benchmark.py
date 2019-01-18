#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag


class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('player')
        r.fieldcell('title')
        r.fieldcell('notes')

    def th_order(self):
        return 'title'

    def th_options(self):
        return dict(virtualStore=False)

class Form(BaseComponent):
    py_requires='deck_importer:DeckImporter'


    def th_form(self, form):
        bc = form.center.borderContainer()
        self.topBc(bc.contentPane(region='top', height='100px', datapath='#FORM.record'))
        self.benchmarkDecksPane(bc.contentPane(title='Decks', datapath='#FORM', region='center'))

    def topBc(self, pane):
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('player')
        fb.field('title')
        fb.field('notes')

    def benchmarkDecksPane(self, pane):
        pane.dialogTableHandler(relation='@decks',
                                viewResource='ViewFromBenchmark', title='Benchmark')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

