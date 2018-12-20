# encoding: utf-8
import re

TRIGGER_EXP = re.compile(r"""(Play|Omni|Reap|Before Fight|Fight|Destroyred)?/?(Play|Omni|Reap|Before Fight|Fight|Destroyred)?/?(Play|Omni|Reap|Before Fight|Fight|Destroyred)?/?(Play|Omni|Reap|Before Fight|Fight|Destroyred)?:(?:.*)""")


class Table(object):


    def config_db(self,pkg):
        tbl =  pkg.table('card',pkey='kf_id',name_long='Card',name_plural='Cards',caption_field='card_title', rowcaption='$card_title')
        tbl.column('kf_id',size='36',name_long='KF ID',name_short='KF ID',unique=True,indexed=True)
        tbl.column('card_title',name_long='Card title',name_short='Title',unique=True,indexed=True)
        tbl.column('house',size=':7',name_long='House',name_short='House',indexed=True).relation('house.house',relation_name='cards', mode='foreignkey', onDelete='raise')
        tbl.column('card_type',size=':20',name_long='Card Type',name_short='Card Type',indexed=True).relation('card_type.type',relation_name='cards')
        tbl.column('front_image',size=':80',name_long='Front image',name_short='Image')
        tbl.column('card_text',name_long='Card Text',name_short='Text')
        tbl.column('card_text_only',name_long='Card Text (txt-only)')
        tbl.column('traits',name_long='Traits',name_short='Traits')
        tbl.column('amber',dtype='I',name_long='Amber',name_short='Amber')
        tbl.column('power',dtype='I',name_long='Power',name_short='Power')
        tbl.column('armor',dtype='I',name_long='Armor',name_short='Armor')
        tbl.column('rarity',size=':20',name_long='Rarity',name_short='Rarity').relation('rarity.rarity',relation_name='cards')
        tbl.column('card_number',dtype='I',name_long='Card Number',name_short='Card Number')
        tbl.column('expansion',dtype='I',name_long='Expansion',name_short='Expansion')
        tbl.column('is_maverick',dtype='B',name_long='Is Maverick',name_short='Maverick')
        tbl.column('flavor_text',name_long='Flavor text',name_short='Flavor text')


    def importFromDeck(self, data, traitsDict=None):
        card_trigger_tbl=self.db.table('kftm.card_trigger')
        card_trait_tbl = self.db.table('kftm.card_trait')
        trait_tbl=self.db.table('kftm.trait')
        pkeys = data.digest('#v.id')
        existings = self.query(where='$kf_id IN :pkeys', pkeys=pkeys, columns='$kf_id').fetchAsDict(key='kf_id')
        for c in data.values():
            if c['id'] not in existings:
                c['kf_id']=c.pop('id')
                c['card_text']=c['card_text'].replace('\x0b',' ')
                if c['flavor_text']:
                    c['flavor_text']=c['flavor_text'].replace('\x0b',' ')
                c['card_text_only'] = c['card_text'].replace('<A>','AE').replace('<D>','DMG')
                self.insert(dict(c))
                m=re.match(TRIGGER_EXP,c['card_text_only'])
                if m:
                    for g in m.groups():
                        if g:
                            card_trigger_tbl.insert(dict(card_id=c['kf_id'], trigger=g))
                if c['traits']:
                    sep='\xe2\x80\xa2'
                    traits=c['traits'].replace(' ','')
                    traits_list=traits.split(sep)
                    for t in  traits_list:
                        if not t in traitsDict:
                            trait_tbl.insert(dict(trait=t))
                            traitsDict[t]=t
                        card_trait_tbl.insert(dict(card_id=c['kf_id'], trait=t))


        

