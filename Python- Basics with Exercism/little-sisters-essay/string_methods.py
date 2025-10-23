"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    title2 = title.title()
    return title2


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    zdanie = sentence.endswith(".")
    return zdanie
check_sentence_ending("czy to działa.")

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    zdanie = sentence.strip("   ")
    return zdanie

#print(clean_up_spacing(" I like to go on hikes with my dog.  "))


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    zdanie = sentence.replace(old_word,new_word)
    return zdanie

#print(replace_word_choice("I bake good cakes.", "good", "amazing"))

