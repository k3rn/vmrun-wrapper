import subprocess


class vmrun():

    def __init__(self, bundle_path=None, binary_path=None):
        if bundle_path:
            pass
        else:
            self._cli_path = ['/Applications/VMware Fusion.app/Contents'
                              '/Library/vmrun', '-T', 'fusion']

    def _cli(self, arguments):
        if arguments[0] != 'list' and not self.check_vmx_path(arguments[1]):
            raise ValueError

        command = self.cli_path + arguments
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        return proc.communicate()

    def check_vmx_path(self, vmx_path):
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
        if not gui:
            self._cli(['start', vmx_path, 'nogui'])
        else:
            self._cli(['start', vmx_path, 'gui'])

    def stop(self, vmx_path, hard=True):
        if hard:
            self._cli(['stop', vmx_path, 'hard'])
        else:
            self._cli(['stop', vmx_path, 'soft'])

    def pause(self, vmx_path):
        self._cli(['pause', vmx_path])

    def unpause(self, vmx_path):
        self._cli(['unpause', vmx_path])

    def suspend(self, vmx_path, hard=True):
        self._cli(['suspend', vmx_path])

    def list(self):
        result = self._cli(['list'])[0].split()
        if int(result[3]) == 0:
            return {'count': 0}
        machines = list()
        for n in range(4, len(result)):
            machines.append(result[n])
        return {'count': result[3], 'machines': machines}
