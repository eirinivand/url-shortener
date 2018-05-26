from url_shortener import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/tssss')
    assert response.data == b'no such url found'