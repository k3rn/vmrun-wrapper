import unittest
from vmrun_wrapper.vmrun import cli


class TestCheckers(unittest.TestCase):

    def setUp(self):
        self.cli = cli()

    def test_remove_slash_vmx_path_is_valid(self):
        self.assertEqual(self.cli.vmx_path_is_valid('vm.vmx/'), True)

    def test_with_vmwarevm_extension_vmx_path_is_valid(self):
        self.assertEqual(self.cli.vmx_path_is_valid('vm.vmwarevm'), True)

    def test_invalid_extension_vmx_path_is_valid(self):
        self.assertEqual(self.cli.vmx_path_is_valid('vmx.invalid'), False)

if __name__ == "__main__":
    unittest.main()
