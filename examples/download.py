import nexradaws2
import tempfile
import six
templocation = tempfile.mkdtemp()
conn = nexradaws2.NexradAwsInterface()
scans = conn.get_avail_scans('2013', '05', '31', 'KTLX')

localfiles = conn.download(scans[0:12],templocation)
six.print_(localfiles.success)
six.print_(localfiles.success[0].filepath)