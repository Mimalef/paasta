from flask import Blueprint
from kernel.config import VIEWS_DIR
	
blueprint = Blueprint(
	'blueprint',
	__name__,
	template_folder= VIEWS_DIR
)

from os import path
from glob import glob

__all__ = [
	path.basename(f)[:-3]
	for f in glob(path.dirname(__file__) + "/*.py")
]

__all__.append('blueprint')