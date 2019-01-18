# encoding: utf-8

import requests
from gnr.core.gnrbag import Bag
from gnr.core.gnrlang import getUuid
from gnr.core.gnrdecorator import public_method


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('deck',pkey='kf_id',name_long='Deck',name_plural='Decks',caption_field='name', rowcaption='$short_name')
        self.sysFields(tbl,id=False)
        tbl.column('kf_id',size='36',name_long='KF ID',name_short='ID',unique=True,indexed=True)
        tbl.column('name',size=':100',name_long='Deck name',name_short='Name',unique=True,indexed=True)
        tbl.column('short_name',size=':30',name_long='Short name',name_short='Short name',unique=True,indexed=True)
        tbl.column('expansion',dtype='I',name_long='Expansion',name_short='Expansion')
        tbl.column('power_level',dtype='I',name_long='Power level',name_short='Power level')
        tbl.column('chains',dtype='I',name_long='Chains',name_short='Chains')
        tbl.column('deck_traits_bag', dtype='X', name_long='Deck traits bag')
        tbl.column('deck_traits', name_long='Traits')
        tbl.column('deck_triggers_bag', dtype='X', name_long='Deck triggers bag')
        tbl.column('deck_triggers', name_long='Triggers')
        tbl.column('houses', name_long='Houses')
        tbl.column('n_creatures', dtype='I', name_long='N.Creatures')
        tbl.column('n_artifacts', dtype='I', name_long='N.Artifacts')
        tbl.column('n_actions',  dtype='I', name_long='N.Actions')
        tbl.column('n_upgrades',  dtype='I', name_long='N.Upgrades')
        tbl.column('tot_amber', dtype='I', name_long='Tot.Amber')
        tbl.column('avg_amber', dtype='N', name_long='Avg.Amber')
        tbl.column('avg_cr_power', dtype='N', name_long='Avg.Power')
        tbl.column('avg_cr_armor', dtype='N', name_long='Avg.Armor')

        tbl.column('tot_matches', dtype = 'L', name_long = 'N.Matches')
        tbl.column('won_matches', dtype = 'L', name_long = 'N.Won')
        tbl.column('lost_matches', dtype = 'L', name_long = 'N.Lost')
        tbl.column('tot_keys', dtype = 'L', name_long = 'Tot.Keys')
        tbl.column('external_site_url', name_long = 'External Site URL')

        tbl.aliasColumn('players', '@players.player', name_long='Players')
        tbl.aliasColumn('cards', '@cards.card_title', name_long='Cards')

        tbl.formulaColumn('victory_rate', 'CASE WHEN $tot_matches>0 THEN CAST ($won_matches AS FLOAT ) / CAST ($tot_matches AS FLOAT) ELSE 0 END', dtype = 'N', name_long = 'Victory rate')
        tbl.formulaColumn('avg_keys', 'CASE WHEN $tot_matches>0 THEN CAST( $tot_keys AS FLOAT) /CAST ($tot_matches AS FLOAT) ELSE 0 END', dtype = 'N', name_long = 'Avg Keys')
        tbl.formulaColumn('fast_ambers', select=dict(columns='SUM(@card_id.fast_amber)', table='kftm.deck_card', where='$deck_id=#THIS.kf_id'), dtype='N', name_long='Fast ambers')
        tbl.formulaColumn('n_rares', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.rarity='rare'"), dtype='N',  name_long='N.Rares')

        tbl.formulaColumn('n_uncommon', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.rarity='uncommon'"), dtype='N',  name_long='N.Uncommon')
        #tbl.formulaColumn('n_amber_control', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.func_tags='uncommon'"), dtype='N',  name_long='N.Uncommon')

        tbl.formulaColumn('n_mavericks', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.is_maverick IS TRUE"), dtype='N',  name_long='N.Maverick')
        tbl.formulaColumn('n_super', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.super IS TRUE"), dtype='N',  name_long='N.Super')
        tbl.formulaColumn('n_situational', select=dict(columns='COUNT(*)',  table='kftm.deck_card', where="$deck_id=#THIS.kf_id AND @card_id.situational IS TRUE"), dtype='N',  name_long='N.Sit')

        tbl.formulaColumn('frm_tot_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$win_deck_id=#THIS.kf_id OR $lose_deck_id=#THIS.kf_id'), dtype='L', name_long='Nr.Matches (FRM)')
        tbl.formulaColumn('frm_won_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$win_deck_id=#THIS.kf_id'), dtype='L', name_long='Won Matches (FRM)')
        tbl.formulaColumn('frm_lost_matches', select=dict(columns='COUNT(*)', table='kftm.match', where='$lose_deck_id=#THIS.kf_id'), dtype='L', name_long='Lost Matches (FRM)')
        tbl.formulaColumn('frm_won_keys', select=dict(columns='COALESCE(SUM($win_keys),0)', table='kftm.match', where='$win_deck_id=#THIS.kf_id'), dtype='L', name_long='W Keys (FRM)')
        tbl.formulaColumn('frm_lost_keys', select=dict(columns='COALESCE(SUM($lose_keys),0)', table='kftm.match', where='$lose_deck_id=#THIS.kf_id'), dtype='L', name_long='L Keys (FRM)')
        #tbl.formulaColumn('frm_tot_keys', select='$frm_won_keys+$frm_lost_keys', dtype='L', name_long='Tot keys (FRM)')



    @public_method
    def deckSelectRpc(self,_querystring=None,_id=None,**kwargs):
        result = Bag() 
        #http://www.keyforgegame.com/api/decks/9d8204f7-dd7c-4bd0-9138-bb46ff9e800c/?links=cards
        if len(_querystring) ==36 and '-' in _querystring:
            _id=_querystring
        if _id:
            deck_data=self.getDeckById(_id=_id)['data']
        else:
            deck_data=self.getDeckByName(_querystring=_querystring)
            if deck_data:
                deck_data=deck_data['#0']
        if not deck_data:
            return None
        #print xxx
        houses=', '.join(deck_data['_links.houses'].digest('#v'))
        #for k,v in deck_data.items():
            
        result.addItem('r', None, id=deck_data['id'], name=deck_data['name'], houses=houses,_pkey=deck_data['id'], caption=deck_data['name'])
        
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

    #def getDeckById(self, _id=None):
    #    #try:
    #    if True:
    #        response=requests.get('http://www.keyforgegame.com/api/decks/%s/?links=cards' % _id)
    #        rbag= Bag()
    #        rbag.fromJson(response.json())
    #        return rbag['data']
    #    #except Exception, e:
    #    #    return Bag(dict(error=str(e)))


    def updateTotals(self, match_record):
        def cb_deck(r):
            r['tot_matches']=r['frm_tot_matches']
            r['won_matches']=r['frm_won_matches']
            r['lost_matches']=r['frm_lost_matches']
            r['tot_keys']=r['frm_won_keys']+r['frm_lost_keys']

        self.batchUpdate(cb_deck,
                          columns='*,$frm_tot_matches,$frm_won_matches,$frm_lost_matches,$frm_won_keys,$frm_lost_keys',
                          where='$kf_id=:win_deck_id OR $kf_id=:lose_deck_id',
                          win_deck_id=match_record['win_deck_id'],
                          lose_deck_id=match_record['lose_deck_id'] )


    def importDeck(self, deck_id, short_name=None):
        traitsDict=self.db.table('kftm.trait').query().fetchAsDict(key='trait')
        cardTypes=self.db.table('kftm.card_type').query().fetchAsDict(key='type')
        deck_card_tbl=self.db.table('kftm.deck_card')
        print 'importDeck'
        if True:
            response_bag = self.getDeckById(deck_id)
            deck_bag = response_bag['data']
            #houses_data=response_bag.pop('_linked.houses')
            cards_data = response_bag.pop('_linked.cards')
            deck_houses=deck_bag['_links.houses']
            deck_cards=deck_bag['_links.cards']
            #self.db.table('kftm.house').importFromDeck(houses_data)
            self.db.table('kftm.card').importFromDeck(cards_data, traitsDict=traitsDict)
            deck_record = dict(deck_bag)
            deck_record['kf_id']=deck_record.pop('id')
            deck_record['houses']=', '.join(deck_houses.values())
            deck_record['short_name']=short_name
            self.insert(deck_record)
            deck_houses_records=[dict(id=getUuid(), deck_id=deck_id, house=h) for h in deck_houses.values()]
            deck_cards_records=[dict(id=getUuid(), deck_id=deck_id, card_id=h) for h in deck_cards.values()]
            self.db.table('kftm.deck_house').insertMany(deck_houses_records)
            deck_card_tbl.insertMany(deck_cards_records)
            deck_traits = self.db.table('kftm.card_trait').query(where='$card_id IN :deck_cards', columns='COUNT(*),$trait', deck_cards=deck_cards.values(), distinct='$trait', group_by='$trait').fetch()
            deck_traits_bag = Bag()
            deck_triggers_bag= Bag()
            deck_triggers_list=[]
            deck_traits_list=[]
            old_deck_record=dict(deck_record)
            for dt in deck_traits:
                deck_traits_bag.addItem('t',None,trait=dt['trait'], n=dt['COUNT___'])
                deck_traits_list.append('%s (%s)' % (dt['trait'], dt['COUNT___']))
            deck_record['deck_traits_bag']=deck_traits_bag
            deck_record['deck_traits']=', '.join(deck_traits_list)

            deck_triggers = self.db.table('kftm.card_trigger').query(where='$card_id IN :deck_cards', columns='COUNT(*),$trigger', deck_cards=deck_cards.values(), group_by='$trigger').fetch()
            for dt in deck_triggers:
                deck_triggers_bag.addItem('trg',None,trait=dt['trigger'], n=dt['COUNT___'])
                deck_triggers_list.append('%s (%s)' % (dt['trigger'], dt['COUNT___']))
            deck_record['deck_triggers_bag']=deck_traits_bag
            deck_record['deck_triggers']=', '.join(deck_triggers_list)
            for t in cardTypes.keys():
                count=deck_card_tbl.query(columns='COUNT(*) AS cnt, AVG($card_power) AS avg_power, AVG($card_armor) AS avg_armor', where='@card_id.card_type=:ctype AND $deck_id=:deck_id', deck_id=deck_record['kf_id'] ,ctype=t).fetch()
                if count:
                    deck_record['n_%ss' % t.lower()]=count[0]['cnt']
                if t =='Creature':
                    deck_record['avg_cr_power']=count[0]['avg_power']
                    deck_record['avg_cr_armor']=count[0]['avg_armor']

            amber_counts = deck_card_tbl.query(columns='SUM($card_amber) AS tot_amber, AVG($card_amber) AS avg_amber', where='$deck_id=:deck_id', deck_id=deck_record['kf_id']).fetch()[0]
            deck_record['tot_amber']=amber_counts['tot_amber']
            deck_record['avg_amber']=amber_counts['avg_amber']
            self.update(deck_record, old_deck_record)
        #except Exception, e:
        #    return Bag(dict(error=str(e)))
#


    def getDeckById(self, _id=None):
        response=requests.get('http://www.keyforgegame.com/api/decks/%s/?links=cards' % _id)
        rbag= Bag()
        rbag.fromJson(response.json())
        return rbag
