# Copyright (c) 2018 Presto Labs Pte. Ltd.
# Author: xguo

import os

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from absl import flags
from requests import Response
from googletrans import Translator
import pickleshare

from tornadorpc.json import JSONRPCHandler


flags.DEFINE_integer(
    'port',
    56012,
    'Port of the dashboard web service.'
)


class TransHandler(JSONRPCHandler):
  def initialize(self):
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



class MainHandler(JSONRPCHandler):
  def get(self):
    self.write("Hello , ADD\n")


def create_webapp(gateway, port):
  settings = dict(
      template_path=os.path.join(os.path.dirname(__file__), "template"),
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      debug=False
  )
  application = Application(
      [(r'/', OrderHandler, dict(gateway=gateway))],
      **settings
  )
  application.listen(port)


if __name__ == "__main__":
  private_client = npc.BithumbNativePrivateClient(key_file=, max_connections=1, use_async=True)
  app = Application([('/', OrderHandler)], **settings)
  app.listen(8888)
  IOLoop.current().start()
