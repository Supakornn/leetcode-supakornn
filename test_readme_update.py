import unittest
import os
import shutil
from update_readme import update_readme

class TestReadmeUpdate(unittest.TestCase):
    def setUp(self):
        os.makedirs("22. Add Binary", exist_ok=True)
        os.makedirs("68. Text Justification", exist_ok=True)
        
        self.test_content = """## 🌟 My Personal LeetCode Solutions

- This repository is a collection of my personal LeetCode solutions.
- I will try to solve as many problems as possible and keep updating this repository.

<!-- Start  -->

### 📚 Table of Contents

- [1. Two Sum](./1.%20Two%20Sum/main.go)

<!-- End  -->"""

        with open("TEST_README.md", "w") as f:
            f.write(self.test_content)

    def tearDown(self):
        os.remove("TEST_README.md")
        shutil.rmtree("22. Add Binary", ignore_errors=True)
        shutil.rmtree("68. Text Justification", ignore_errors=True)
        
    def test_update_readme(self):
        from update_readme import update_readme
        update_readme("TEST_README.md")
        
        with open("TEST_README.md", "r") as f:
            content = f.read()
            
        self.assertIn("<!-- Start  -->", content)
        self.assertIn("<!-- End  -->", content)
        self.assertIn("## 🌟 My Personal LeetCode Solutions", content)

        self.assertIn("- [22. Add Binary](./22.%20Add%20Binary/)", content)
        self.assertIn("- [68. Text Justification](./68.%20Text%20Justification/)", content)

        self.assertNotIn("main.go", content)

if __name__ == "__main__":
    unittest.main()
