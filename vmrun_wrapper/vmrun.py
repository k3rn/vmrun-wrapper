import subprocess


class vmrun():

    def __init__(self, bundle_path=None, binary_path=None):
        if bundle_path:
            pass
        else:
            self._cli_path = ['/Applications/VMware Fusion.app/Contents'
                              '/Library/vmrun', '-T', 'fusion']

    def _cli(self, arguments):
        """
        Executes the vmrun utility based on the given arguments.

        :param list arguments: a

        Is a list in which the first element is the \
        command to be executed. The second element is the path to the virtual
        machine, it can be the .vmwarevm folder or the .vmx folder.
        The subsequent elements are aditional parameters.
        """
        if arguments[0] != 'list' and not self.vmx_path_is_valid(arguments[1]):
            raise ValueError

        command = self.cli_path + arguments
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

    def start(self, vmx_path, gui=False):
        """
        Start the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param bool gui: Whether it is to start in the gui mode
        """
        if not gui:
            self._cli(['start', vmx_path, 'nogui'])
        else:
            self._cli(['start', vmx_path, 'gui'])

    def stop(self, vmx_path, hard=True):
        """
        Stop the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param hard: Whether it is to stop the hard way
        """

        if hard:
            self._cli(['stop', vmx_path, 'hard'])
        else:
            self._cli(['stop', vmx_path, 'soft'])

    def pause(self, vmx_path):
        """
        Pause the virtual machine

        :param str vmx_path: The path of the virtual machine
        """
        self._cli(['pause', vmx_path])

    def unpause(self, vmx_path):
        """
        Unpause the virtual machine

        :param str vmx_path: The path of the virtual machine
        """
        self._cli(['unpause', vmx_path])

    def suspend(self, vmx_path, hard=True):
        """
        Unpause the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param hard: Whether it is to suspend in the hard way
        """
        self._cli(['suspend', vmx_path])

    def list(self):
        """
        Lists the running virtual machines.

        Return a

        :returns: The number and the list of the machines running
        :rtype: dict
        """
        result = self._cli(['list'])[0].split()
        if int(result[3]) == 0:
            return {'count': 0}
        machines = list()
        for n in range(4, len(result)):
            machines.append(result[n])
        return {'count': result[3], 'machines': machines}
