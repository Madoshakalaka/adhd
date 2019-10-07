from adhd.main import cmd_entry


def test_cmd_arg_parse(mocker):
    mocked = mocker.patch("adhd.main.start_monitoring")
    cmd_entry([..., "for", "1h"])
    mocked.assert_called_once_with("1h")


def test_cmd(capsys):
    # cmd_entry([..., 'arg1', 'arg2'])
    cmd_entry([...])
    captured = capsys.readouterr()
    assert captured.out.strip() == "reserved command line entry for python package adhd"
    assert captured.err == ""
