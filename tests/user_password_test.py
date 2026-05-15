import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

class TestUserPassword:
    
    def test_valid_password(self):
        assert UserProfile.valid_password("") == True
        assert UserProfile.valid_password("") == True
        assert UserProfile.valid_password("") == True
        assert UserProfile.valid_password("") == True

        assert UserProfile.valid_password("") == False
        assert UserProfile.valid_password("") == False
        assert UserProfile.valid_password("") == False
        assert UserProfile.valid_password("") == False

  if __name__ == "__main__":
    pytest.main([__file__, "-v"])
