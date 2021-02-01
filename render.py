#!/usr/bin/env python

import os, sys, csv, jinja2, yaml

# Set up Jinja2
env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates')
    )

# Make sure directories exist
os.makedirs(f'./configs', exist_ok=True)

# Open/reader CSV file
def with_csv():
    with open('./data.csv', 'r') as df:
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
        template = env.get_template('config_csv.j2')
        # Loop through each row
        for row in data:
            '''
            You can refer to the keys directly in the template
            
            hostname {{ hostname }}
            '''
            # Open hostname-specific file, write out rendered template
            with open(f"./configs/{row['hostname']}_csv.txt", 'w') as tf:
                tf.write(template.render(row))
            print(f"Rendered template for {row['hostname']} from CSV")

def with_yaml():
    with open('./data.yaml', 'r') as df:
        data = yaml.full_load(df)

        template = env.get_template('config_yaml.j2')
        for device, device_config in data['devices'].items():
            with open(f"./configs/{device}_yaml.txt", 'w') as tf:
                tf.write(template.render(g=data['global'], hostname=device, config=device_config))

            print(f"Rendered template for {device} from YAML")

with_csv()
with_yaml()
