# import os
# import subprocess

import pytest


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repo_name": "helloworld"})

    assert result.exception is None
    assert result.exit_code == 0
    assert result.project.basename == "helloworld"
    assert result.project.isdir()


# def run_tox(plugin):
#     """Run the tox suite of the newly created plugin."""
#     try:
#         subprocess.check_call(
#             ["tox", plugin, "-c", os.path.join(plugin, "tox.ini"), "-e", "py"]
#         )
#     except subprocess.CalledProcessError as e:
#         pytest.fail(e)
