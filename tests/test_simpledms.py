import datetime
import os

from simpledms.pdfhandler import DateExtractor
from simpledms.pdfhandler import PdfHandler

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_pdfhandler():

    pdfh = PdfHandler("tests/Letter_de.pdf")
    text = pdfh.gettext()
    dateext = DateExtractor(text)
    assert datetime.datetime(2018, 3, 1) == dateext.getdate()

    pdfh.createthumbnail()

    pdfh.update_and_move(dir_path, "testout", "tags", "2018-03-01")

    date_testvector = ["1.3.2018", "01-03-2018", "1. März 2018", "2018-03-01"]

    for date2test in date_testvector:
        dateext = DateExtractor(date2test)
        date = dateext.getdate()
        assert date == datetime.datetime(2018, 3, 1)

    # Rename pdf file
    os.rename("tests/2018-03-01 testout.pdf", "tests/Letter_de.pdf")
