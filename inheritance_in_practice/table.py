# table.py
import sys

def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    # Emit table headers
    formatter.headings(colnames)
    for obj in objects:
        # Emit a row of table data
        rowdata = [ str(getattr(obj, colname)) for colname in colnames ]
        formatter.row(rowdata)


class TableFormatter(object):
    def __init__(self, outfile=None):
        if not outfile:
            outfile = sys.stdout
        self.outfile = outfile

    # Serve as a design spec for making tables (use inheritance to customize)
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)    # Initialize parent
        self.width = width

    def headings(self, headers):
        for header in headers:
            #print('{:>10s}'.format(header), end=' ', file=self.outfile)
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            #print('{:>10s}'.format(item), end=' ')
            print('{:>{}s}'.format(item, self.width), end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers), file=self.outfile)

    def row(self, rowdata):
        print(','.join(rowdata), file=self.outfile)


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}<th>'.format(h), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}<td>'.format(d), end='')
        print('</tr>')


class QuotedTextTableFormatter(TextTableFormatter):    # Tightly coupled
    def row(self, rowdata):    # Alter the behavior
        # Put quotes around all values
        quoted = [ '"{}"'.format(d) for d in rowdata ]
        super().row(quoted)


class QuotedMixin(object):    # Loosely coupled
    def row(self, rowdata):    # Alter the behavior
        # Put quotes around all values
        quoted = [ '"{}"'.format(d) for d in rowdata ]
        super().row(quoted)
