import os

from webdriver_manager.config import Configuration

expect_mz_latest = 'https://api.github.com/repos/mozilla/geckodriver/releases/latest'
expect_mz_tag = 'https://api.github.com/repos/mozilla/geckodriver/releases/tags/{0}'
expect_gh_token = u'""'


def test_config_with_deafault_params():
    config = Configuration(config_folder=os.path.dirname(__file__))
    assert config.mozila_latest_release == expect_mz_latest
    assert config.mozila_release_tag == expect_mz_tag
    assert config.gh_token == expect_gh_token


def test_config_variables_with_default_params():
    config = Configuration()
    assert config.gh_token == ''
    assert config.mozila_latest_release == expect_mz_latest
    assert config.mozila_release_tag == expect_mz_tag


def test_config_with_custom_file():
    config = Configuration(config_folder=os.path.dirname(__file__), file_name="wd_config.ini")
    assert config.get('gh_token') == "test_token"
    assert config.get("mozila_latest_release") == "test_release"
