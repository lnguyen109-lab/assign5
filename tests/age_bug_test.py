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
      assert UserProfile.get_age(2000, 2, 28) == 26
      assert UserProfile.get_age(2000, 3, 28) == 26
      assert UserProfile.get_age(2000, 4, 28) == 26
      assert UserProfile.get_age(2000, 5, 28) == 25
      assert UserProfile.get_age(2000, 6, 28) == 25
      assert UserProfile.get_age(2000, 7, 28) == 25
