## Config Render Example

```
git clone https://github.com/yzguy/config_render_example.git
cd config_render_example

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

-> python render.py
Rendered template from CSV to ./configs/switch1_csv.txt
Rendered template from CSV to ./configs/switch2_csv.txt
Rendered template from YAML to ./configs/switch1_yaml.txt
Rendered template from YAML to ./configs/switch2_yaml.txt
```
