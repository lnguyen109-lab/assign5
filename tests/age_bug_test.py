import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

'''
get_age() function should return these numbers correctly, and be able to tell when someone's birthday has passed this year
'''

class TestUserProfile:
    # Some of these should return the wrong age
    def test_correct_age(self):
      assert UserProfile.get_age("2/28/2000") == 26
      assert UserProfile.get_age("3/28/2000") == 26
      assert UserProfile.get_age("4/28/2000") == 26
      assert UserProfile.get_age("5/28/2000") == 25
      assert UserProfile.get_age("6/28/2000") == 25
      assert UserProfile.get_age("7/28/2000") == 25
