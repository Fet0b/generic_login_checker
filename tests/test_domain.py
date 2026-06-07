from app.domain.model import * 
import pytest


def test_file_to_list(): 

    reader = file_to_list("aaaaaaa.csv")
    correct = ["aaaa","aaaa","aaaa","aaaa","aaaa"]  
        
    assert(reader == correct) 