import subprocess


class cli():

    def __init__(self, bundle_path=None, binary_path=None):
        if bundle_path:
            pass
        else:
            self._cli_path = ['/Applications/VMware Fusion.app/Contents'
                              '/Library/vmrun', '-T', 'fusion']

    def cli(self, arguments):
        """
        Executes the vmrun utility based on the given arguments.

        :param list arguments: | The first element is the command to be
                               | executed. The second is the path to the
                               | virtual machine and has to be either the
                               | extension *.vmx* or *.vmwarevm*. The remaining
                               | elements are aditionals depending of the
                               | command to be executed.
        """
        if arguments[0] != 'list' and not self.vmx_path_is_valid(arguments[1]):
            raise ValueError

        command = self._cli_path + arguments
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        return proc.communicate()

    def vmx_path_is_valid(self, vmx_path):
        """
        Verify if the given path is valid following these conditions:

        If the extension is *.vmx*, verify it exists and is a file.

        If the extension is *.vmwarevm*, verify if it is a folder and
        contains a *.vmx* file inside.

        :param str vmx_path: The path to be tested
        :rtype: bool
        """
        if vmx_path[-1:] == '/':
            vmx_path = vmx_path[:-1]

        if vmx_path[-3:] != 'vmx':
            a = vmx_path[-8:]
            if a == 'vmwarevm':
                return True
            else:
                return False
        else:
            return True
