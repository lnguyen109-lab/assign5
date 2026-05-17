import pytest
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

'''
get_age() function should return these numbers correctly, and be able to tell when someone's birthday has passed this year
'''

class TestUserProfile:
    # Some of these should return the wrong age
    def test_correct_age(self):

        reference_date = datetime(2000, 2, 28)
        assert UserProfile.get_age(reference_date) == 26

        reference_date = datetime(2000, 3, 28)
        assert UserProfile.get_age(reference_date) == 26
        
        reference_date = datetime(2000, 4, 28)
        assert UserProfile.get_age(reference_date) == 26
        
        reference_date = datetime(2000, 5, 28)
        assert UserProfile.get_age(reference_date) == 25
        
        reference_date = datetime(2000, 6, 28)
        assert UserProfile.get_age(reference_date) == 25

        reference_date = datetime(2000, 7, 28)
        assert UserProfile.get_age(reference_date) == 25






