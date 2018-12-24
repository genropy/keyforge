from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrbag import Bag
import requests
from dateutil import rrule, relativedelta
from decimal import Decimal
from gnr.core.gnrdecorator import public_method

class DeckImporter(BaseComponent):

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
