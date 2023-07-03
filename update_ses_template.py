"""
Python script to create and update SES Email templates
"""

import os
import sys
import json
from colorama import Fore
import boto3


class AWSSesTemplate:
    """
    Class to manage SES Email templates creation and update
    """
    def __init__(self, region_name, aws_access_key_id=None, aws_secret_access_key=None):
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.client = self.create_client()

    def create_client(self):
        """Function to create Boto3 SES client
        Returns:
            Dic: return a python dictionary with the command output
        """
        return boto3.client('ses', region_name=self.region_name,
                            aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def list_templates(self):
        """Function to list templates
        Returns:
            Dic: return a python dictionary with the command output
        """
        response = self.client.list_templates(MaxItems=20)
        return [response['TemplatesMetadata'][index]['Name'] for index, item in enumerate(response['TemplatesMetadata'])]

    def get_template(self,template_name):
        """Function to get content of a template based on the name
        Args:
            template_name: name of the template
        Returns:
            Dic: return a python dictionary with template
        """
        return self.client.get_template(TemplateName=template_name)['Template']

    def create_template(self, template_name, subject_part, text_part, html_part):
        """Function to create SES Email template
        Args:
            template_name (str): Name of the template
            subject_part (str): Subject of the template
            text_part (str): Text part of the template
            html_part (str): HTML part of the template
        Returns:
            dic: return a python dictionary with the command output
        """
        response = self.client.create_template(
            Template={
                'TemplateName': template_name,
                'SubjectPart': subject_part,
                'TextPart': text_part,
                'HtmlPart': html_part
            }
        )
        return response

    def update_template(self, template_name, subject_part=None, text_part=None, html_part=None):
        """Function to update SES Email template
        Args:
            template_name (str): Name of the template
            subject_part (str): Subject of the template
            text_part (str): Text part of the template
            html_part (str): HTML part of the template
        Returns:
            dic: return a python dictionary with the command output
        """
        response = self.client.update_template(
            Template={
                'TemplateName': template_name,
                'SubjectPart': subject_part,
                'TextPart': text_part,
                'HtmlPart': html_part
            }
        )
        return response



def main():
    """Main function
    """
    TEMPLATE_NAME = sys.argv[1]
    TEMPLATE_NAME_SPLITTED =  os.path.splitext(TEMPLATE_NAME)[0]
    REMOTE_TEMPLATE_LIST = ses_client.list_templates()
    try:
        with open(f"""{os.environ['ACCOUNT_NAME']}/{TEMPLATE_NAME}""") as file:
            local_template = json.load(file)

        if TEMPLATE_NAME_SPLITTED not in REMOTE_TEMPLATE_LIST:
            ses_client.create_template(TEMPLATE_NAME_SPLITTED,
                                        local_template['Template']['SubjectPart'],
                                        local_template['Template']['TextPart'],
                                        local_template['Template']['HtmlPart'])
            print(f'{Fore.GREEN} Template {TEMPLATE_NAME_SPLITTED} does not exist. Creating...')
        elif ses_client.get_template(TEMPLATE_NAME_SPLITTED) == local_template['Template']:
            print(f'Template {TEMPLATE_NAME} does not need to be updated')
        else:
            ses_client.update_template(TEMPLATE_NAME_SPLITTED,
                                       local_template['Template']['SubjectPart'],
                                       local_template['Template']['TextPart'],
                                       local_template['Template']['HtmlPart'])
            print(f'{Fore.YELLOW} Updating {TEMPLATE_NAME}...')

    except Exception as err:
        print(f'ERROR: {err}')
        sys.exit(1)

if __name__ == '__main__':
    ses_client = AWSSesTemplate(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                                region_name=os.environ['AWS_REGION'])

    main()
