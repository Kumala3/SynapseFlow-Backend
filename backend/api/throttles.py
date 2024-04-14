from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class FaqQuestionAnonRateThrottle(AnonRateThrottle):
    scope = "faq_question_anon_user"


class FaqQuestionRateThrottle(UserRateThrottle):
    scope = "faq_question_user"
