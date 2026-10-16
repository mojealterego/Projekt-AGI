import unittest
from agi_research.experiment import make_trace, transform, decode, run


class ExperimentTests(unittest.TestCase):
    def test_balanced_baseline(self):
        data = run(100)["results"]
        self.assertEqual(data["identity"]["bit_recovery_accuracy"], 1.0)
        self.assertEqual(data["paraphrase"]["bit_recovery_accuracy"], 1.0)
        self.assertEqual(data["bottleneck"]["bit_recovery_accuracy"], 0.5)
        self.assertTrue(all(x["task_accuracy"] == 1.0 for x in data.values()))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            make_trace(2)
        with self.assertRaises(ValueError):
            run(3)
        with self.assertRaises(ValueError):
            transform("a", "unknown")

    def test_receiver(self):
        self.assertEqual(decode(make_trace(0)[0]), 0)
        self.assertEqual(decode(make_trace(1)[0]), 1)


if __name__ == "__main__":
    unittest.main()
