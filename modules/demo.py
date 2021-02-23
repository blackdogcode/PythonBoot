from time import sleep

print('demo module imported')


def process_data(prev_data):
    print('Start Data Processing')
    post_data = prev_data + " modifying completed"
    sleep(3)
    print('End Data Processing')
    return post_data
