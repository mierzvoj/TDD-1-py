import unittest

from main import statement


class Test(unittest.TestCase):

    def test_play_earned(self):
        self.assertTrue("$650" in statement({"customer": "BigCo",
                                             "performances": [{"playID": "hamlet", "audience": 55}]}, {
                                                "hamlet": {"name": "Hamlet", "type": "tragedy"}}

                                            ))

    def test_play_amount_owed(self):
        self.assertTrue("1,150" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "hamlet", "audience": 55},
                                                               {"playID": "othello", "audience": 40}]},
                                             {
                                                 "hamlet": {"name": "Hamlet", "type": "tragedy"},
                                                 "othello": {"name": "Othello", "type": "tragedy"}}))

    def test_play_credits_on_tragedy(self):
        self.assertTrue("35" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "hamlet", "audience": 55},
                                                               {"playID": "othello", "audience": 40}]},
                                             {
                                                 "hamlet": {"name": "Hamlet", "type": "tragedy"},
                                                 "othello": {"name": "Othello", "type": "tragedy"}}))

    def test_play_credits_on_comedy(self):
        self.assertTrue("12" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "as-like", "audience": 35}]},
                                             {
                                                 "as-like": {"name": "As You Like It", "type": "comedy"}
                                             }))
