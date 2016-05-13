import sys
sys.path.append("libs/anubad/src")

import core
from libs.anubad.src import config
from libs.anubad_wrapper import AnubadWrapper

class EnToNp:
    def __init__(self):
        rc = config.RC()
        rc.read('config/anubad_core.cnf')
        rc.load()
        core.load_from_config(rc)
        self.glossary = core.Glossary
        self.anubad_wrapper = AnubadWrapper()

    def search(self, phrase):
        raw_result = self.glossary.search(phrase)
        return self.anubad_wrapper.get_all_items(raw_result)

    def json_search(self, phrase):
        raw_result = self.glossary.search(phrase)
        return self.anubad_wrapper.get_json_dumps(raw_result)
