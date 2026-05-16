import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

'''
Must be at least 8 characters long
Must contain one uppercase, one lowercase, one digit and one special character from: @$!%*?&
'''

class TestUserPassword:
    # Some of the true statements should fail
    def test_valid_password(self):
        assert UserProfile.valid_password("passwordTest109!") == True
        assert UserProfile.valid_password("@ThisPasses3") == True
        assert UserProfile.valid_password("Testing123!") == True
        assert UserProfile.valid_password("&Can15MinutesSaveYou15%OnCarInsurance?") == True
        assert UserProfile.valid_password("1234567890Yeah!") == True
        assert UserProfile.valid_password("helloWorld67!") == True

        assert UserProfile.valid_password("ThereIsNothingSpecialHere") == False
        assert UserProfile.valid_password("nevermore!") == False
        assert UserProfile.valid_password("0987654321") == False
        assert UserProfile.valid_password("WHATDOYOUWANT?") == False
