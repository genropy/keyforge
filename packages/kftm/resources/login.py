from gnr.web.gnrbaseclasses import BaseComponent

class LoginComponent(BaseComponent):

    def onUserSelected(self,avatar,data):
        player = self.db.table('adm.user').readColumns(pkey=avatar.user_id,columns='@player.nickname')
        data.setItem('player',player)
        if player:
            data['custom_index'] = 'player'
            return
