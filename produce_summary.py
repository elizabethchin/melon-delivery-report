file_one = "um-deliveries-20140519.txt"
file_two = "um-deliveries-20140520.txt"
file_three = "um-deliveries-20140521.txt"

def produce_summary(day, file):

        print(day)
        the_file = open(file)
        for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
        the_file.close()


