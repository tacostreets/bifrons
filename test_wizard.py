#!/usr/bin/env python3

import unittest
import wiz

class WizText(unittest.TestCase):
    def test_travel_tower(self):
        wizard = wiz.Wizard(location="village")
        self.assertEqual(
            wizard.travel("tower"),
            "You travel to your modest one story wizard tower!"
            )

    def test_travel_tower_already_there(self):
        wizard = wiz.Wizard(location="tower")
        self.assertEqual(
            wizard.travel("tower"),
             "You are already in the tower, silly wizard!"
            )

if __name__=='__main__':
    unittest.main()