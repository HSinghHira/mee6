from plugin import Plugin
import logging

log = logging.getLogger('discord')

class Commands(Plugin):

    fancy_name = 'Custom Commands'

    def get_commands(self, server):
        storage = self.get_storage(server)
        commands = sorted(storage.smembers('commands'))
        cmds = []
        for command in commands:
            cmd = {
                'name': command
            }
            cmds.append(cmd)
        return cmds

    async def on_message(self, message):
        if message.author.id == self.mee6.user.id:
            return
        storage = self.get_storage(message.server)
        commands = storage.smembers('commands')
        if message.content in commands:
            log.info('{}#{}@{} >> {}'.format(
                message.author.name,
                message.author.discriminator,
                message.server.name,
                message.clean_content
            ))
            response = storage.get('command:{}'.format(message.content))
            await  self.mee6.send_message(
                message.channel,
                response
            )
