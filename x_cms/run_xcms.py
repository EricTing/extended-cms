import os


def checkEnv():
    """check if pkcombu and apoc are properly installed
    """
    cmd_exists = lambda x: any(os.access(os.path.join(path, x), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))
    assert cmd_exists('pkcombu'), "Cannot find pkcombu"
    assert cmd_exists('apoc'), "Cannot find apoc"
