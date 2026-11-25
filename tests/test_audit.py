import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from casrn_validation_claim_audit.audit import audit, claims, evidence, main
from casrn_validation_claim_audit.phrases import CASRNVALIDATION, NOCASRNVALIDATION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in CASRNVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOCASRNVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate cas number\n```'), (False, False))
        self.assertEqual(claims("doesn't validate cas-number"), (False, True))
    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for source in ('import stdnum.casrn\nstdnum.casrn.%s(x)', 'import stdnum.casrn as c\nc.%s(x)', 'import stdnum\nstdnum.casrn.%s(x)', 'from stdnum import casrn as c\nc.%s(x)', 'from stdnum.casrn import %s as f\nf(x)'):
                with self.subTest(method=method, source=source): self.assertTrue(evidence(source % method))
    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            with self.subTest(name=name):
                self.assertTrue(evidence('obj.%s(x)' % name))
                self.assertTrue(evidence('from lib import %s as f\nf(x)' % name))
                self.assertFalse(evidence('%s(x)' % name))
                self.assertFalse(evidence('def %s(x): pass\nobj.%s(x)' % (name, name)))
    def test_not_evidence(self):
        cases = ['import stdnum.casrn', 'validate(x)', 'is_valid(x)', 'casrn(x)', 'compact(x)', 'calc_check_digit(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'stdnum.casrn.compact(x)', 'stdnum.casrn.calc_check_digit(x)', 'import re\nre.match("x", x)', 'import re\nre.search("x", x)', 'import re\nre.fullmatch("x", x)', 'len(x) == 7', 'x[2] == "-"', 'x.isdigit()', 'obj.lookup_cas_number(x)', 'obj.generate_cas_number()', 'obj.validate_inchi(x)', 'obj.validate_smiles(x)', 'obj.validate_ec_number(x)', 'obj.validate_un_number(x)', 'obj.lookup_pubchem_cid(x)', 'obj.validate_chemical_structure(x)', '"validate cas number"', '# cas number validation', 'validate_cas_number', 'def broken(', 'import subprocess\nsubprocess.run(["checker", x])', 'import stdnum.casrn as c\nc = x\nc.validate(x)', 'from stdnum.casrn import validate\ndef validate(x): pass\nvalidate(x)', 'import stdnum.casrn as c\nwith thing() as c: pass\nc.is_valid(x)']
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))
        self.assertTrue(evidence('result = thing()\nresult.validate_cas_number(x)'))
    def test_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('validate cas number')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'tests').mkdir()
            (root / 'tests/test_x.py').write_text('import stdnum.casrn\nstdnum.casrn.validate(x)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root / 'app.py').write_text('import stdnum.casrn\nstdnum.casrn.is_valid(x)')
            self.assertEqual(audit(root), [])
            (root / 'README.md').write_text('no cas number validation')
            self.assertEqual(audit(root)[0]['id'], 'documented-no-casrn-validation-claim-false')
            self.assertEqual(audit(root, ['app.py']), [])
    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(['audit', tmp, '--json']), 0)
            self.assertEqual(main(['audit', tmp, '--fail-on', 'medium']), 0)
            self.assertEqual(main(['audit', tmp + '/missing']), 1)
