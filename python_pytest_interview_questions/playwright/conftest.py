import pytest
from playwright.sync_api import Page, Playwright, expect

@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param


