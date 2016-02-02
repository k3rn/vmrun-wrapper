import subprocess
import os


class cli():

    def __init__(self, vmrun_path=None):
        if vmrun_path:
            self._cli = [vmrun_path, '-T', 'fusion']
        else:
            self._cli = ['/Applications/VMware Fusion.app/Contents'
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

        command = self._cli + arguments
        proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
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
            if vmx_path[-8:] == 'vmwarevm':
                if os.path.isdir(vmx_path):
                    filelist = os.listdir(vmx_path)
                    for file in filelist:
                        if file[-3:] == 'vmx':
                            path = os.path.join(vmx_path, file)
                            if os.path.isfile(path):
                                return True
                            else:
                                return False
                else:
                    return False
            else:
                return False
        else:
            if os.path.isfile(vmx_path):
                return True
            else:
                return False
