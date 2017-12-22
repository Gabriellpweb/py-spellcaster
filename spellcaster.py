from enchant import request_pwl_dict


class SpellCaster:

    def __init__(self, locale):
        self.pwl = learn_locale(locale)

    def cast_suggest_spell(self, term):

        replacement = term

        if not self.pwl:
            return False

        words = term.split(' ')
        suggestions = []

        for word in words:
            suggestion = self.pwl.suggest(word)

            suggestions.append({
                'word': word,
                'suggest': suggestion
            })

            if suggestion.__len__() > 0:
                replacement = replacement.replace(word, suggestion[0])

        return {'term': term, 'replacement': replacement, 'suggestions': suggestions}


def learn_locale(locale):
    pwl = None
    if locale == 'pt_br':
        pwl = request_pwl_dict("pt_br.txt")
    return pwl
