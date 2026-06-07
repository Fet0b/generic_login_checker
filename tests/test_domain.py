from app.domain.model import * 
import pytest


def test_file_to_list(tmp_path): 

    source = tmp_path / "aaaaaaa.csv"
    source.write_text("aaaa\naaaa\naaaa\naaaa\naaaa\n")
    #source.write_text("aaaa,aaaa,aaaa,aaaa,aaaa")
    
    reader = file_to_list(source)
    lista = reader.convert_to_list()
    
    correct = [["aaaa"], ["aaaa"], ["aaaa"], ["aaaa"], ["aaaa"]]
    
    assert lista == correct