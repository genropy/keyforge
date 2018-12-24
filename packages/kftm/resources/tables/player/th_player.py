#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag


class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nickname')
        r.fieldcell('firstname')
        r.fieldcell('lastname')

    def th_order(self):
        return 'nickname'

    def th_options(self):
        return dict(virtualStore=False)

class Form(BaseComponent):
    py_requires='deck_importer:DeckImporter'

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.topBc(bc.borderContainer(region='top', height='100px'))
        

        centerTc = bc.tabContainer(region='center', margin='5px')
        self.playerDecksPane(centerTc.contentPane(title='Decks'))
        self.playerResultsPane(centerTc.contentPane(title='Results'))

    def topBc(self, bc):
        player_form= bc.contentPane(region='left', datapath='.record').div(margin_right='10px')
        fb = player_form.formbuilder(cols=1, border_spacing='4px')
        fb.field('nickname')
        fb.field('firstname')
        fb.field('lastname')

        bc.contentPane(region='center', datapath='.record').linkerBox('user_id',label='User',formUrl='/adm/user_page',dialog_height='400px',
                        dialog_width='650px',
                        default_firstname='=#FORM.record.firstname',
                        default_lastname='=#FORM.record.lastname',
                        default_username='=#FORM.record.nickname',
                        newRecordOnly=False,
                        margin='2px')

    def playerResultsPane(self, pane):
        pane.plainTableHandler(table='kftm.match', condition='$win_player=:player OR $lose_player=:player',
                                condition_player='^#FORM.pkey',
                                nodeId='player_matches',
                                viewResource='ViewFromPlayer',
                                formResource='Form',
                                title='My Results')

    def playerDecksPane(self, pane):
        pane.dialogTableHandler(relation='@decks',
                                viewResource='ViewFromPlayer', title='My Decks')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


class PlayerPage(Form):
    py_requires='deck_importer:DeckImporter'

    def th_options(self):
        return dict(showtoolbar=False,autoSave=True)

    def topBc(self, bc):
        player_form= bc.contentPane(region='center', datapath='.record', width='350px')
        fb = player_form.formbuilder(cols=1, border_spacing='4px')
        fb.field('nickname')
        fb.field('firstname')
        fb.field('lastname')
        fb.textbox(value='^.@user_id.md5pwd', type='password', lbl='Password')
        