# ses-template-updater

<p align="center">
  <img src="ses+py2.png">
</p>


### Description
SES Email Templates creation and update through python and Boto3


### Usage

Set AWS ENV
```
export AWS_ACCESS_KEY_ID = ****************
export AWS_SECRET_ACCESS_KEY = ****************
export AWS_REGION = ****************
```

# Install venv
```
pip install virtualenv
```
# Create venv
## Windows
```
python -m virtualenv env
.\env\Scripts\activate
```
## Mac
```
virtualenv venv
source venv/bin/activate
```

# Install required libraries
```
pip install -r requirements.txt
```

# Run script
```
python3 update_ses_template.py EmailTemplate.json
```

