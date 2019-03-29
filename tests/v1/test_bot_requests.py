import unittest
from v1.bot_requests import Room

class TestRoom(unittest.TestCase):
    """
    Tests for the requests made to and from the rooms
    """

    def test_get_rooms(self):
        room = Room()
        data = room.get_rooms()
        
        self.assertEqual(data.status_code, 200)