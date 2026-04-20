from unittest.mock import MagicMock, patch
from list_contents import main

def make_blob(name):
    blob=MagicMock()
    blob.name=name
    return blob

# mix of matching and non-matching files to verify that filter grabs all matching cases
mock_blobs=[
    make_blob('f1.csv.gz'),
    make_blob('f2.csv.gz'),
    make_blob('file3.csv.gz'),
    make_blob('f4.gz'),
    make_blob('f5.csv'),
    make_blob('readme.txt'),
]

@patch('list_contents.BlobServiceClient')
def test_print_all_matching_files(mock_client, capsys):
    mock_container=MagicMock()
    mock_container.list_blobs.return_value=mock_blobs
    mock_client.return_value.get_container_client.return_value=mock_container

    main()

    output=capsys.readouterr().out

    # assert that all matching files are printed
    assert 'f1.csv.gz' in output
    assert 'f2.csv.gz' in output
    assert 'file3.csv.gz' in output
    assert 'f4.gz' not in output
    assert 'f5.csv' not in output
    assert 'readme.txt' not in output

