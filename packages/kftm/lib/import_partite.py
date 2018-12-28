# encoding: utf-8

from gnr.app.gnrapp import GnrApp
from gnr.core.gnrbag import Bag
from datetime import date,datetime
import csv

class MatchesImporter(object):


    #def __init__(self,db=None, filepath=None):
    #    self.db=db
    #    self.reader = XlsReader(filepath)
    #    self.tournament_tbl=self.db.table('kftm.tournament')
    #    self.deck_tbl=self.db.table('kftm.deck')
    #    self.player_tbl=self.db.table('kftm.player')
    #    self.match_tbl=self.db.table('kftm.match')
#
    #    self.deckDict = self.deck_tbl.query().fetchAsDict(key='short_name')
    #    self.playersDict = self.player_tbl.query().fetchAsDict(key='nickname')
    #    self.tournament_id= self.tournament_tbl.query().fetch()[0]['id']

    def __init__(self,db=None, filepath=None):
        self.db=db
        csv_file = open(filepath, mode='r')
        self.csv_reader = csv.DictReader(csv_file, delimiter=';')
        self.tournament_tbl=self.db.table('kftm.tournament')
        self.deck_tbl=self.db.table('kftm.deck')
        self.player_tbl=self.db.table('kftm.player')
        self.match_tbl=self.db.table('kftm.match')

        self.deckDict = self.deck_tbl.query().fetchAsDict(key='short_name')
        self.playersDict = self.player_tbl.query().fetchAsDict(key='nickname')
        self.tournament_id= self.tournament_tbl.query().fetch()[0]['id']
        


    def populateTables(self):
        for row in self.csv_reader:
            self.insertRecordsFromCsvRow(row)


    
    def insertRecordsFromCsvRow(self, row):
        vincitore=row['Vincitore']
        perdente = row['Perdente']
        d_w=row['Mvincitore'].strip()
        d_l=row['Mperdente'].strip()
        win_player=self.playersDict[vincitore]['nickname']
        lose_player=self.playersDict[perdente]['nickname']
        if d_w not in self.deckDict:
            win_deck=None
        else:
            win_deck=self.deckDict[d_w]['kf_id']
        
        if d_l not in self.deckDict:
            lose_deck=None
        else:
            lose_deck=self.deckDict[d_l]['kf_id']
        
        
        tournament_id = self.tournament_id if row['Torneo'] == '1° di prova' else None
        match_record=dict(win_player=win_player,
                          lose_player=lose_player,
                          win_deck_id=win_deck,
                          lose_deck_id=lose_deck,
                          win_keys=row['Kvincitore'] or 0,
                          lose_keys=row['Kperdente'] or 0,
                          win_chains=row['Vincoli'] or 0,
                          online=True if row['Crucible'] == 'Y' else None,
                          tournament_id=tournament_id)

        self.match_tbl.insert(match_record)


if __name__ == '__main__':
    db = GnrApp('keyforge').db
    filepath='risultati.csv'
    importer = MatchesImporter(db, filepath)
    importer.populateTables()
    db.commit()
    print 'fatto e committato'
