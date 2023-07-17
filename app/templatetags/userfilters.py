from django import template

register=template.Library()


@register.filter('swapping')# swapping is the filter name for swap function
def swap(data):
    return data.swapcase()

@register.filter()#it considers function name as Filter name
def remove(data,arg):
    return data.replace(arg,'')


#register.filter('swap',swap)
#register.filter('remove',remove)


@register.filter()
def change(value):
    s=value.split()
    l=[]
    for i in range(len(s)):
        if i==0 or i==len(s)-1:
            l.append(s[i])
        else:
            l.append(s[i].lower())
    return ' '.join(l)


@register.filter()
def count(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub):]==sub:
            c+=1
    return c



