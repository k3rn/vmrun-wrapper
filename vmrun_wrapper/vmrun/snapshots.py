from vmrun_wrapper.vmrun import cli


class snapshots():

    def __init__(self):
        self.vmrun = cli().cli

    def list(self, vmx_path, showtree=False):
        """
        List the snapshots of a virtual machine.

        At this point I can't figure out a way to display the connections
        between snapshots, so if showtree set to true, it doesn't return
        anything diferent at this point.

        :param str vmx_path: The path to the virtual machine.
        :param bool showtree: Whether show the snapshot tree.
        :returns: The number of snapshots and the names
        :rtype: dict
        """
        if showtree:
            result = self.vmrun(['listSnapshots', vmx_path,
                                'showTree'])[0].split()
        else:
            result = self.vmrun(['listSnapshots', vmx_path])[0].split()
        if int(result[2]) == 0:
            return {'count': 0}

        snapshots = list()
        for n in range(3, len(result)):
            snapshots.append(result[n])
        return {'count': result[2], 'snapshots': snapshots}

    def create(self, vmx_path, snapshot_name):
        """
        Create a snapshot of the virtual machine

        :param str vmx_path: The path to the virtual machine
        :param str name: The name of the snapshot
        """
        self.vmrun(['snapshot', vmx_path, snapshot_name])

    def delete(self, vmx_path, snapshot_name, delete_children=False):
        """
        Delete a snapshot of the virtual machone

        :param str vmx_path: The path to the virtual machine
        :param str snapshot_name: The name of the snapshot
        :param bool delete_children: Also deletes the children of the snapshot
        """
        if delete_children:
            self.vmrun(['deleteSnapshot', vmx_path, snapshot_name,
                       'andDeleteChildren'])
        else:
            self.vmrun(['deleteSnapshot', vmx_path, snapshot_name])

    def revert_to_snapshot(self, vmx_path, snapshot_name):
        """
        Revert the virtual machine to the given snapshot

        :param str vmx_path: The path to the virtual machine
        :param str snapshot_name: The name of the snapshot
        """
        self.vmrun('revertToSnapshot', vmx_path, snapshot_name)
