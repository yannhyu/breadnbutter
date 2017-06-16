# evenley.py
import xmltodict
#import json
from toolchain import write, scrub_data_value
from evendict import flush

def digest_xml(filename):
    results = []
    with open(filename, 'r') as fh:
        xml = fh.read().replace('\n', '')
        res = xmltodict.parse(xml)
        # print(json.dumps(result, indent=4))
        inflated_res = flush(res)
        # for k, v in inflated_res.items():
        #     print('{} ---> {}'.format(k, v))
        if ('catalog', 'book') in inflated_res:
            books = inflated_res.get(('catalog', 'book'))
            if isinstance(books, list):
                for book in books:
                    results.append(book)
    
    return results


if __name__ == '__main__':
    resp_file = 'books.xml'
    output_file = 'books_mapped.txt'
    results = digest_xml(resp_file)
    write(output_file, results)    