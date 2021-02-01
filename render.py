#!/usr/bin/env python

import os, sys, csv, jinja2

# Set up Jinja2
env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates')
    )

# Make sure directories exist
os.makedirs(f'./configs', exist_ok=True)

# Get path to CSV from CLI arg
try:
    data_file = sys.argv[1]
except IndexError:
    print('You must specify a csv file')

# Open/reader CSV file
with open(data_file, 'r') as df:
    ''' 
    DictReader creates a dict for each row, with the header being the key
    [{
        'hostname': 'switch1',
        'datacenter': 'dc1',
        ...
    }]
    '''
    data = csv.DictReader(df)

    # Load Jinja2 template
    template = env.get_template('config.j2')
    # Loop through each row
    for row in data:
        # Open hostname-specific file, write out rendered template
        with open(f"./configs/{row['hostname']}.txt", 'w') as tf:
            tf.write(template.render(row))

        '''
        You can refer to the keys directly in the template
        
        hostname {{ hostname }}
        '''
        
        print(f"Rendered template for {row['hostname']}")
