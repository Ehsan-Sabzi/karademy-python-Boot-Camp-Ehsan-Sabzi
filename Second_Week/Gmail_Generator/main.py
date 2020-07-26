def read_email_address():
    with open('email_address_list.txt', 'r') as email_file:
        for email_entry in email_file:
            yield email_entry


if __name__ == "__main__":
    read_email_address_generator = read_email_address()
    for email_address_entry in filter(lambda email_address: '@gmail.com' in email_address, read_email_address_generator):
        print(email_address_entry[:-11].replace('.', ''))
