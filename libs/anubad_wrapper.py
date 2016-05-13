import collections

from IPython import embed

class AnubadWrapper:
    def get_item(self, raw_result):
        """
        >>> root._view_item(instance, src, [1, "sunday" "[सन्डे] n(आइतबार) #time"])
        >>> print(GUI.clips)
        ['आइतबार', 'सन्डे'],
        """
        # TODO: move it to viewer
        (instance, src, row) = raw_result
        (distance, word, parsed_info) = row
        meta = (instance, src, distance)
        parsed_result_for_word = collections.defaultdict(list)

        for key, val in parsed_info:
            parsed_result_for_word[key].append(val)
        word_result = { 'distance': distance,
                        'word': word,
                        'result': parsed_result_for_word}
        return word_result

    def get_all_items( self, raw_results ):
        parsed_result = dict(exact= None, fuzzy= [])
        parsed_result['exact'] = self.get_item(raw_results[0][0])

        for raw_r in raw_results[1]:
            parsed_result['fuzzy'].append(self.get_item(raw_r))

        return parsed_result
