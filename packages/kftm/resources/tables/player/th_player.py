#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
import requests
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

class Page(BaseComponent):
    
    @public_method
    def deckSelectRpc(self,_querystring=None,_id=None,**kwargs):
        result = Bag() 
        #http://www.keyforgegame.com/api/decks/9d8204f7-dd7c-4bd0-9138-bb46ff9e800c/?links=cards
        
        if _id:
            deck_data=self.getDeckById(_id=_id)
        else:
            deck_data=self.getDeckByName(_querystring=_querystring)
        if not deck_data:
            return None
        for k,v in deck_data.items():
            houses=', '.join(v['_links.houses'].digest('#v'))
            result.addItem(k, None, id=v['id'], name=v['name'], houses=houses,_pkey=v['id'], caption=v['name'])
        
        return result,dict(columns='name,houses',headers='Name,Houses')

    def getDeckByName(self, _querystring=None, page_size=10):
        #try:
        _querystring=_querystring.replace('*','')
        if True:
            api_url='http://www.keyforgegame.com/api/decks/?page_size=%s&search=%s' % (page_size,_querystring)
            response=requests.get(api_url)
            rbag= Bag()
            rbag.fromJson(response.json())
            return rbag['data']
        #except Exception, e:
        #    return Bag(dict(error=str(e)))

    def getDeckById(self, _id=None):
        #try:
        if True:
            response=requests.get('http://www.keyforgegame.com/api/decks/%s/?links=cards' % _id)
            rbag= Bag()
            rbag.fromJson(response.json())
            return rbag['data']
        #except Exception, e:
        #    return Bag(dict(error=str(e)))

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        topBc = bc.borderContainer(region='top', height='130px')
        player_form= topBc.contentPane(region='left', datapath='.record', width='350px').div(margin_right='10px')
        fb = player_form.formbuilder(cols=1, border_spacing='4px')
        fb.field('nickname')
        fb.field('firstname')
        fb.field('lastname')

        topBc.contentPane(region='center', datapath='.record').linkerBox('user_id',label='User',formUrl='/adm/user_page',dialog_height='400px',
                        dialog_width='650px',
                        default_firstname='=#FORM.record.firstname',
                        default_lastname='=#FORM.record.lastname',
                        default_username='=#FORM.record.nickname',
                        newRecordOnly=False,
                        margin='2px')

        centerTc = bc.tabContainer(region='center')
        self.decksPane(centerTc.contentPane(title='Decks'))
        self.resultsPane(centerTc.contentPane(title='Results'))

    def resultsPane(self, pane):
        pane.plainTableHandler(table='kftm.match', condition='$win_player=:player OR $lose_player=:player',
                                condition_player='^#FORM.pkey',
                                viewResource='ViewFromPlayer', formResource='Form',
                                title='Results')

    def decksPane(self, pane):
        pane.dialogTableHandler(relation='@decks',
                                viewResource='ViewFromPlayer', title='Decks')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

    @public_method
    def th_onLoading(self,record,newrecord,loadingParameters,recInfo):
        if not newrecord:
            player_nickname = record['nickname']
        else:
            player_nickname = None
        with self.pageStore() as store:
            store.setItem('dbenv.curr_player', player_nickname)
