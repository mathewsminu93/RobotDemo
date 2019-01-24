from pathlib import Path

from docutils.core import publish_cmdline
from invoke import task
from rellu.tasks import clean
from robot.libdoc import libdoc


assert Path.cwd() == Path(__file__).parent


@task
def kw_docs(ctx):
    """Generates the library keyword documentation

    Documentation is generated by using the Libdoc tool.
    """
    libdoc(str(Path('CalculatorLibrary.py')),
           str(Path('docs/CalculatorLibrary.html')))


@task
def project_docs(ctx):
    """Generate project documentation.

     These docs are visible at http://robotframework.org/SeleniumLibrary/.
     """
    args = ['--stylesheet=style.css,extra.css',
            '--link-stylesheet',
            'README.rst',
            'docs/index.html']
    publish_cmdline(writer_name='html5', argv=args)
    print(Path(args[-1]).absolute())
