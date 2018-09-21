import PyPDF2
import sqlalchemy

import helpers
from psychotherapist import Psychotherapist


def main():
    f = open("/Users/Ben/Downloads/psychotherapeuten.pdf", "rb")
    file_reader = PyPDF2.PdfFileReader(f)
    session = sqlalchemy.Session()
    psychotherapist = None
    for page in file_reader.pages:
        text = page.extractText().split('\n')[5:-5]

        for element in text:
            if helpers.is_name(element):
                if psychotherapist:
                    session.add(psychotherapist)
                psychotherapist = Psychotherapist()
                psychotherapist.first_name = helpers.parse_name(element)[0]
                psychotherapist.last_name = helpers.parse_name(element)[1]
                continue

            if helpers.is_fee(element):
                fee = int(element)
                psychotherapist.fee_in_eur = fee
                print(psychotherapist.fee_in_eur)
                continue

            if helpers.is_postal_code(element):
                psychotherapist.postal_code = element
                continue

            if helpers.is_phone_number(element):
                psychotherapist.phone_number = element
                continue

            if helpers.is_specialization(element):
                pass


if __name__ == '__main__':
    main()