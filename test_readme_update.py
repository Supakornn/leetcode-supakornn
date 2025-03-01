import unittest
import os
import shutil
from update_readme import update_readme
from sort_readme import sort_toc

class TestReadmeUpdate(unittest.TestCase):
    def setUp(self):
        os.makedirs("22. Add Binary", exist_ok=True)
        os.makedirs("68. Text Justification", exist_ok=True)
        
        with open("README.md", "w") as f:
            f.write("""# LeetCode Solutions\n\n### 📚 Table of Contents\n\n- [1. Two Sum](/1. Two Sum/main.go)\n""")

    def tearDown(self):
        shutil.rmtree("67. Add Binary", ignore_errors=True)
        shutil.rmtree("68. Text Justification", ignore_errors=True)
        
    def test_update_readme(self):
        update_readme()
        
        with open("README.md", "r") as f:
            content = f.read()
            
        self.assertIn("22. Add Binary", content)
        self.assertIn("68. Text Justification", content)

if __name__ == "__main__":
    unittest.main()
