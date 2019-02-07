from unittest import TestCase
from utils import nvim_utils

class TestNvimModule(TestCase):
    """ Base64クラスのテスト """

    def test_get_visual_pos(self):
        """ get_visual_posのテスト """

        class Nvim():
            def __init__(self, start_r, start_c, end_r, end_c):
                self.start_r = start_r
                self.start_c = start_c
                self.end_r = end_r
                self.end_c = end_c

            def eval(self, command):
                if command == 'getpos("\'<")[1:2]':
                    return self.start_r, self.start_c
                elif command == 'getpos("\'>")[1:2]':
                    return self.end_r, self.end_c
                else:
                    raise ValueError("invalid command!")

        test_patterns = [
            (1, 2, 1, 3),
        ]

        for start_r, start_c, end_r, end_c in test_patterns:
            with self.subTest(start_r=start_r, start_c=start_c, end_r=end_r, end_c=end_c):
                nvim = Nvim(start_r, start_c, end_r, end_c)
                self.assertEqual(nvim_utils.get_visual_pos(nvim), (start_r, start_c, end_r, end_c))