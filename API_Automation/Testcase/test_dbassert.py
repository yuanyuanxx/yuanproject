# -*- coding:utf-8 -*-
from API_Automation.Common import dbselect
import pytest

def test_getuser(db):
    users=dbselect.select_user(db)
    print(len(users))
    assert len(users)==13
