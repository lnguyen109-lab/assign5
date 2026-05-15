import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

class TestUserProfile:
    def test_correct_age(self):
      assert UserProfile.get_age("2/28/2000") == 26
      assert UserProfile.get_age("3/28/2000") == 26
      assert UserProfile.get_age("4/28/2000") == 26
      assert UserProfile.get_age("5/28/2000") == 25
      assert UserProfile.get_age("6/28/2000") == 25
      assert UserProfile.get_age("7/28/2000") == 25


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
