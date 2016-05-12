import sys
sys.path.append("libs/anubad/src")

import core, libs.anubad.src.config as config

class EnToNp:
    def __init__(self):
        rc = config.RC()
        rc.read('config/anubad_core.cnf')
        rc.load()
        core.load_from_config(rc)
        self.glossary = core.Glossary

    def search(self, phrase):
        return self.glossary.search(phrase)
