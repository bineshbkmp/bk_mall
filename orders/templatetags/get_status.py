from django import template

register=template.Library()


@register.simple_tag(name='get_status') #decorator for modify function   the file-name is used in load statement,  in template page
def get_status(status):
    status=status-1
    status_array=['Confirmed','Processed','Delivered','Rejected']
    return status_array[status]

  
