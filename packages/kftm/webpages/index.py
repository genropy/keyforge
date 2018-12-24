# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    css_requires='bau'
    py_requires = 'plainindex,th/th:TableHandler,deck_importer:DeckImporter'


    def index_player(self,root,**kwargs):
        main_bc = root.borderContainer(region='center', background_color='rgba(121 39 35)')
        tc=main_bc.tabContainer(region='center', margin='15px')
        tc.contentPane(title='My profile', background_color='white').thFormHandler(datapath='playerpage',formId='formPlayer',
                                    formResource='PlayerPage',table='kftm.player',
                                startKey=self.rootenv['player'],
                                margin='2px')

        tc.contentPane(title='Matches & Results', background_color='white').remote('resultsPane',_waitingMessage=True)
        tc.contentPane(title='Decks', background_color='white').remote(self.decksPane,_waitingMessage=True)
        self.prepareBottom(main_bc)

    @public_method
    def resultsPane(self, pane,**kwargs):
        pane.dialogTableHandler(datapath='all_matches',
                                nodeId='all_matches', 
                                table='kftm.match',
                                extendedQuery=True, virtualStore=True,
                                view_store__onBuilt=True,
                                viewResource='ViewGeneral')
    @public_method
    def decksPane(self, pane,**kwargs):
        pane.plainTableHandler(datapath='all_decks',
                               nodeId='all_decks', 
                               table='kftm.deck',
                               extendedQuery=True,
                               virtualStore=True,
                               view_store__onBuilt=True,
                               viewResource='View')

        