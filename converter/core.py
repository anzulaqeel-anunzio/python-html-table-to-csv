# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from html.parser import HTMLParser
import csv
import io

class HtmlTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.current_table = []
        self.current_row = []
        self.current_cell_text = ""
        self.in_cell = False
        self.in_table = False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
            self.current_table = []
        elif tag == "tr":
            if self.in_table:
                self.current_row = []
        elif tag in ["td", "th"]:
            if self.in_table:
                self.in_cell = True
                self.current_cell_text = ""

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
            if self.current_table:
                self.tables.append(self.current_table)
        elif tag == "tr":
            if self.in_table:
                self.current_table.append(self.current_row)
        elif tag in ["td", "th"]:
            if self.in_table:
                self.in_cell = False
                self.current_row.append(self.current_cell_text.strip())

    def handle_data(self, data):
        if self.in_cell:
            self.current_cell_text += data

class HtmlToCsvConverter:
    @staticmethod
    def get_tables_as_csv(html_content):
        parser = HtmlTableParser()
        parser.feed(html_content)
        
        results = []
        for i, table in enumerate(parser.tables):
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerows(table)
            results.append(output.getvalue())
            
        return results

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
