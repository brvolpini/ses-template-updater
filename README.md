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

Create virtual environment and run script

```
pip install virtualenv
```
```
virtualenv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```


```
python3 update_ses_template.py EmailTemplate.json
```

