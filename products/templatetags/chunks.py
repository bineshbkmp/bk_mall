from django import template

register=template.Library()


@register.filter(name='chunks') #decorator for modify function
def chunks(list_data,chunk_size):
    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk   # yield statement is used by generators intead of return 
            chunk=[]
            i=0
    if chunk:
        yield chunk

