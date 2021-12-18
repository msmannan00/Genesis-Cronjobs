from cronjob_manager.constants.strings import STRINGS

class word_model:
    m_word = STRINGS.S_EMPTY
    m_user_generated = False
    m_score = 0
    m_last_update = None

    def __init__(self, p_word, p_user_generated, p_score, p_last_update):
        self.m_word = p_word
        self.m_user_generated = p_user_generated
        self.m_score = p_score
        self.m_last_update = p_last_update
