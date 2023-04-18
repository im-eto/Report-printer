import pytest
from project import validate, data_import
from pdf import write_pdf

def test_validate():

    dictionary = [{'NAME' : 123, 'PERSON': 123}]

    assert validate(dictionary) == True

    dictionary = [{'PERSON': 1234, 'FILE': 1234}]

    assert validate(dictionary) == False

def test_data_import():

    with pytest.raises(SystemExit):
        data_import('test.test')

    assert data_import('test.csv') == [{'NAME': 'Heinrich', 'LEVEL': 'AS', 'TUTOR': 'Sanri', 'HONESTY': 'yes', 'PERSEVERANCE': 'yes', 'LOYALTY': 'yes', 'COMPASSION': 'yes', 'MATH': 'A', 'MATH COMMENT': 'really good', 'ENGLISH': '', 'ENGLISH COMMENT': '', 'PHYSICS': 'C', 'PHYSICS COMMENT': 'keep going', 'AFRIKAANS': 'A', 'AFRIKAANS COMMENT': 'way to go'}, {'NAME': 'Sanri', 'LEVEL': 'IG', 'TUTOR': 'Heinrich', 'HONESTY': 'no', 'PERSEVERANCE': 'no', 'LOYALTY': 'no', 'COMPASSION': 'no', 'MATH': 'A', 'MATH COMMENT': 'ok', 'ENGLISH': 'C', 'ENGLISH COMMENT': 'no', 'PHYSICS': 'A', 'PHYSICS COMMENT': 'great', 'AFRIKAANS': 'B', 'AFRIKAANS COMMENT': 'Happy'}]

    with pytest.raises(FileNotFoundError):
        data_import('fake.csv')

def test_write_pdf():

    data = [{'NAME': 'Heinrich', 'LEVEL': 'AS', 'TUTOR': 'Sanri', 'HONESTY': 'yes', 'PERSEVERANCE': 'yes', 'LOYALTY': 'yes', 'COMPASSION': 'yes', 'MATH': 'A', 'MATH COMMENT': 'really good', 'ENGLISH': '', 'ENGLISH COMMENT': '', 'PHYSICS': 'C', 'PHYSICS COMMENT': 'keep going', 'AFRIKAANS': 'A', 'AFRIKAANS COMMENT': 'way to go'}, {'NAME': 'Sanri', 'LEVEL': 'IG', 'TUTOR': 'Heinrich', 'HONESTY': 'no', 'PERSEVERANCE': 'no', 'LOYALTY': 'no', 'COMPASSION': 'no', 'MATH': 'A', 'MATH COMMENT': 'ok', 'ENGLISH': 'C', 'ENGLISH COMMENT': 'no', 'PHYSICS': 'A', 'PHYSICS COMMENT': 'great', 'AFRIKAANS': 'B', 'AFRIKAANS COMMENT': 'Happy'}]

    assert write_pdf(data) == True

    data = [{'NAME': '', 'LEVEL': 'AS', 'TUTOR': 'Sanri', 'HONESTY': 'yes', 'PERSEVERANCE': 'yes', 'LOYALTY': 'yes', 'COMPASSION': 'yes', 'MATH': 'A', 'MATH COMMENT': 'really good', 'ENGLISH': '', 'ENGLISH COMMENT': '', 'PHYSICS': 'C', 'PHYSICS COMMENT': 'keep going', 'AFRIKAANS': 'A', 'AFRIKAANS COMMENT': 'way to go'}, {'NAME': 'Sanri', 'LEVEL': 'IG', 'TUTOR': 'Heinrich', 'HONESTY': 'no', 'PERSEVERANCE': 'no', 'LOYALTY': 'no', 'COMPASSION': 'no', 'MATH': 'A', 'MATH COMMENT': 'ok', 'ENGLISH': 'C', 'ENGLISH COMMENT': 'no', 'PHYSICS': 'A', 'PHYSICS COMMENT': 'great', 'AFRIKAANS': 'B', 'AFRIKAANS COMMENT': 'Happy'}]

    assert write_pdf(data) == False