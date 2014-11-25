import unittest
from vmrun_wrapper.vmrun import vmrun


class TestCheckers(unittest.TestCase):

    def setUp(self):
        self.vmrun = vmrun()

    def test_remove_slash_check_vmx_path(self):
        self.assertEqual(self.vmrun.check_vmx_path('vm.vmx/'), True)

    def test_with_vmwarevm_extension_check_vmx_path(self):
        self.assertEqual(self.vmrun.check_vmx_path('vm.vmwarevm'), True)

    def test_invalid_extension_check_vmx_path(self):
        self.assertEqual(self.vmrun.check_vmx_path('vmx.invalid'), False)

if __name__ == "__main__":
    unittest.main()
