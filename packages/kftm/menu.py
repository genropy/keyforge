#!/usr/bin/python
# -*- coding: UTF-8 -*-

def config(root,application=None):
    kftm = root.branch('Keyforge tournament manager')
    kftm.thpage('Decks',table='kftm.deck')
    kftm.thpage('Player friends',table='kftm.player_friend')
    kftm.thpage('Activation trigger',table='kftm.act_trigger')
    kftm.thpage('Deck houses',table='kftm.deck_house')
    kftm.thpage('Houses',table='kftm.house')
    kftm.thpage('Rarities',table='kftm.rarity')
    kftm.thpage('card_trait',table='kftm.card_trait')
    kftm.thpage('Traits',table='kftm.trait')
    kftm.thpage('Cards',table='kftm.card')
    kftm.thpage('card_type',table='kftm.card_type')
    kftm.thpage('Keyword abilities',table='kftm.keyword')
    kftm.thpage('Card triggers',table='kftm.card_trigger')
    kftm.thpage('Players',table='kftm.player')
    kftm.thpage('player_deck',table='kftm.player_deck')
    kftm.thpage('Deck cards',table='kftm.deck_card')
    kftm.thpage('Matches & Results',table='kftm.match')
    kftm.lookups('Lookup tables',lookup_manager='kftm')

