import subprocess


class vmrun():

    def __init__(self, bundle_path=None, binary_path=None):
        if bundle_path:
            pass
        else:
            self.cli_path = ['/Applications/VMware Fusion.app/Contents'
                             '/Library/vmrun', '-T', 'fusion']

    def __cli(self, arguments):
        """
        Execute the coomand.
        Receives a list with the command, the path to the vm and additionals
        parameters, in this exact order.
        """
        command = self.cli_path + arguments
        print command
        proc = subprocess.call(command)

    def check_vmx_path(self, vmx_path):
        """

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

    def start(self, vmx_path, gui=False):
        if self.check_vmx_path(vmx_path):
            if not gui:
                args = ['start', vmx_path, 'nogui']
            else:
                args = ['start', vmx_path, 'gui']
            self.__cli(args)
