import json
import unittest
from app import response_for


class ResponseTests(unittest.TestCase):
    def test_home_page(self):
        status, content_type, body = response_for("/")
        self.assertEqual(status, 200)
        self.assertIn("text/html", content_type)
        self.assertIn("Vibe Coding", body)

    def test_health_check(self):
        status, content_type, body = response_for("/healthz")
        self.assertEqual(status, 200)
        self.assertIn("application/json", content_type)
        self.assertEqual(json.loads(body), {"status": "ok"})

    def test_unknown_path(self):
        status, _, body = response_for("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(json.loads(body), {"error": "not found"})


if __name__ == "__main__":
    unittest.main()
