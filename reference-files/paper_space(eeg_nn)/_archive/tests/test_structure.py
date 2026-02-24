import os
import unittest


ROOT = os.path.dirname(os.path.dirname(__file__))


class PaperSpaceStructureTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required_paths = [
            os.path.join(ROOT, "main.tex"),
            os.path.join(ROOT, "build.ps1"),
            os.path.join(ROOT, "bib", "references.bib"),
            os.path.join(ROOT, "sections"),
            os.path.join(ROOT, "figures"),
            os.path.join(ROOT, "tables"),
        ]
        missing = [path for path in required_paths if not os.path.exists(path)]
        self.assertFalse(missing, f"Missing required paths: {missing}")

    def test_main_uses_ccn_style(self) -> None:
        main_tex = os.path.join(ROOT, "main.tex")
        with open(main_tex, "r", encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn(r"\usepackage{ccn}", content)
        self.assertIn(r"\bibliographystyle{ccn_style}", content)


if __name__ == "__main__":
    unittest.main()
