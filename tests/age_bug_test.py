import pytest
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile
from src.location import Location

'''

get_age() function should return these numbers correctly, and be able to tell when someone's birthday has passed this year

'''

class TestUserProfile:
    # Some of these should return the wrong age
    def test_correct_age(self):

        User = UserProfile(
            name = "Test Name",
            email = "testname@something.com",
            password = "ThisisATest123!",
            dob = "2000-04-28",
            location = Location(
                city = "Los Angeles",
                state = "CA",
                country = "USA"
            )
        )

        assert User.get_age(datetime(2025, 2, 28)) == 24
        assert User.get_age(datetime(2025, 4, 26)) == 24
        assert User.get_age(datetime(2025, 4, 28)) == 25
        assert User.get_age(datetime(2025, 4, 30)) == 25
        assert User.get_age(datetime(2025, 6, 28)) == 25

