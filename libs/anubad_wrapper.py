import collections
from json import dumps as json_dumps
from operator import itemgetter

class AnubadWrapper:
    def get_item(self, raw_result):
        """
        >>> root._view_item(instance, src, [1, "sunday" "[सन्डे] n(आइतबार) #time"])
        >>> print(GUI.clips)
        ['आइतबार', 'सन्डे'],
        """
        (instance, src, row)          = raw_result
        (distance, word, parsed_info) = row

        # TODO: i am not sure of it yet
        if type(distance)==tuple : distance=distance[0]
    
        meta                          = (instance, src, distance)
        parsed_result_for_word        = collections.defaultdict(list)

        transliterate                 =""
        for key, val in parsed_info:
            if   key == "_transliterate": transliterate = val; continue
            elif key[0] == "_" or val == "": continue
            parsed_result_for_word[key].append(val)

        word_result = { 'distance':      distance,
                        'word':          word,
                        'transliterate': transliterate,
                        'result':        dict(parsed_result_for_word)
        }

        return word_result

    def get_all_items( self, raw_results ):
        parsed_result = dict(exact= None, fuzzy= [])
        parsed_result['exact'] = self.get_item(raw_results[0][0])

        for raw_r in raw_results[1]:
            parsed_result['fuzzy'].append(self.get_item(raw_r))

        parsed_result['fuzzy'].sort(key=itemgetter('distance'))
        return parsed_result

    def get_json_dumps( self, raw_results):
        json_result = json_dumps(self.get_all_items(raw_results), ensure_ascii=False)
        return json_result
