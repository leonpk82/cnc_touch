from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

    # add any custom methods here

from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

    # add any custom methods here
       
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.offsetButtonGroup.buttonClicked.connect(self.offsetHandleKeys)
        self.mdiButtonGroup.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiBackSpaceKey.clicked.connect(self.mdiBackSpace)

        self.toolOffsetGroup.buttonClicked.connect(self.toolHandleKeys)
        self.toolOffsetBackspace.clicked.connect(self.toolBackSpace)

    def offsetHandleKeys(self, button):
        char = str(button.text())
        text = self.offsetLabel.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.offsetLabel.setText(text)


    def mdiHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiBackSpace(self):
        if len(self.mdiEntry.text()) > 0:
            text = self.mdiEntry.text()[:-1]
            self.mdiEntry.setText(text)



    def toolHandleKeys(self, button):
        text = self.toolOffsetLabel.text()
        if len(text) > 0:
            self.toolOffsetLabel.setText(text + button.text())
        else:
            self.toolOffsetLabel.setText(button.text())

    def toolBackSpace(self):
        text = self.toolOffsetLabel.text()[:-1]
        self.toolOffsetLabel.setText(text)


