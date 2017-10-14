from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "microflack_common"
default_task = ['analyze', 'publish']


@init
def set_properties(project):
    #project.depends_on('flask')
    project.set_property('flake8_ignore', 'E402')
    project.set_property('flake8_verbose_output', True)
