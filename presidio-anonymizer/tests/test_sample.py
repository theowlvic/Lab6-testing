import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    dict1 = {
        "text":"My name is BIP.",
        'items': [
            {'start':11, 'end':14, 'entity_type':'PERSON', 'text':'BIP', 'operator':'replace'}
            ]
    }
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    assert result.text == dict1["text"]
    assert result.items[0].start == dict1["items"][0]["start"]
    assert result.items[0].end == dict1["items"][0]["end"]
    assert result.items[0].entity_type == dict1["items"][0]["entity_type"]
    assert result.items[0].text == dict1["items"][0]["text"]
    assert result.items[0].operator == dict1["items"][0]["operator"]