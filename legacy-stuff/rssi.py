from subprocess import Popen, PIPE  # Used to run native OS commads in python wrapped subproccess


class rssi:

    def __init__(self, interface):
        self.interface = interface

    def getRawNetworkScan(self, sudo=False):
        # Scan command 'iwlist interface scan' needs to be fed as an array.
        if sudo:
            scan_command = ['sudo', 'iwlist', self.interface, 'scan']
        else:
            scan_command = ['iwlist', self.interface, 'scan']
        # Open a subprocess running the scan command.
        scan_process = Popen(scan_command, stdout=PIPE, stderr=PIPE)
        # Returns the 'success' and 'error' output.
        (raw_output, raw_error) = scan_process.communicate()
        # Block all execution, until the scanning completes.
        scan_process.wait()
        # Returns all output in a dictionary for easy retrieval.
        return {'output': raw_output, 'error': raw_error}
