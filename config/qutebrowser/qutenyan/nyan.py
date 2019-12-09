# Copyright 2018 Jay Kamat <jaygkamat@gmail.com>

# This file is part of qutenyan.
#
# qutenyan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutenyan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutenyan.  If not, see <http://www.gnu.org/licenses/>.


import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtCore

from qutebrowser.mainwindow.statusbar import percentage

NYAN_WIDTH = 150


class NyanPercentage(QSlider):

	"""Reading percentage displayed in the statusbar."""

	def __init__(self, parent=None):
		"""Constructor. Set percentage to 0%."""
		super().__init__(parent)

		# TODO find a better way to get this
		self.tab = None
		self.pressed = False

		self.set_perc(0, 0)

		self.setOrientation(QtCore.Qt.Horizontal)
		self.setMaximum(100)

		# Get nyan resources
		dir_path = os.path.dirname(os.path.realpath(__file__))
		nyan_img_path = os.path.join(dir_path, "./img/nyan.svg")
		nyan_rainbow_path = os.path.join(dir_path, "./img/rainbow.svg")

		# TODO reduce the magic numbers in here (and account for thicker statusbars)
		self.setStyleSheet("""
			QSlider::groove {{
				border: 1px none;
				height: 16px;
				margin: 0 12px;
			}}

			QSlider::sub-page:horizontal {{
				border-image: url({});
			}}

			QSlider::handle:horizontal {{
				image: url({});
				width: 30px;
				margin: -24px -12px;
			}}
		""".format(nyan_rainbow_path, nyan_img_path))

		self.setMaximumWidth(NYAN_WIDTH)
		self.setMinimumWidth(NYAN_WIDTH)

		self.valueChanged.connect(self.val_changed)
		self.sliderPressed.connect(self.pressed_slot)
		self.sliderReleased.connect(self.released_slot)

	@pyqtSlot(int, int)
	def set_perc(self, _x_offset, y_offset):  # pylint: disable=unused-argument
		"""Setter to be used as a Qt slot.

		Args:
			x: The x percentage (int), currently ignored.
			y: The y percentage (int)
		"""
		# controlled by slider
		if self.pressed:
			return

		if y_offset is None:
			# We don't know, the pos, set to 0
			self.setValue(0)
		else:
			self.setValue(min(y_offset, 100))

	@pyqtSlot()
	def val_changed(self):
		"""Update tab position based on slider"""
		if self.pressed and self.tab:
			self.tab.scroller.to_perc(y=self.value())

	@pyqtSlot()
	def pressed_slot(self):
		"""Update pressed status"""
		self.pressed = True

	@pyqtSlot()
	def released_slot(self):
		"""Update pressed status"""
		self.pressed = False

	def on_tab_changed(self, tab):
		"""Update scroll position when tab changed."""
		self.tab = tab
		self.set_perc(*tab.scroller.pos_perc())


def init_qutenyan():
	"""Initialize qutenyan"""
	# This is really bad, but we need nyans
	percentage.Percentage = NyanPercentage


init_qutenyan()
