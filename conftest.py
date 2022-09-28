import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application(browser='chrome', base_url='http://localhost/addressbook/')
    fixture.session.login(username='admin', password='secret')
    request.addfinalizer(fixture.destroy)
    return fixture

