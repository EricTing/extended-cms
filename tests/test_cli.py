import pytest
from click.testing import CliRunner
from x_cms import run_xcms


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_with_checkenv():
    run_xcms.checkEnv()
