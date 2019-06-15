from djchoices import DjangoChoices, ChoiceItem


class Language(DjangoChoices):
    ENGLISH = ChoiceItem("English")
    INDONESIAN = ChoiceItem("Indonesian")


class Currency(DjangoChoices):
    USD = ChoiceItem("USD")
    IDR = ChoiceItem("IDR")
