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

        reference_date1 = datetime(2000, 2, 28)
        assert UserProfile.get_age(reference_date1) == 26

        reference_date2 = datetime(2000, 3, 28)
        assert UserProfile.get_age(reference_date2) == 26
        
        reference_date3 = datetime(2000, 4, 28)
        assert UserProfile.get_age(reference_date3) == 26
        
        reference_date4 = datetime(2000, 5, 28)
        assert UserProfile.get_age(reference_date4) == 25
        
        reference_date5 = datetime(2000, 6, 28)
        assert UserProfile.get_age(reference_date5) == 25

        reference_date6 = datetime(2000, 7, 28)
        assert UserProfile.get_age(reference_date6) == 25






