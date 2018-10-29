import os
import yaml

import itchat

from sh import bash
from googletrans import Translator


class Translate(object):
  def __init__(self):
    self._translator = Translator()

  def _translate(text):
    text_en = self._translator.translate(text).text
    return text_en

  def translate(text):
    text_list = text.split('\n')
    res = []
    for line in text_list:
      line_en = self._translate(line)
      res.append(line_en)
      time.sleep(1)
      return '\n'.join(res)


@itchat.msg_register(itchat.content.TEXT)
def msg_executor(msg):
    if msg['ToUserName'] != 'filehelper':
      return

    command = msg['Text']
    output = 'error'
    try:
      output = subprocess.check_output(command, shell=True)
      output = output.decode()
    except Exception:
      pass

    itchat.send(output, 'filehelper')


def main():
  itchat.auto_login(True)
  itchat.run()


if __name__ == '__main__':
  main()
