import time
import traceback
import itchat
from googletrans import Translator


class Translate(object):
  def __init__(self):
    self._translator = Translator()

  def _translate(self, text):
    text_en = self._translator.translate(text).text
    return text_en

  def translate(self, text):
    text_list = text.split('\n')
    res = []
    for line in text_list:
      line_en = self._translate(line)
      res.append(line_en)
      time.sleep(1)
      return '\n'.join(res)


tran = Translate()


@itchat.msg_register(itchat.content.TEXT)
def msg_executor(msg):
    if msg['ToUserName'] != 'filehelper':
      return

    text = msg['Text']
    # noinspection PyBroadException
    try:
      output = tran.translate(text)
    except Exception:
      output = traceback.format_exc()

    itchat.send(output, 'filehelper')


def main():
  itchat.auto_login(True, enableCmdQR=-3)
  itchat.run()


if __name__ == '__main__':
  main()
