from vmrun_wrapper.vmrun import cli


class machine():

    def __init__(self):
        self.vmrun = cli().cli

    def start(self, vmx_path, gui=False):
        """
        Start the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param bool gui: Whether it is to start in the gui mode
        """
        if not gui:
            self.vmrun(['start', vmx_path, 'nogui'])
        else:
            self.vmrun(['start', vmx_path, 'gui'])

    def stop(self, vmx_path, hard=True):
        """
        Stop the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param hard: Whether it is to stop the hard way
        """

        if hard:
            self.vmrun(['stop', vmx_path, 'hard'])
        else:
            self.vmrun(['stop', vmx_path, 'soft'])

    def pause(self, vmx_path):
        """
        Pause the virtual machine

        :param str vmx_path: The path of the virtual machine
        """
        self.vmrun(['pause', vmx_path])

    def unpause(self, vmx_path):
        """
        Unpause the virtual machine

        :param str vmx_path: The path of the virtual machine
        """
        self.vmrun(['unpause', vmx_path])

    def suspend(self, vmx_path, hard=True):
        """
        Unpause the virtual machine

        :param str vmx_path: The path of the virtual machine
        :param bool hard: Whether it is to suspend in the hard way
        """
        self.vmrun(['suspend', vmx_path])

    def list(self):
        """
        Lists the running virtual machines.

        :returns: The number and the list of the machines running
        :rtype: dict
        """
        result = self.vmrun(['list'])[0].split()
        if int(result[3]) == 0:
            return {'count': 0}
        machines = list()
        for n in range(4, len(result)):
            machines.append(result[n])
        return {'count': result[3], 'machines': machines}

    def clone(self, vmx_path_src, vmx_path_dest, full=True, snapshot=None):
        """
        Clone the virtual machine

        :param str vmx_path_src: The path to the original virtual machine
        :param str vmx_path_dest: The path to the clone virtual machine
        :param bool full: Whether it is a full or linked clone
        :param str snapshot: The snapshot to clone from
        """
        args = ['clone', vmx_path_src, vmx_path_dest]
        if full:
            args.append('full')
        else:
            args.append('linked')
        if snapshot:
            args.append('-snapshot=%s' % snapshot)
        if name:
            args.append('-cloneName=%s' % name)
        self.vmrun(args)
