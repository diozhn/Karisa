from commands.commands import bot
from settings import TOKEN
from keep_alive import keep_alive

if __name__ in '__main__':
  print(
    r'''
      Iniciando sistema... Karisa rodando!
    '''
  )
keep_alive()
bot.run(TOKEN)
